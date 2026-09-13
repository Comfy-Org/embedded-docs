# Pixal3DConditioning

Le nœud Pixal3DConditioning prépare le conditionnement d’image pour le pipeline de génération 3D Trellis2. Il utilise un modèle de vision DINOv3 pour extraire les caractéristiques visuelles de l’image d’entrée à deux résolutions (512 et 1024), puis les organise en cartes de caractéristiques par étape qui peuvent être éventuellement améliorées par un modèle NAF. Les informations de caméra sont dérivées du champ de vision horizontal pour construire la matrice de transformation de projection, et le nœud produit une paire de conditionnement positive (caractéristiques issues de l’image plus données de projection) et une paire de conditionnement négative (tenseurs de caractéristiques mis à zéro) pour le guidage sans classifieur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision. | CLIP_VISION | Oui | — |
| `image` | Image prétraitée issue de ImageCropToMask (pad_factor=1.1 pour Pixal3D). | IMAGE | Oui | — |
| `camera_angle_x` | Champ de vision horizontal (FOV) en degrés (affiché comme `fov`). Connectez un MoGeGeometryToFOV (axis='horizontal', unit='degrees') pour un FOV par image (correspond à la valeur par défaut d'origine). Valeur par défaut : 49.13. | FLOAT | Oui | 1.0 – 170.0 (pas 0.01) |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | La sortie de conditionnement positive contenant les cartes de caractéristiques issues de l’image et les données de projection pour la génération Trellis2. | CONDITIONING |
| `negative` | La sortie de conditionnement négative avec des tenseurs de caractéristiques mis à zéro, utilisée pour le guidage sans classifieur. | CONDITIONING |

Remarque : La valeur `camera_angle_x` est convertie des degrés en radians en interne, et la distance de caméra est calculée à partir de celle-ci pour construire la matrice de transformation de projection. Lorsque le modèle de vision fourni inclut un composant NAF, le nœud produit également des cartes de caractéristiques haute résolution pour les étapes de forme et de texture.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `88e82b48fbe297c8e32ddd1b6659f196bda6f77fd53480bc021e85170d1923c7`
