# AEGIS — P10 — Détection deepfake (audio/vidéo, légère)

[![Vercel](https://img.shields.io/badge/Vercel-aegis-p10--blue?logo=vercel)](https://aegis-p10-deepfake-light.vercel.app)
[![Tests](https://img.shields.io/badge/Tests-passing-brightgreen)]

Détection deepfake (audio/vidéo, légère) — PFE P13 style AEGIS (Master 1 Sécurité informatique).

## Infos rapides

| Élément | Valeur |
|---|---|
| **GitHub** | https://github.com/LaidiMohammed/aegis-p10-deepfake-light |
| **Vercel** | https://aegis-p10-deepfake-light.vercel.app |
| **Stacks** | librosa, cv2, Pillow, reportlab |
| **Type** | ml |
| **Ethique** | Labo local, anti-GPU, anti-cloud, stand-alone |

## Install

```bash
pip install -r requirements.txt
make install  # (venv)
```

## Smoke & tests (démo à la prof)

```bash
make smoke   # ou: scripts/run_smoke.sh
make test
```

## Fonctions à exécuter à la démo

Voir [`docs/ETHICS.md`](docs/ETHICS.md), [`docs/SPEC.md`](docs/SPEC.md).
