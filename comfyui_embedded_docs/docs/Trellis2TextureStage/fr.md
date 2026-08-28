# Trellis2TextureStage

Ce nœud configure l’étape d’échantillonnage de la passe de texture pour la génération Trellis2. Il lit la structure de coordonnées et le latent de forme par voxel du latent de forme entrant, construit un latent sparse vide à 32 canaux avec la même structure de coordonnées, et attache les métadonnées requises pour l’étape de texture au conditioning.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `positif` | Le conditioning positif utilisé pour la passe de génération de texture. Les métadonnées de l’étape de texture y sont attachées. | CONDITIONING | Oui | - |
| `négatif` | Le conditioning négatif utilisé pour la passe de génération de texture. Les métadonnées de l’étape de texture y sont attachées. | CONDITIONING | Oui | - |
| `shape_latent` | Le dict latent produit par Trellis2ShapeStage ou Trellis2UpsampleStage. Il doit contenir `coords` (la structure de coordonnées, forme [N, 4]) et `samples` (le latent de forme par voxel) ; `coord_resolution` et `model_frame` sont facultatifs. | LATENT | Oui | - |

Remarques :
- `shape_latent` doit être la sortie de Trellis2ShapeStage ou Trellis2UpsampleStage ; il fournit la structure de coordonnées et le latent de forme par voxel utilisés par la passe de texture.
- La structure de coordonnées est validée : les identifiants de lot dans la première colonne de `coords` doivent être non négatifs et contigus, et le nombre total de lignes doit correspondre aux comptes de coordonnées.
- Lorsque `positive` contient un pack de caractéristiques de projection (conditionnement Pixal3D) et que `shape_latent` inclut `coord_resolution`, les caractéristiques de projection à la résolution de texture 1024 sont calculées et attachées au conditioning.
- Le cadre de modèle (model frame) est lu depuis `shape_latent` ; en son absence, il prend par défaut la valeur `"y_up"` si des caractéristiques de projection sont présentes, et `"z_up"` sinon.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positif` | Le conditioning positif avec les métadonnées de l’étape de texture attachées (mode de génération, coordonnées, comptes de coordonnées, latent de forme, cadre de modèle et caractéristiques de projection le cas échéant). | CONDITIONING |
| `négatif` | Le conditioning négatif avec les mêmes métadonnées de l’étape de texture attachées. | CONDITIONING |
| `latent` | Un nouveau latent sparse vide à 32 canaux avec la même structure de coordonnées que le latent de forme entrant. Son dict inclut `samples`, `type` (`"trellis2"`), `coords`, `coord_counts` et `model_frame` ; `coord_resolution` est inclus lorsqu’il est disponible. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2TextureStage/fr.md)

---
**Source fingerprint (SHA-256):** `ae612021af7c74cd09206d905e7b800fa48367a22daf9b0335b444c854a78b1e`
