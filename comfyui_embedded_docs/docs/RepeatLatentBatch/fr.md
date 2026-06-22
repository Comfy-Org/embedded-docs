# Répéter Lot Latent

Le nœud RepeatLatentBatch est conçu pour répliquer un lot donné de représentations latentes un nombre spécifié de fois, en incluant potentiellement des données supplémentaires comme des masques de bruit et des indices de lot. Cette fonctionnalité est cruciale pour les opérations nécessitant plusieurs instances des mêmes données latentes, telles que l'augmentation de données ou des tâches génératives spécifiques.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `échantillons` | Le paramètre 'samples' représente les représentations latentes à répliquer. Il est essentiel pour définir les données qui seront soumises à la répétition. | `LATENT` |
| `quantité` | Le paramètre 'amount' spécifie le nombre de fois que les échantillons d'entrée doivent être répétés. Il influence directement la taille du lot de sortie, affectant ainsi la charge de calcul et la diversité des données générées. | `INT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `latent` | La sortie est une version modifiée des représentations latentes d'entrée, répliquées selon le 'amount' spécifié. Elle peut inclure des masques de bruit répliqués et des indices de lot ajustés, le cas échéant. | `LATENT` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RepeatLatentBatch/fr.md)
