
Le nœud RepeatLatentBatch est conçu pour répliquer un lot donné de représentations latentes un nombre spécifié de fois, incluant potentiellement des données supplémentaires comme des masques de bruit et des indices de lot. Cette fonctionnalité est cruciale pour les opérations nécessitant plusieurs instances des mêmes données latentes, telles que l'augmentation de données ou des tâches génératives spécifiques.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | Le paramètre 'samples' représente les représentations latentes à répliquer. Il est essentiel pour définir les données qui subiront la répétition. |
| `amount`  | `INT`       | Le paramètre 'amount' spécifie le nombre de fois que les échantillons d'entrée doivent être répétés. Il influence directement la taille du lot de sortie, affectant ainsi la charge computationnelle et la diversité des données générées. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La sortie est une version modifiée des représentations latentes d'entrée, répliquées selon le 'amount' spécifié. Elle peut inclure des masques de bruit répliqués et des indices de lot ajustés, si applicable. |
