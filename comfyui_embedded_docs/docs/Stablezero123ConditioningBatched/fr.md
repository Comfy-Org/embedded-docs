# Stablezero123ConditioningBatched

Ce nœud est conçu pour traiter les informations de conditionnement par lots, spécifiquement adapté au modèle StableZero123. Il se concentre sur la gestion efficace de plusieurs ensembles de données de conditionnement simultanément, optimisant le flux de travail pour les scénarios où le traitement par lots est crucial.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `clip_vision` | Les embeddings visuels CLIP qui fournissent le contexte visuel pour le processus de conditionnement. | `CLIP_VISION` |
| `init_image` | L'image initiale à conditionner, servant de point de départ pour le processus de génération. | `IMAGE` |
| `vae` | L'autoencodeur variationnel utilisé pour encoder et décoder les images dans le processus de conditionnement. | `VAE` |
| `width` | La largeur de l'image de sortie. | `INT` |
| `height` | La hauteur de l'image de sortie. | `INT` |
| `batch_size` | Le nombre d'ensembles de conditionnement à traiter en un seul lot. | `INT` |
| `elevation` | L'angle d'élévation pour le conditionnement du modèle 3D, affectant la perspective de l'image générée. | `FLOAT` |
| `azimuth` | L'angle d'azimut pour le conditionnement du modèle 3D, affectant l'orientation de l'image générée. | `FLOAT` |
| `elevation_batch_increment` | La variation incrémentielle de l'angle d'élévation au sein du lot, permettant des perspectives variées. | `FLOAT` |
| `azimuth_batch_increment` | La variation incrémentielle de l'angle d'azimut au sein du lot, permettant des orientations variées. | `FLOAT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `positive` | La sortie de conditionnement positive, adaptée pour promouvoir certaines caractéristiques ou aspects dans le contenu généré. | `CONDITIONING` |
| `negative` | La sortie de conditionnement négative, adaptée pour défavoriser certaines caractéristiques ou aspects dans le contenu généré. | `CONDITIONING` |
| `latent` | La représentation latente dérivée du processus de conditionnement, prête pour d'autres étapes de traitement ou de génération. | `LATENT` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123ConditioningBatched/fr.md)
