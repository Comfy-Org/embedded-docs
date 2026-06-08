# TripoSplat Prétraitement d'Image

Ce nœud rogne chaque image d'entrée en un carré centré sur fond noir, puis ajoute un remplissage pour atteindre la taille de sortie spécifiée. Il est conçu pour préparer les images pour le modèle 3D TripoSplat en garantissant un cadrage carré cohérent et une érosion facultative du mat alpha pour éviter les artefacts de bordure.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | Image(s) d'entrée à prétraiter | IMAGE | Oui | - |
| `mask` | Masque alpha de l'image, utilisé pour déterminer la zone de rognage | MASK | Oui | - |
| `erode_radius` | Érode le mat alpha de ce rayon en pixels avant le rognage (évite les débordements de bordure). Par défaut : 1 | INT | Oui | 0 à 16 |
| `size` | Taille d'image carrée. Le modèle est entraîné à 1024 ; les autres tailles fonctionnent mais sont hors distribution. Par défaut : 1024 | INT | Oui | 256 à 4096 (pas de 16) |

**Remarque :** L'entrée `mask` est requise et doit être fournie. Si le masque a une taille de lot différente de celle de l'image, il est automatiquement répété pour correspondre. Si les dimensions du masque diffèrent de celles de l'image, le masque est redimensionné pour correspondre à l'image par interpolation bilinéaire.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | Image(s) prétraitée(s) rognée(s) en un carré centré sur fond noir avec remplissage | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatPreprocessImage/fr.md)

---
**Source fingerprint (SHA-256):** `3f33dbc3a99ccb23ede767915a28fabdfa388edb8d5782edea3f8d03e5965b2a`
