# Aperçu d'échantillonnage TripoSplat

Ce nœud patch un modèle TripoSplat afin que, lorsqu'il est utilisé avec le nœud KSampler standard, un aperçu en direct du splat gaussien décodé soit affiché à chaque étape d'échantillonnage. Il fonctionne en enveloppant le callback de l'échantillonneur pour décoder la sortie du modèle en une image d'aperçu après chaque étape.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle TripoSplat à patcher pour l'aperçu en direct | MODEL | Oui | |
| `vae` | Décodeur VAE de TripoSplat | VAE | Oui | |
| `octree_level` | Profondeur de l'octree pour le décodage de l'aperçu (plus bas = moins coûteux/plus grossier). Défaut : 5 | INT | Non | 2 à 8 |
| `num_gaussians` | Nombre de gaussiennes à produire pour l'aperçu (arrondi à un multiple de 32). Défaut : 16384 | INT | Non | 1024 à 262144 (pas : 32) |
| `yaw` | Lacet de la caméra d'aperçu en degrés. Défaut : 90.0 | FLOAT | Non | -360.0 à 360.0 (pas : 1.0) |
| `pitch` | Tangage de la caméra d'aperçu en degrés. Défaut : 15.0 | FLOAT | Non | -89.0 à 89.0 (pas : 1.0) |
| `point_size` | Rayon maximal des splats en pixels. Chaque gaussienne est dimensionnée à partir de son échelle et plafonnée ici ; plus bas = plus fin/plus ponctuel, plus haut = plus épais. Défaut : 3 | INT | Non | 1 à 16 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `MODEL` | Le modèle TripoSplat patché avec la fonctionnalité d'aperçu en direct ajoutée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatSamplingPreview/fr.md)

---
**Source fingerprint (SHA-256):** `78678b65df325da964cfd3e8cd0dc07fa25b92d26bb2057117db413a205e9535`
