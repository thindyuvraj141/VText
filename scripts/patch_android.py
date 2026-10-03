import os, re, pathlib
p = pathlib.Path('android/app/src/main/AndroidManifest.xml')
s = p.read_text()
perms = ['RECORD_AUDIO', 'MODIFY_AUDIO_SETTINGS', 'ACCESS_FINE_LOCATION', 'ACCESS_COARSE_LOCATION', 'CAMERA', 'POST_NOTIFICATIONS', 'USE_BIOMETRIC', 'USE_FINGERPRINT']
add = ''.join('    <uses-permission android:name="android.permission.%s"/>\n' % x for x in perms if x not in s)
add += '    <uses-feature android:name="android.hardware.camera" android:required="false"/>\n'
add += '    <uses-feature android:name="android.hardware.microphone" android:required="false"/>\n'
add += '    <uses-feature android:name="android.hardware.location" android:required="false"/>\n'
s = s.replace('</manifest>', add + '</manifest>')
if 'windowSoftInputMode' not in s:
    s = re.sub(r'<activity\b', '<activity android:windowSoftInputMode="adjustResize"', s, count=1)
p.write_text(s)
vc = os.environ.get('VERSION_CODE')
if vc:
    g = pathlib.Path('android/app/build.gradle')
    t = g.read_text()
    t = re.sub(r'versionCode\s*=?\s*\d+', 'versionCode = ' + vc, t, count=1)
    t = re.sub(r'versionName\s*=?\s*"[^"]*"', 'versionName = "1.0.' + vc + '"', t, count=1)
    g.write_text(t)
print('android project patched')
