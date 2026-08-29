[app]

title = Hello Kivy
package.name = hellokivy
package.domain = org.example

source.dir = .
source.include_exts = py

version = 0.1

requirements = python3,kivy

orientation = portrait

fullscreen = 0


[buildozer]

log_level = 2


[app:android]

android.permissions =


[buildozer:android]

android.archs = arm64-v8a
