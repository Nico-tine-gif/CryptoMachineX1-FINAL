[app]
title = CryptoMachineX1
package.name = cryptomachinex1
package.domain = org.kivy.cryptomachinex1

source.dir =.
source.include_exts = py
source.include_patterns = main.py
source.exclude_patterns = backup*, archive*, phase*, *backup*, *archive*, tests,.buildozer,.git, __pycache__, *.backup, *.bak

version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a, armeabi-v7a
p4a.bootstrap = sdl2
