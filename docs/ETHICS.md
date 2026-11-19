# ETHICS — P10 — Détection deepfake (audio/vidéo, légère) (AEGIS)

Engagements éthiques du projet — stand-alone, labo local, GPU refused, anti-cloud.

- **Cible** : [AEGIS Détection deepfake (audio/vidéo, légère)](https://github.com/LaidiMohammed/aegis-p10-deepfake-light)
- **Périmètre** : [AEGIS Détection deepfake (audio/vidéo, légère)](https://aegis-p10-deepfake-light.vercel.app) — smoke + fonctions CLI.
- **GPU refused** : implementation uniquement CPU/pure Python.
- **Données locales** : sources acceptées : labo local (localhost, Juice Shop, DVWA, etc.).
- **Smoke au prof** : cmds à exécuter — voir README/scripts/run_smoke.sh.
- **Smoke clé de validation** : voir `smoke()` dans `src/deepfake_light_main.py` — doit retourner `{"ok": true, ...}`.
- **Site statique Vercel** : disponible pour la démo statique (smoke uniquement).

See SPEC.md (avec use cases + tableaux attendus).
