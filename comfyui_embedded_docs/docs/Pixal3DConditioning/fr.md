# Pixal3DConditioning

Ce nœud prépare le conditionnement d'image pour le pipeline de génération 3D Trellis2. Il extrait les caractéristiques visuelles de l'image d'entrée avec un modèle de vision DINOv3 à deux résolutions, les organise en cartes de caractéristiques par étape (éventuellement améliorées avec un modèle NAF), et les combine avec les données de caméra dérivées du champ de vision horizontal. Il produit une paire de conditionnement positive et négative, où la négative utilise des caractéristiques mises à zéro pour le guidage sans classifieur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision. | CLIP_VISION | Oui | — |
| `image` | Image prétraitée issue de ImageCropToMask (pad_factor=1.1 pour Pixal3D). | IMAGE | Oui | — |
| `camera_angle_x` | Champ de vision horizontal en degrés (nom affiché : fov). Connectez un nœud MoGeGeometryToFOV (axis='horizontal', unit='degrees') pour une FOV par image (correspond à la valeur par défaut en amont). Défaut : 49.13. | FLOAT | Oui | 1.0 – 170.0 |

Remarque : La valeur `camera_angle_x` est convertie en radians en interne et utilisée pour calculer la distance de la caméra pour la matrice de transformation de projection. Lorsque le modèle de vision fourni inclut un composant NAF, le nœud produit en plus des cartes de caractéristiques haute résolution pour les étapes de forme et de texture.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positif` | Conditionnement positif contenant les cartes de caractéristiques dérivées de l'image et les données de projection pour la génération Trellis2. | CONDITIONING |
| `négatif` | Conditionnement négatif avec des tenseurs de caractéristiques mis à zéro, utilisé pour le guidage sans classifieur. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `3eba711620f6c56a21bbf7df89f8d406ce6f90908298b1a295a1dbbddd042472`
