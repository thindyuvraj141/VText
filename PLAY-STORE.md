# VText: Play Store checklist

## Ek baar karna hai
1. play.google.com/console par developer account (US$25 ek baar, ID verification).
2. **Personal account (13 Nov 2023 ke baad bana)**: production se pehle closed test me 12 log, 14 din lagatar opt-in. Organization account me ye nahi lagta.
3. Keystore banao (PC ya Termux par):
   `keytool -genkeypair -v -keystore vtext.jks -alias vtext -keyalg RSA -keysize 2048 -validity 10000`
   `base64 -w0 vtext.jks`  (output copy karo). Keystore aur password kahin safe rakho, kabhi repo me mat daalo.
4. GitHub repo > Settings > Secrets and variables > Actions me 4 secrets: `KEYSTORE_BASE64`, `KEYSTORE_PASSWORD`, `KEY_ALIAS`, `KEY_PASSWORD`.
5. `privacy.html`, `terms.html`, `delete-account.html` me `YOUR_EMAIL@example.com` ko apni email se badlo.
6. Firebase: Firestore Rules me naya `firestore.rules` Publish karo. Google Cloud console me `messages` aur `parts` par `expireAt` ki TTL policy lagao (privacy policy me yahi likha hai).

## Har release
Actions > **Build Play Store AAB** > Run workflow > Artifacts se `VText.aab` > Play Console me upload.
(Version code har run par apne aap badhta hai.)

## Play Console me bharna
- Package name: `com.thindyuvraj.vtext` (ek baar upload ke baad badal nahi sakta).
- Privacy policy URL: https://thindyuvraj141.github.io/VText/privacy.html
- Account deletion URL: https://thindyuvraj141.github.io/VText/delete-account.html
- Category: Communication. Ads: No. Content rating: questionnaire me "user-generated content / users interact" = Yes.
- Data safety: collected = email, name, user IDs, photos/videos, audio, messages, approx/precise location (only if user shares); encrypted in transit = Yes; users can request deletion = Yes; shared with third parties = No (Firebase = service provider).
- App access: reviewer ke liye ek test email + password do.
- Graphics: `store/icon-512.png`, `store/feature-graphic-1024x500.png`, aur phone se kam se kam 2 asli screenshots.

Short description: Simple private chat with photos, voice notes and groups.
Full description: VText is a simple chat app. Add friends by username, chat one-to-one or in groups, send photos, videos, voice messages, documents and your location. Messages disappear automatically after the time you choose.
