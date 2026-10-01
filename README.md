# VText 💬
WhatsApp jaisi chat app (PWA). Frontend: GitHub Pages, deploy: GitHub Actions, backend: Firebase (free).

## Setup (10 minute)
1. **Firebase**: console.firebase.google.com par project banao.
   - Build > Authentication > Sign-in method > **Email/Password** ON karo.
   - Build > Firestore Database > Create (production mode).
   - Firestore > Rules me `firestore.rules` ka content paste karke Publish karo.
   - Project settings > Your apps > Web (`</>`) > config copy karke `config.js` me paste karo.
   - **Auto-delete (backup nahi):** Firestore > **TTL** tab > Create policy: collection group `messages`, field `expireAt`; phir ek aur: collection group `parts`, field `expireAt`. Messages 24 ghante baad khud delete ho jaate hain (app expire hue messages turant chhupa deti hai).
2. **GitHub**: naya repo banao, saari files upload/push karo (branch `main`).
3. Repo > Settings > Pages > Source = **GitHub Actions**.
4. Actions tab me "Deploy VText" chalega. Link: `https://USERNAME.github.io/REPO/`
5. Firebase > Authentication > Settings > **Authorized domains** me `USERNAME.github.io` add karo.
6. Phone me link kholo > browser menu > **Add to Home screen** (app ki tarah install hogi).

## Features
Username se dost add (➕), group (👥), text, photo (auto compress), video (max 3MB ~10-15 sec). Naya account banate waqt username chuno.
Purane version ke rules/accounts naye rules ke saath kaam nahi karenge, naya signup karo.

## APK (Capacitor)
1. Repo me `package.json`, `capacitor.config.json`, `scripts/`, `assets/` aur `.github/workflows/android.yml` bhi hone chahiye.
2. Actions tab > **Build APK** > **Run workflow**.
3. 5-10 min baad Releases (repo ka right side) me `VText.apk` milegi, ya run page ke Artifacts me.
4. APK site `thindyuvraj141.github.io/VText` se load hoti hai, to `index.html` badalne par APK dobara banane ki zaroorat nahi.
