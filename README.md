# VText 💬
WhatsApp jaisi chat app (PWA). Frontend: GitHub Pages, deploy: GitHub Actions, backend: Firebase (free).

## Setup (10 minute)
1. **Firebase**: console.firebase.google.com par project banao.
   - Build > Authentication > Sign-in method > **Email/Password** ON karo.
   - Build > Firestore Database > Create (production mode).
   - Firestore > Rules me `firestore.rules` ka content paste karke Publish karo.
   - Project settings > Your apps > Web (`</>`) > config copy karke `config.js` me paste karo.
2. **GitHub**: naya repo banao, saari files upload/push karo (branch `main`).
3. Repo > Settings > Pages > Source = **GitHub Actions**.
4. Actions tab me "Deploy VText" chalega. Link: `https://USERNAME.github.io/REPO/`
5. Firebase > Authentication > Settings > **Authorized domains** me `USERNAME.github.io` add karo.
6. Phone me link kholo > browser menu > **Add to Home screen** (app ki tarah install hogi).
