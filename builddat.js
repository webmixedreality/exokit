const browserify = require('browserify')
const defaultBuiltins = require('browserify/lib/builtins')

browserify('./node_modules/node-dat-archive/', {
  insertGlobalVars: {
    process: () => 'require("process/browser.js")'
  },
  standalone: 'DatArchive',
  browserField: false,
  detectGlobals: true,
})
.exclude(Object.keys(defaultBuiltins))
.exclude('utp-native')
.bundle()
.pipe(process.stdout)
