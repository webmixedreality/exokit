{
  'targets': [
    {
      'target_name': 'exokit',
      'conditions': [
        ['OS=="win"', {
          'sources': [
            'main.cpp',
            'deps/exokit-bindings/bindings/src/*.cc',
            'deps/exokit-bindings/util/src/*.cc',
            'deps/exokit-bindings/canvas/src/*.cpp',
            'deps/exokit-bindings/nanosvg/src/*.cpp',
            'deps/exokit-bindings/canvascontext/src/*.cc',
            'deps/exokit-bindings/webglcontext/src/*.cc',
            'deps/exokit-bindings/platform/windows/src/*.cpp',
            'deps/exokit-bindings/webaudiocontext/src/*.cpp',
            'deps/exokit-bindings/videocontext/src/*.cpp',
            'deps/exokit-bindings/glfw/src/*.cc',
            'deps/openvr/src/*.cpp',
            'deps/exokit-bindings/leapmotion/src/*.cc',
          ],
          'include_dirs': [
            "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/include')\")",
            "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/core')\")",
            "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/config')\")",
            "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/gpu')\")",
            "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/effects')\")",
            "<!(node -e \"console.log(require.resolve('native-audio-deps').slice(0, -9) + '/include')\")",
            "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/include')\")",
            "<!(node -e \"console.log(require.resolve('native-openvr-deps').slice(0, -9) + '/headers')\")",
            "<!(node -e \"console.log(require.resolve('leapmotion').slice(0, -9) + '/include')\")",
            '<(module_root_dir)/deps/exokit-bindings',
            '<(module_root_dir)/deps/exokit-bindings/utf8',
            '<(module_root_dir)/deps/exokit-bindings/node',
            '<(module_root_dir)/deps/exokit-bindings/native_app_glue',
            '<(module_root_dir)/deps/exokit-bindings/util/include',
            '<(module_root_dir)/deps/exokit-bindings/bindings/include',
            '<(module_root_dir)/deps/exokit-bindings/canvas/include',
            '<(module_root_dir)/deps/exokit-bindings/nanosvg/include',
            '<(module_root_dir)/deps/exokit-bindings/canvascontext/include',
            '<(module_root_dir)/deps/exokit-bindings/webglcontext/include',
            '<(module_root_dir)/deps/exokit-bindings/webaudiocontext/include',
            '<(module_root_dir)/deps/exokit-bindings/videocontext/include',
            '<(module_root_dir)/deps/exokit-bindings/glfw/include',
            '<(module_root_dir)/deps/openvr/include',
            '<(module_root_dir)/deps/exokit-bindings/leapmotion/include',
          ],
          'library_dirs': [
            "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/lib/windows/glew')\")",
            "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/lib/windows/glfw')\")",
            "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/lib/windows')\")",
            "<!(node -e \"console.log(require.resolve('native-audio-deps').slice(0, -9) + '/lib/windows')\")",
            "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/win')\")",
            "<!(node -e \"console.log(require.resolve('native-openvr-deps').slice(0, -9) + '/lib/win64')\")",
            "<!(node -e \"console.log(require.resolve('leapmotion').slice(0, -9) + '/lib/win')\")",
            "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64')\")",
          ],
          'libraries': [
            'opengl32.lib',
            'glew32.lib',
            'glfw3dll.lib',
            'gdiplus.lib',
            'skia.lib',
            'LabSound.lib',
            'avformat.lib',
            'avcodec.lib',
            'avutil.lib',
            'swscale.lib',
            'swresample.lib',
            'openvr_api.lib',
            'Leap.lib',
          ],
          'copies': [
            {
              'destination': '<(module_root_dir)/build/Release/',
              'files': [
                "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/lib/windows/glew/glew32.dll')\")",
                "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/lib/windows/glfw/glfw3.dll')\")",
                "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/win/avformat-58.dll')\")",
                "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/win/avcodec-58.dll')\")",
                "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/win/avutil-56.dll')\")",
                "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/win/swscale-5.dll')\")",
                "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/win/swresample-3.dll')\")",
                "<!(node -e \"console.log(require.resolve('native-openvr-deps').slice(0, -9) + '/bin/win64/openvr_api.dll')\")",
                "<!(node -e \"console.log(require.resolve('leapmotion').slice(0, -9) + '/lib/win/Leap.dll')\")",
              ]
            }
          ],
          'defines': [
            'NOMINMAX',
          ],
          'conditions': [
            ['"<!(echo %MAGICLEAP%)" != "%MAGICLEAP%"', {
              'sources': [
                'deps/exokit-bindings/magicleap/src/*.cc',
              ],
              'include_dirs': [
                '<(module_root_dir)/deps/exokit-bindings/magicleap/include',
                "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/include')\")",
              ],
              'libraries': [
                'ml_app_analytics.lib',
                'ml_audio.lib',
                'ml_camera.lib',
                'ml_camera_metadata.lib',
                'ml_dispatch.lib',
                'ml_ext_logging.lib',
                'ml_graphics.lib',
                'ml_identity.lib',
                'ml_input.lib',
                'ml_lifecycle.lib',
                'ml_mediacodec.lib',
                'ml_mediacodeclist.lib',
                'ml_mediacrypto.lib',
                'ml_mediadrm.lib',
                'ml_mediaerror.lib',
                'ml_mediaextractor.lib',
                'ml_mediaformat.lib',
                'ml_mediaplayer.lib',
                'ml_musicservice.lib',
                'ml_musicservice_provider.lib',
                'ml_perception_client.lib',
                'ml_privileges.lib',
                'ml_purchase.lib',
                'ml_screens.lib',
                'ml_secure_storage.lib',
                'ml_sharedfile.lib',
                'ml_virtual_device.lib',
              ],
              'copies': [
                {
                  'destination': '<(module_root_dir)/build/Release/',
                  'files': [
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/EyeTrackingStateMixer.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/GesturesMixer.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/HeadStateMixer.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/InputControllerMixer.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/OrientationMixer.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/PassthroughMixer.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/PositionMixer.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/assimp-vc140-mt.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/glfw3.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_app_analytics.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_audio.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_camera.dll')\")", "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_camera_metadata.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_dispatch.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_ext_logging.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_graphics.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_identity.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_input.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_lifecycle.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_mediacodec.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_mediacodeclist.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_mediacrypto.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_mediadrm.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_mediaerror.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_mediaextractor.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_mediaformat.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_mediaplayer.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_musicservice.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_musicservice_provider.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_perception_client.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_privileges.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_purchase.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_screens.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_secure_storage.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_sharedfile.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/ml_virtual_device.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/portaudio_x64.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/protobuf-cpp-full.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/z.dll')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/win64/zmq.dll')\")",
                  ],
                }
              ],
              'defines': [
                'MAGICLEAP=$(MAGICLEAP)',
              ],
            }],
          ],
        }],
        ['OS=="linux"', {
          'sources': [
            'main.cpp',
            '<!@(ls -1 deps/exokit-bindings/bindings/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/util/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/canvas/src/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/nanosvg/src/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/canvascontext/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/webglcontext/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/webaudiocontext/src/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/videocontext/src/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/glfw/src/*.cc)',
            '<!@(ls -1 deps/openvr/src/*.cpp)',
          ],
          'include_dirs': [
            "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/include')\")",
            "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/core')\")",
            "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/config')\")",
            "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/gpu')\")",
            "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/effects')\")",
            "<!(node -e \"console.log(require.resolve('native-audio-deps').slice(0, -9) + '/include')\")",
            "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/include')\")",
            "<!(node -e \"console.log(require.resolve('native-openvr-deps').slice(0, -9) + '/headers')\")",
            '<(module_root_dir)/deps/exokit-bindings',
            '<(module_root_dir)/deps/exokit-bindings/utf8',
            '<(module_root_dir)/deps/exokit-bindings/node',
            '<(module_root_dir)/deps/exokit-bindings/native_app_glue',
            '<(module_root_dir)/deps/exokit-bindings/util/include',
            '<(module_root_dir)/deps/exokit-bindings/bindings/include',
            '<(module_root_dir)/deps/exokit-bindings/canvas/include',
            '<(module_root_dir)/deps/exokit-bindings/nanosvg/include',
            '<(module_root_dir)/deps/exokit-bindings/canvascontext/include',
            '<(module_root_dir)/deps/exokit-bindings/webglcontext/include',
            '<(module_root_dir)/deps/exokit-bindings/webaudiocontext/include',
            '<(module_root_dir)/deps/exokit-bindings/videocontext/include',
            '<(module_root_dir)/deps/exokit-bindings/glfw/include',
            '<(module_root_dir)/deps/openvr/include',
          ],
          'library_dirs': [
            "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/lib/linux/glew')\")",
            "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/lib/linux/glfw')\")",
            "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/lib/linux')\")",
            "<!(node -e \"console.log(require.resolve('native-audio-deps').slice(0, -9) + '/lib/linux')\")",
            "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/linux')\")",
            "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/linux/libavformat')\")",
            "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/linux/libavcodec')\")",
            "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/linux/libavutil')\")",
            "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/linux/libswscale')\")",
            "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/linux/libswresample')\")",
            "<!(node -e \"console.log(require.resolve('native-openvr-deps').slice(0, -9) + '/lib/linux64')\")",
          ],
          'libraries': [
            '-lGL',
            '-lGLU',
            '-lX11',
            '-lGLEW',
            '-lglfw3',
            '-lfontconfig',
            '-lfreetype',
            '-lpng16',
            '-lskia',
            '-lLabSound',
            '-lavformat',
            '-lavcodec',
            '-lavutil',
            '-lswscale',
            '-lswresample',
            '-lopenvr_api',
            '-luuid',
          ],
          'ldflags': [
            '-Wl,-Bsymbolic', # required for ffmpeg asm linkage
            '-Wl,--no-as-needed', # required to prevent elision of shared object linkage

            "-Wl,-rpath,<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/lib/linux/glew')\")",
            "-Wl,-rpath,<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/lib/linux/glfw')\")",
            "-Wl,-rpath,<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/lib/linux')\")",
            "-Wl,-rpath,<!(node -e \"console.log(require.resolve('native-audio-deps').slice(0, -9) + '/lib/linux')\")",
            "-Wl,-rpath,<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/linux/libavformat')\")",
            "-Wl,-rpath,<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/linux/libavcodec')\")",
            "-Wl,-rpath,<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/linux/libavutil')\")",
            "-Wl,-rpath,<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/linux/libswscale')\")",
            "-Wl,-rpath,<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/linux/libswresample')\")",
            "-Wl,-rpath,<!(node -e \"console.log(require.resolve('native-openvr-deps').slice(0, -9) + '/bin/linux64')\")",
          ],
          'defines': [
            'NOMINMAX',
          ],
        }],
        ['OS=="mac"', {
          'sources': [
            'main.cpp',
            '<!@(ls -1 deps/exokit-bindings/bindings/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/util/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/canvas/src/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/nanosvg/src/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/canvascontext/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/webglcontext/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/webaudiocontext/src/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/videocontext/src/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/glfw/src/*.cc)',
            '<!@(ls -1 deps/openvr/src/*.cpp)',
          ],
          'include_dirs': [
            "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/include')\")",
            "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/core')\")",
            "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/config')\")",
            "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/gpu')\")",
            "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/include/effects')\")",
            "<!(node -e \"console.log(require.resolve('native-audio-deps').slice(0, -9) + '/include')\")",
            "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/include')\")",
            "<!(node -e \"console.log(require.resolve('native-openvr-deps').slice(0, -9) + '/headers')\")",
            '<(module_root_dir)/deps/exokit-bindings',
            '<(module_root_dir)/deps/exokit-bindings/utf8',
            '<(module_root_dir)/deps/exokit-bindings/node',
            '<(module_root_dir)/deps/exokit-bindings/native_app_glue',
            '<(module_root_dir)/deps/exokit-bindings/util/include',
            '<(module_root_dir)/deps/exokit-bindings/bindings/include',
            '<(module_root_dir)/deps/exokit-bindings/canvas/include',
            '<(module_root_dir)/deps/exokit-bindings/nanosvg/include',
            '<(module_root_dir)/deps/exokit-bindings/canvascontext/include',
            '<(module_root_dir)/deps/exokit-bindings/webglcontext/include',
            '<(module_root_dir)/deps/exokit-bindings/webaudiocontext/include',
            '<(module_root_dir)/deps/exokit-bindings/videocontext/include',
            '<(module_root_dir)/deps/exokit-bindings/glfw/include',
            '<(module_root_dir)/deps/openvr/include',
          ],
          'library_dirs': [
            "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/lib/macos/glew')\")",
            "<!(node -e \"console.log(require.resolve('native-graphics-deps').slice(0, -9) + '/lib/macos/glfw')\")",
            "<!(node -e \"console.log(require.resolve('native-canvas-deps').slice(0, -9) + '/lib/macos')\")",
            "<!(node -e \"console.log(require.resolve('native-audio-deps').slice(0, -9) + '/lib/macos')\")",
            "<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/macos')\")",
          ],
          'libraries': [
            '-framework OpenGL',
            '-framework Cocoa',
            '-lGLEW',
            '-lglfw3',
            '-lskia',
            '-framework CoreAudio',
            '-framework AudioUnit',
            '-framework AudioToolbox',
            '-llabsound',
            '-lavformat',
            '-lavcodec',
            '-lavutil',
            '-lswscale',
            '-lswresample',
            "-F <!(node -e \"console.log(require.resolve('native-openvr-deps').slice(0, -9) + '/bin/osx64')\")",
            '-framework OpenVR',
          ],
          'link_settings': {
            'libraries': [
              "-Wl,-rpath,<!(node -e \"console.log(require.resolve('native-audio-deps').slice(0, -9) + '/lib/macos')\")",
              "-Wl,-rpath,<!(node -e \"console.log(require.resolve('native-video-deps').slice(0, -9) + '/lib/macos')\")",
              "-Wl,-rpath,<!(node -e \"console.log(require.resolve('native-openvr-deps').slice(0, -9) + '/bin/osx64')\")",
              '-framework OpenVR',
            ],
          },
          'conditions': [
            ['"<!(echo $MAGICLEAP)" != ""', {
              'sources': [
                'deps/exokit-bindings/magicleap/src/*.cc',
              ],
              'include_dirs': [
                '<(module_root_dir)/deps/exokit-bindings/magicleap/include',
                "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/include')\")",
              ],
              'library_dirs': [
                "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx')\")",
              ],
              'link_settings': {
                'libraries': [
                  "-rpath <!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/')\")",
                  "-Wl,-rpath,<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/')\")",
                  '-lml_lifecycle',
                  '-lEyeTrackingStateMixer',
                  '-lGesturesMixer',
                  '-lHeadStateMixer',
                  '-lInputControllerMixer',
                  '-lOrientationMixer',
                  '-lPassthroughMixer',
                  '-lPositionMixer',
                  '-lassimp',
                  '-lml_app_analytics',
                  '-lml_audio',
                  '-lml_camera',
                  '-lml_camera_metadata',
                  '-lml_dispatch',
                  '-lml_ext_logging',
                  '-lml_graphics',
                  '-lml_identity',
                  '-lml_input',
                  '-lml_lifecycle',
                  '-lml_mediacodec',
                  '-lml_mediacodeclist',
                  '-lml_mediacrypto',
                  '-lml_mediadrm',
                  '-lml_mediaerror',
                  '-lml_mediaextractor',
                  '-lml_mediaformat',
                  '-lml_mediaplayer',
                  '-lml_musicservice',
                  '-lml_musicservice_provider',
                  '-lml_perception_client',
                  '-lml_privileges',
                  '-lml_purchase',
                  '-lml_screens',
                  '-lml_secure_storage',
                  '-lml_sharedfile',
                  '-lml_virtual_device',
                  '-lportaudio',
                  '-lprotobuf-cpp-full',
                  '-lvpx.4',
                  '-lz',
                  '-lzmq',
                ],
              },
              'copies': [
                {
                  'destination': '<(module_root_dir)/build/Release/',
                  'files': [
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_perception_client.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_lifecycle.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libz.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_camera_metadata.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_identity.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_mediacrypto.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libzmq.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_ext_logging.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_mediaformat.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libvpx.4.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_sharedfile.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_mediaextractor.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libEyeTrackingStateMixer.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_virtual_device.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_camera.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libHeadStateMixer.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libGesturesMixer.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_musicservice_provider.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_screens.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libPassthroughMixer.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_purchase.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_mediadrm.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_secure_storage.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_mediaplayer.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_mediacodec.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_dispatch.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_privileges.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libportaudio.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libPositionMixer.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_input.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libInputControllerMixer.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libassimp.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libOrientationMixer.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_graphics.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_mediaerror.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_musicservice.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_app_analytics.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_audio.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libprotobuf-cpp-full.dylib')\")",
                    "<!(node -e \"console.log(require.resolve('magicleap').slice(0, -9) + '/lib/osx/libml_mediacodeclist.dylib')\")",
                  ],
                }
              ],
              'defines': [
                'MAGICLEAP=$(MAGICLEAP)',
              ],
            }],
          ],
        }],
      ],
    },
  ],
}
