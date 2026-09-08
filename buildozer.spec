[app]
title = CryptoMasterX1
package.name = cryptomasterx1
package.domain = org.cmx1
source.dir =.
source.include_exts = py,png,jpg,kv,json,txt
version = 1.0
requirements = python3,kivy,requests,websocket-client,cryptography==3.4.8
orientation = portrait
android.permissions = INTERNET,ACCESS_NETWORK_STATE,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
