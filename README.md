# Tender Radar Distiller

Static marketing site for Tender Radar Distiller.

## Run locally

```bash
python3 -m http.server 4173
```

Open `http://127.0.0.1:4173`.

## Rebuild design assets

The procurement triage board SVG is deterministic and generated from source:

```bash
python3 scripts/build-design-assets.py
```

Generated output lives in `assets/generated/` and is committed for GitHub Pages.
