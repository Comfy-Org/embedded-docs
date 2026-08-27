# Trellis2TextureStage

Ce nœud configure l’étape d’échantillonnage de la passe de texture pour la génération Trellis2. Il lit la disposition des coordonnées et le latent de forme par voxel depuis le latent de forme entrant, construit un latent épars vide de 32 canaux avec la même disposition des coordonnées, et attache les métadonnées requises pour l’étape de texture au conditionnement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `positive` | Le conditionnement positif utilisé pour la passe de génération de texture. Les métadonnées de l’étape de texture y sont attachées. | CONDITIONING | Oui | - |
| `negative` | Le conditionnement négatif utilisé pour la passe de génération de texture. Les métadonnées de l’étape de texture y sont attachées. | CONDITIONING | Oui | - |
| `shape_latent` | Le dictionnaire latent produit par Trellis2ShapeStage ou Trellis2UpsampleStage. Il doit contenir `coords` (la disposition des coordonnées, forme [N, 4]) et `samples` (le latent de forme par voxel) ; `coord_resolution` et `model_frame` sont facultatifs. | LATENT | Oui | - |

Remarques :
- `shape_latent` doit être la sortie de Trellis2ShapeStage ou Trellis2UpsampleStage ; il fournit la disposition des coordonnées et le latent de forme par voxel utilisés par la passe de texture.
- La disposition des coordonnées est validée : les identifiants de lot dans la première colonne de `coords` doivent être non négatifs et contigus, et le nombre total de lignes doit correspondre aux nombres de coordonnées.
- Lorsque `positive` contient un pack de caractéristiques de projection (conditionnement Pixal3D) et que `shape_latent` inclut `coord_resolution`, les caractéristiques de projection en résolution de texture 1024 sont calculées et attachées au conditionnement.
- Le repère du modèle est lu depuis `shape_latent` ; en son absence, il est défini par défaut sur `"y_up"` si des caractéristiques de projection sont présentes, et sur `"z_up"` sinon.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Le conditionnement positif avec les métadonnées de l’étape de texture attachées (mode de génération, coordonnées, nombres de coordonnées, latent de forme, repère du modèle et caractéristiques de projection le cas échéant). | CONDITIONING |
| `negative` | Le conditionnement négatif avec les mêmes métadonnées de l’étape de texture attachées. | CONDITIONING |
| `latent` | Un nouveau latent épars vide de 32 canaux avec la même disposition des coordonnées que le latent de forme entrant. Son dictionnaire inclut `samples`, `type` (`"trellis2"`), `coords`, `coord_counts` et `model_frame` ; `coord_resolution` est inclus lorsqu’il est disponible. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2TextureStage/fr.md)

---
**Source fingerprint (SHA-256):** `ae612021af7c74cd09206d905e7b800fa48367a22daf9b0335b444c854a78b1e`
