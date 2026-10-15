# Set Reference Multi Latent

Ce nœud encode une ou plusieurs images de référence et ajoute leurs latents au conditionnement consommé par un modèle d’édition. Il s’agit de la contrepartie multi-image de Set Reference Latent : vous connectez un VAE ainsi qu’un ensemble d’images de référence, et le nœud attache chaque latent encodé au conditionnement positif et, lorsqu’un conditionnement négatif est connecté, à ce dernier également. Utilisez-le lorsqu’un modèle attend plusieurs images de référence à la fois plutôt qu’un seul latent.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Le conditionnement positif à modifier avec les latents de référence. | CONDITIONING | Oui | - |
| `negative` | Conditionnement négatif facultatif qui reçoit les mêmes latents de référence. Laissez-le non connecté pour réutiliser le conditionnement positif modifié sur la sortie `negative`. | CONDITIONING | Non | - |
| `vae` | Le VAE utilisé pour encoder les images de référence connectées. Lorsqu’aucun VAE n’est connecté, les images de référence sont ignorées. | VAE | Non | - |
| `resolution` | Comment chaque image de référence est préparée avant l’encodage. `"keep resolution"` l’encode à sa taille d’entrée ; `"resize"` la redimensionne vers un nombre cible de mégapixels tout en préservant le rapport d’aspect, ce qui fait apparaître `megapixels`. (par défaut : "keep resolution") | DYNAMIC_COMBO | Oui | `"keep resolution"`<br>`"resize"` |
| `images` | Emplacement extensible : connectez une ou plusieurs images de référence (`image_1`, `image_2`, ...) à utiliser comme références. Les images sont encodées dans l’ordre des emplacements et ajoutées au conditionnement dans cet ordre. | IMAGE | Non | 1 à 100 |

### Entrées de redimensionnement

Ces options apparaissent lorsque `resolution` est défini sur `"resize"`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `megapixels` | Taille cible de chaque image de référence, en préservant le rapport d’aspect. 1.0 correspond à environ 1024 x 1024 pixels. (par défaut : 1.0) | FLOAT | Oui | 0.01 à 16.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Le conditionnement positif avec les latents de référence encodés ajoutés. | CONDITIONING |
| `negative` | Le conditionnement négatif avec les mêmes latents de référence ajoutés. Renvoie la sortie positive lorsqu’aucun conditionnement négatif n’est connecté. | CONDITIONING |
| `empty_latent` | Le premier latent de référence multiplié par 0.0, prêt à amorcer un sampler. Vide lorsqu’aucune image de référence n’est connectée. | LATENT |

## Remarques

- Les latents sont ajoutés plutôt que remplacés ; enchaîner plusieurs nœuds Set Reference Multi Latent accumule donc les références.
- Chaque image connectée est encodée séparément ; les images de référence n’ont donc pas besoin d’avoir la même taille.
- Sans aucune image connectée, `positive` et `negative` sont renvoyés inchangés et `empty_latent` est vide.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceMultiLatent/fr.md)

---
**Source fingerprint (SHA-256):** `06f98e7c21e8750a2bdf365cb80fac990bcf01246f183c60ef83bd195fc1225b`
