[app]

# (str) Title of your application
title = RussianCoin

# (str) Package name
package.name = russiancoin

# (str) Package domain (needed for android packaging)
package.domain = org.elnur

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) Application requirements
# Керекті кітапханаларды осында қосасың
requirements = python3,kivy,kivymd,pillow

# (str) Custom source folders for requirements
# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the libs of dists
android.skip_update = False

# (bool) If True, then copy the whole source dir to the device
android.copy_libs = 1

# -----------------------------------------------------------------------------
# АРХИТЕКТУРАЛАРДЫ БАПТАУ (Осы жер маңызды!)
# -----------------------------------------------------------------------------
# 32-бит (armeabi-v7a) және 64-бит (arm64-v8a) бірге жиналуы үшін:
android.archs = armeabi-v7a, arm64-v8a

# (bool) enables Android auto backup
android.allow_backup = True

# (str) The format used to package the app for release mode (aab or apk)
# Google Play үшін "aab", тест үшін "apk"
android.release_artifact = apk

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1