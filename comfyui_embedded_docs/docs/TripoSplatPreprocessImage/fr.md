# Prétraitement d'image TripoSplat

Ce nœud recadre chaque image d'entrée en un carré centré sur un fond noir, puis ajoute un remplissage (padding) pour atteindre la taille de sortie spécifiée. Il est conçu pour préparer les images pour le modèle 3D TripoSplat en garantissant un cadrage carré cohérent et une érosion facultative du cache alpha afin d'éviter les artefacts de bord.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | Les images d'entrée à prétraiter | IMAGE | Oui | - |
| `mask` | Masque alpha de l'image, utilisé pour déterminer la zone de recadrage | MASK | Oui | - |
| `erode_radius` | Érode le cache alpha de ce rayon en pixels avant le recadrage (évite les fuites de bord). Défaut : 1 | INT | Oui | 0 to 16 |
| `size` | Taille de l'image carrée. Le modèle est entraîné à 1024 ; les autres tailles fonctionnent mais sont hors distribution. Défaut : 1024 | INT | Oui | 256 to 4096 (step of 16) |

**Remarque :** L'entrée `mask` est requise et doit être fournie. Si le masque a une taille de lot différente de celle de l'image, il est automatiquement répété pour correspondre. Si les dimensions du masque diffèrent de celles de l'image, le masque est redimensionné pour correspondre à l'image à l'aide d'une interpolation bilinéaire. La taille de sortie est automatiquement arrondie à l'inférieur au multiple de 16 le plus proche pour garantir la compatibilité avec les exigences de patch DINOv3 et de stride de Flux2 VAE. Une erreur est levée si le masque ne contient aucun pixel de premier plan.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | Les images prétraitées recadrées en un carré centré sur un fond noir avec un remplissage | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatPreprocessImage/fr.md)

---
**Source fingerprint (SHA-256):** `ec66941846398ee6637576b11ae9d2f9576f6b05ed2ef730cdbf99a68fe9b838`
