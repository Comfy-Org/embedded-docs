
Ce nœud est conçu pour traiter les informations de conditionnement de manière groupée, spécifiquement adapté au modèle StableZero123. Il se concentre sur la gestion efficace de plusieurs ensembles de données de conditionnement simultanément, optimisant le flux de travail pour les scénarios où le traitement par lots est crucial.

## Entrées

| Paramètre             | Data Type | Description |
|----------------------|--------------|-------------|
| `clip_vision`         | `CLIP_VISION` | Les embeddings de vision CLIP qui fournissent un contexte visuel pour le processus de conditionnement. |
| `init_image`          | `IMAGE`      | L'image initiale à conditionner, servant de point de départ pour le processus de génération. |
| `vae`                 | `VAE`        | L'autoencodeur variationnel utilisé pour encoder et décoder les images dans le processus de conditionnement. |
| `width`               | `INT`        | La largeur de l'image de sortie. |
| `height`              | `INT`        | La hauteur de l'image de sortie. |
| `batch_size`          | `INT`        | Le nombre d'ensembles de conditionnement à traiter dans un seul lot. |
| `elevation`           | `FLOAT`      | L'angle d'élévation pour le conditionnement du modèle 3D, affectant la perspective de l'image générée. |
| `azimuth`             | `FLOAT`      | L'angle d'azimut pour le conditionnement du modèle 3D, affectant l'orientation de l'image générée. |
| `elevation_batch_increment` | `FLOAT` | Le changement incrémental de l'angle d'élévation à travers le lot, permettant des perspectives variées. |
| `azimuth_batch_increment` | `FLOAT` | Le changement incrémental de l'angle d'azimut à travers le lot, permettant des orientations variées. |

## Sorties

| Paramètre     | Type de Donnée | Description |
|---------------|--------------|-------------|
| `positive`    | `CONDITIONING` | La sortie de conditionnement positive, adaptée pour promouvoir certaines caractéristiques ou aspects dans le contenu généré. |
| `negative`    | `CONDITIONING` | La sortie de conditionnement négative, adaptée pour réduire certaines caractéristiques ou aspects dans le contenu généré. |
| `latent`      | `LATENT`     | La représentation latente dérivée du processus de conditionnement, prête pour des étapes de traitement ou de génération ultérieures. |
