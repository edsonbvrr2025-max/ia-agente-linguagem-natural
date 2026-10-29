[app]

# (str) Title of your application
title = ORÁCULO

# (str) Package name
package.name = oraculo

# (str) Package domain (needed for android/ios packaging)
package.domain = org.oraculo

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,md,yaml,txt,sh

# (list) List of inclusions using pattern matching
# source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
# source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests,bin,buildozer,.buildozer,models,__pycache__,.git,backups,logs,.venv,venv,env

# (list) List of exclusions using pattern matching
# source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/oraculo/__init__.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,pyyaml,llama-cpp-python,pure-python-adb,rich,requests,psutil,sqlite-vec,onnxruntime

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source =

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/assets/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/assets/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
# services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# author = © Copyright Info

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
# android.presplash_color = #FFFFFF

# (string) Presplash animation using Lottie format
# android.presplash_lottie =

# (list) Permissions
android.permissions = INTERNET,RECORD_AUDIO,WAKE_LOCK,FOREGROUND_SERVICE,FOREGROUND_SERVICE_MICROPHONE,FOREGROUND_SERVICE_MEDIA_PLAYBACK,POST_NOTIFICATIONS,VIBRATE,BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT,MODIFY_AUDIO_SETTINGS

# (list) Features (adds uses-feature -tags to manifest)
# android.features = android.hardware.microphone

# (int) Target Android API, should be as high as possible.
# android.api = 34

# (int) Minimum API your APK / AAB will support.
# android.minapi = 30

# (int) Android SDK version to use
# android.sdk = 34

# (str) Android NDK version to use
# android.ndk = 27c

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
# android.ndk_api = 30

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
# android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
# android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid any communication with the internet
# android.skip_update = False

# (bool) If True, then automatically accept SDK license agreements
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
# android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
# android.activity_class_name = org.kivy.android.PythonActivity

# (str) Extra xml to write directly inside the <manifest> element of AndroidManifest.xml
# Use that parameter to provide a filename from where to load your custom XML code
# android.extra_manifest_xml =

# (str) Extra xml to write directly inside the <manifest><application> tag of AndroidManifest.xml
# android.extra_application_xml =

# (str) Full name including package path of the Java class that implements PythonService
# android.service_class_name = org.kivy.android.PythonService

# (str) Android logcat filters to use
android.logcat_filters = *:S python:I

# (bool) Android logcat auto filter
# android.logcat_auto_filter = False

# (str) Android additional adb arguments
# android.adb_args = -H host.docker.internal

# (bool) Copy library instead of making a libpymodules.so
# android.copy_libs = 1

# (list) The Android archs to build for: arm64-v8a, armeabi-v7a, x86, x86_64
# In past, was `android.archs = arm64-v8a, armeabi-v7a`
android.archs = arm64-v8a

# (int) overrides automatic versionCode computation (used in build.gradle)
# android.versioncode =

# (str) custom python-for-android branch to use, if not master
# p4a.branch = master

# (str) OUYA Console category
# android.ouya.category = GAME

# (str) Filename of OUYA Console icon
# android.ouya.icon.filename =

# (str) XML to include in the AndroidManifest.xml <activity> tag for the main activity
# android.manifest_activity_xml =

# (str) intent filters to add to the main activity in AndroidManifest.xml
android.manifest_intent_filters = <intent-filter><action android:name="android.intent.action.MAIN"/><category android:name="android.intent.category.LAUNCHER"/></intent-filter><intent-filter><action android:name="android.intent.action.VOICE_COMMAND"/></intent-filter>

# (bool) Whether to use the new Gradle-based build system (recommended)
android.gradle = True

# (str) gradle properties file (relative to buildozer.spec)
# android.gradle_properties =

# (str) extra gradle properties to pass to the gradle build
# android.gradle_properties =

# (bool) Enable AndroidX support (recommended)
android.enable_androidx = True

# (str) The Android Gradle plugin version to use
# android.gradle_plugin = 8.1.0

# (str) The Kotlin version to use
# android.kotlin_version = 1.9.0

# (bool) If True, build AAB instead of APK
android.build_aab = False

# (str) Signing configuration for release builds
# android.signing.keystore = %(source.dir)s/release.keystore
# android.signing.keyalias = release
# android.signing.storepass = 
# android.signing.keypass =

# (str) Proguard configuration file
# android.proguard =

# (int) Maximum number of concurrent jobs for the build
# android.concurrent_jobs = 4

# (str) Python-for-android branch to use
# p4a.branch = master

# (str) Extra arguments to pass to python-for-android
# p4a.extra_args =

#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
# ios.kivy_ios_dir =

# (str) Name of the certificate to use for signing the debug version
# ios.codesign.debug =

# (str) Name of the certificate to use for signing the release version
# ios.codesign.release =

#
# Buildozer specific
#

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
# bin_dir = ./bin

# (list) Buildozer will run "command" in the "env" environment
# Each "command" has the format: "env:command"
# [buildozer]
# commands =

# (str) Profile to use for the build
# profile = 

# (str) Sections to include in the spec file
# sections = 

# (str) Command to run after building the APK
# postbuild = 

# [buildozer] 
# targets =