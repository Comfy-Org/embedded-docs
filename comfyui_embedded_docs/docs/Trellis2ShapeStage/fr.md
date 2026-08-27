# Trellis2ShapeStage

Ce nœud configure la première passe d’échantillonnage de génération de forme du pipeline Trellis2. Il prend le voxel de structure dense produit par VaeDecodeStructureTrellis2, extrait les coordonnées éparses des voxels remplis, crée un latent épars vide, puis attache les métadonnées d’échantillonnage au conditionnement afin que le modèle puisse les lire pendant l’échantillonnage. Pour la seconde passe de forme après le suréchantillonnage, utilisez plutôt Trellis2UpsampleStage, qui combine la cascade et la configuration de l’étape de seconde passe.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `positive` | Le conditionnement positif à préparer pour l’étape de forme. Il peut s’agir d’un conditionnement Trellis2 standard ou d’un conditionnement Pixal3D fournissant un pack de caractéristiques de projection ; lorsque des caractéristiques de projection sont présentes, elles sont calculées pour l’étape sélectionnée et attachées au conditionnement de sortie. | CONDITIONING | Oui | Tout conditionnement Trellis2 ou Pixal3D |
| `negative` | Le conditionnement négatif à préparer pour l’étape de forme. Les mêmes métadonnées d’étape de forme y sont attachées que pour le conditionnement positif. | CONDITIONING | Oui | Tout conditionnement Trellis2 ou Pixal3D |
| `voxel` | Voxel de structure dense provenant de VaeDecodeStructureTrellis2. | VOXEL | Oui | Toute grille de voxels ; la résolution de la grille (voxels par axe) sélectionne l’étape du pipeline |

### Remarques

- La résolution de la grille de voxels sélectionne l’étape du pipeline : une résolution de 32 ou moins utilise le mode `shape_generation_512` avec l’étape `shape_512` ; une résolution supérieure à 32 utilise le mode `shape_generation` avec l’étape `shape_1024`.
- Le voxel doit contenir au moins un voxel rempli ; un voxel vide provoque une erreur. Les indices de lot dérivés du voxel doivent être non négatifs et contigus.
- Lorsque le conditionnement `positive` contient un `proj_feat_pack` (fourni par le conditionnement Pixal3D), les caractéristiques de projection sont calculées pour l’étape sélectionnée et le repère du modèle du latent de sortie est défini sur `y_up`. Sinon, aucune caractéristique de projection n’est attachée et le repère du modèle est défini sur `z_up`.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `positive` | Le conditionnement positif avec les métadonnées d’étape de forme attachées : mode de génération, coordonnées éparses, nombres de coordonnées par lot, et caractéristiques de projection lorsque le conditionnement source les fournit. | CONDITIONING |
| `negative` | Le conditionnement négatif avec les mêmes métadonnées d’étape de forme attachées. | CONDITIONING |
| `latent` | Un tenseur latent épars vide (forme : taille de lot, 32, nombre de tokens, 1) accompagné des coordonnées éparses extraites, des nombres de coordonnées par lot, de la résolution des coordonnées, du marqueur de type `trellis2`, et de l’orientation du repère du modèle. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2ShapeStage/fr.md)

---
**Source fingerprint (SHA-256):** `7dbee8a5b6ef7111f07def4dbe1cc4908533e00ffcb775f5a284099360c7eed3`
