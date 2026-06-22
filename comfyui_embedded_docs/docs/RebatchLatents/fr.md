# Rebatch Latents

Le nœud RebatchLatents est conçu pour réorganiser un lot de représentations latentes en une nouvelle configuration de lot, basée sur une taille de lot spécifiée. Il garantit que les échantillons latents sont regroupés de manière appropriée, en gérant les variations de dimensions et de tailles, afin de faciliter le traitement ultérieur ou l'inférence du modèle.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `latents` | Le paramètre 'latents' représente les représentations latentes d'entrée à regrouper. Il est essentiel pour déterminer la structure et le contenu du lot de sortie. | `LATENT` |
| `taille_de_lot` | Le paramètre 'batch_size' spécifie le nombre souhaité d'échantillons par lot dans la sortie. Il influence directement le regroupement et la division des latents d'entrée en nouveaux lots. | `INT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `latent` | La sortie est un lot réorganisé de représentations latentes, ajusté en fonction de la taille de lot spécifiée. Elle facilite le traitement ou l'analyse ultérieure. | `LATENT` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RebatchLatents/fr.md)
