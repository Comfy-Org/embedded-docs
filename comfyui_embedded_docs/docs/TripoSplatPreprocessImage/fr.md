# Prétraitement d'image TripoSplat

Ce nœud recadre chaque image d’entrée en un carré centré sur fond noir et ajoute un remplissage pour atteindre la taille de sortie spécifiée. Il est conçu pour préparer les images pour le modèle 3D TripoSplat en garantissant un cadrage carré cohérent et une érosion facultative du matte alpha afin d’éviter les artefacts de bord.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L’image ou les images d’entrée à prétraiter. | IMAGE | Oui | - |
| `mask` | Masque alpha pour l’image, utilisé pour déterminer la zone de recadrage. | MASK | Oui | - |
| `erode_radius` | Érode le matte alpha de ce rayon en pixels avant le recadrage (évite les débordements de bord). Défaut : 1. Mettez à 0 pour désactiver l’érosion. | INT | Oui | 0 à 16 |
| `size` | Taille de l’image carrée. Le modèle est entraîné à 1024 ; les autres tailles fonctionnent mais sont hors distribution. Défaut : 1024. | INT | Oui | 256 à 4096 (step of 16) |

**Remarque :** L’entrée `mask` est requise et doit être fournie. Si le masque a une taille de lot différente de celle de l’image, il est automatiquement répété pour correspondre. Si les dimensions du masque diffèrent de celles de l’image, le masque est redimensionné pour correspondre à l’image par interpolation bilinéaire. La taille de sortie est automatiquement arrondie au multiple de 16 le plus proche (minimum 16) pour garantir la compatibilité avec les exigences de pas des patchs DINOv3 et de stride du VAE Flux2. Le nœud génère une erreur si le masque ne contient aucun pixel de premier plan (masque vide). Lorsque `erode_radius` est à 0, aucune érosion n’est appliquée. Le recadrage carré est centré sur la boîte englobante du matte alpha du masque et dimensionné à 1,2 fois la plus grande dimension de la boîte englobante ; toute zone en dehors des limites de l’image est remplie de noir.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L’image ou les images prétraitées, recadrées en un carré centré sur fond noir avec remplissage, à la résolution `size` demandée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatPreprocessImage/fr.md)

---
**Source fingerprint (SHA-256):** `ec66941846398ee6637576b11ae9d2f9576f6b05ed2ef730cdbf99a68fe9b838`
