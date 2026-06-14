# Nœud d'Image Clé Runway Aleph2

Ce nœud ancre une image de guidage à un moment spécifique de votre vidéo d'entrée, permettant au modèle Aleph2 d'orienter l'édition à cet endroit précis de votre séquence. Connectez ce nœud à l'entrée "keyframes" du nœud Runway Aleph2 Vidéo vers Vidéo, et enchaînez plusieurs exemplaires (jusqu'à 5) via l'entrée optionnelle "keyframes".

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image de guidage à appliquer au moment choisi de la vidéo d'entrée. | IMAGE | Oui | - |
| `timing` | Comment placer cette image sur la ligne temporelle de la vidéo d'entrée. | COMBO | Oui | Voir ci-dessous |
| `keyframes` | Images clés antérieures optionnelles à chaîner avec celle-ci. | KEYFRAME | Non | - |

### Options du paramètre Timing

Le paramètre `timing` propose deux modes :

| Mode | Sous-paramètre | Description | Plage |
|------|----------------|-------------|-------|
| "Secondes absolues" | `seconds` | Temps en secondes depuis le début de la vidéo d'entrée où cette image s'applique (par défaut : 0.0) | 0.0 à 30.0, pas de 0.1 |
| "Fraction de durée" | `fraction` | Position dans la vidéo d'entrée où cette image s'applique, exprimée en fraction de sa durée (0.0 = début, 1.0 = fin) (par défaut : 0.0) | 0.0 à 1.0, pas de 0.01 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `keyframes` | Une chaîne d'images clés incluant celle-ci et toutes les images clés précédemment connectées. | KEYFRAME |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2KeyframeNode/fr.md)

---
**Source fingerprint (SHA-256):** `b5ac6553166b7366fd35f97740861be163f91bc2353f5f83bdc2f04bf40f8478`
