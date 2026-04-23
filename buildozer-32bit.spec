[app]
title = Mortgage Calculator
package.name = mortgagecalculator
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas
version = 0.1
requirements = python3==3.9.13,kivy==2.0.0,kivymd==1.1.1,sdl2_ttf==2.0.15,openpyxl
orientation = portrait
fullscreen = 0
android.arch = armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
