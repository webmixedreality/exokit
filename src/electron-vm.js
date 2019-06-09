const path = require('path');
const {EventEmitter} = require('events');
const stream = require('stream');
const net = require('net');
const child_process = require('child_process');
const {TextEncoder} = require('util');

const electron = require('electron');

const {process} = global;

const TYPES = (() => {
  let iota = 0;
  return {
    CONSOLE: ++iota,
    IMAGEDATA: ++iota,
  };
})();

let numVms = 0;

class ElectronVm extends EventEmitter {
  constructor({url = 'http://google.com', width = 1280, height = 1024} = {}) {
    super();
    
    const server = net.createServer(stream => {
      cp.stdin
        .pipe(stream)
        .pipe(cp.stdout);
    });
    const pipePath = '\\\\.\\pipe\\exokit-electron' + numVms++;
    server.listen(pipePath);
    
    const cp = child_process.spawn(electron, [path.join(__dirname, 'electron-child.js'), pipePath]);
    cp.stdin = new stream.PassThrough();
    cp.stdout = new stream.PassThrough();

    const bs = [];
    let bsLength = 0;
    const _pull  = l => {
      if (bsLength >= l) {
        const result = Buffer.allocUnsafe(l);
        let localLength = 0;

        while (localLength < l) {
          const need = l - localLength;
          let b = bs.shift();
          if (b.length >= need) {
            b.copy(result, localLength, 0, need);
            b = b.slice(need);
            if (b.length > 0) {
              bs.unshift(b);
            }
            localLength += need;
            bsLength -= need;
          } else {
            b.copy(result, localLength, 0, b.length);
            localLength += b.length;
            bsLength -= b.length;
          }
        }

        return result;
      } else {
        return null;
      }
    };
    cp.stdout.on('data', b => {
      // console.log('got data', b.slice(0, 40).toString('hex'), JSON.stringify(b.slice(0, 40).toString()));

      bs.push(b);
      bsLength += b.byteLength;

      while (bsLength >= Uint32Array.BYTES_PER_ELEMENT) {
        let [b] = bs;
        if ((b.byteOffset % Uint32Array.BYTES_PER_ELEMENT) !== 0) {
          const oldB = b;
          b = bs[0] = new Buffer(new ArrayBuffer(oldB.byteLength), 0, oldB.byteLength);
          oldB.copy(b, 0, 0, oldB.byteLength);
        }
        const [type] = new Uint32Array(b.buffer, b.byteOffset, 1);
        // console.log('got type', type);
        switch (type) {
          case TYPES.CONSOLE: {
            if (b.length < (1+1)*Uint32Array.BYTES_PER_ELEMENT) {
              console.warn(new Error('did not get full header from electron pipe').stack);
            }
            const header = new Uint32Array(b.buffer, b.byteOffset + Uint32Array.BYTES_PER_ELEMENT, 1);
            const [size] = header;
            b = _pull((1+1)*Uint32Array.BYTES_PER_ELEMENT + size);
            if (b) {
              b = Buffer.from(b.buffer, b.byteOffset + (1+1)*Uint32Array.BYTES_PER_ELEMENT, size);
              const s = new TextDecoder().decode(b);
              process.stdout.write(s);
            } else {
              // console.log('failed to pull', (1+1)*Uint32Array.BYTES_PER_ELEMENT + size, bsLength);
              return;
            }
            break;
          }
          case TYPES.IMAGEDATA: {
            if (b.length < (1+4)*Uint32Array.BYTES_PER_ELEMENT) {
              console.warn(new Error('did not get full header from electron pipe').stack);
            }
            const header = new Uint32Array(b.buffer, b.byteOffset + Uint32Array.BYTES_PER_ELEMENT, 4);
            const [x, y, width, height] = header;
            // console.log('got header', x, y, width, height);
            b = _pull((1+4)*Uint32Array.BYTES_PER_ELEMENT + width*height*4);
            if (b) {
              const imageData = new Buffer(b.buffer, b.byteOffset + (1+4)*Uint32Array.BYTES_PER_ELEMENT, width*height*4);
              console.log('got frame', x, y, width, height, imageData.byteLength);
            } else {
              return;
            }
            break;
          }
          default: {
            console.warn('electron parent got invalid type', type);
            throw new Error('fail');
            return;
          }
        }
      }
    });
    cp.stdout.on('end', () => {
      console.log('stdout end');
    });
    cp.stderr.on('data', b => {
      process.stdout.write(b);
    });
    cp.stderr.on('end', () => {
      console.log('stderr end');
    });
    cp.on('exit', () => {
      console.log('child process exit');
    });
    
    this.childProcess = cp;
    this.runAsync({
      method: 'initialize',
      url,
      width,
      height,
    });
  }
  
  runAsync(e) {
    const s = JSON.stringify(e);
    const uint8Array = new TextEncoder().encode(s);
    const buffer = new Buffer(uint8Array.buffer, uint8Array.byteOffset, uint8Array.byteLength);
    {
      const b = Uint32Array.from([buffer.length]);
      const b2 = new Buffer(b.buffer, b.byteOffset, b.byteLength);
      this.childProcess.stdin.write(b2);
    }
    this.childProcess.stdin.write(buffer);
  }
  
  postMessage(message) {
    this.runAsync({
      method: 'postMessage',
      message,
    });
  }

  runJs(jsString, scriptUrl, startLine) {
    this.runAsync({
      method: 'runJs',
      jsString,
      scriptUrl,
      startLine,
    });
  }

  sendInputEvent(event) {
    this.runAsync({
      method: 'sendInputEvent',
      event,
    });
  }

  sendMouseMove(x, y) {
    this.sendInputEvent({
      type: 'mousemove',
      x,
      y,
    });
  }

  destroy() {
    this.childProcess.kill(9);
  }
}
module.exports.ElectronVm = ElectronVm;

/* const browser = new ElectronVm({
  url: 'https://google.com',
  width: 1920,
  height: 1080,
});
browser.postMessage({
  lol: 'zol',
}); */

/* {
  process.on('SIGINT', () => {
    // cp.kill(9);
    console.log('SIGINT...');
    process.exit();
  });
  process.on('SIGTERM', () => {
    // cp.kill(9);
    console.log('SIGTERM...');
    process.exit();
  });
  process.on('exit', () => {
    console.log('exiting...');
    cp.kill(9);
  });
} */