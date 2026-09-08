[app]
title = CryptoMachineX1
package.name = cryptomachinex1
package.domain = com.cryptomachinex1.app
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json,txt
version = 0.1
version.regex = __version__ = ['"]([^'"]+)['"]
version.filename = %(source.dir)s/main.py
requirements = python3==3.11.8,kivy==2.3.0,kivymd,pillow,certifi,charset-normalizer,idna,urllib3,requests,pycryptodome
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreement = True
android.ant = auto
p4a.branch = master
p4a.bootstrap = sdl2
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer:android]
# no extra
