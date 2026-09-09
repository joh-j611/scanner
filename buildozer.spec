[app]

# (str) Title of your application
title = Airtime Scanner

# (str) Package name
package.name = airtimescanner

# (str) Package domain (needed for android/ios packaging)
package.domain = org.johj611

# (str) Source code where the main.py live
source.dir = .

# (str) Main entry point file
source.main = main.py

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.2

# (list) Application requirements
requirements = python3,kivy,plyer

# (str) Supported orientation
orientation = portrait

# (list) Permissions
android.permissions = CALL_PHONE,CAMERA

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 24

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use
android.ndk_api = 24

# (bool) Automatically accept SDK license agreements
android.accept_sdk_license = True

# (bool) Skip trying to update the Android sdk
android.skip_update = False

# (str) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature
android.allow_backup = True

# (str) Package format for release mode
android.release_artifact = apk

[buildozer]

# (int) Log level
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
# (str) python-for-android branch to use, defaults to master
p4a.branch = master
