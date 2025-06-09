
Le nœud RebatchLatents est conçu pour réorganiser un lot de représentations latentes en une nouvelle configuration de lot, basée sur une taille de lot spécifiée. Il garantit que les échantillons latents sont regroupés de manière appropriée, en gérant les variations de dimensions et de tailles, pour faciliter un traitement ultérieur ou une inférence du modèle.

## Entrées

| Paramètre    | Data Type | Description |
|--------------|-------------|-------------|
| `latents`    | `LATENT`    | Le paramètre 'latents' représente les représentations latentes d'entrée à réorganiser. Il est crucial pour déterminer la structure et le contenu du lot de sortie. |
| `batch_size` | `INT`       | Le paramètre 'batch_size' spécifie le nombre souhaité d'échantillons par lot dans la sortie. Il influence directement le regroupement et la division des latents d'entrée en nouveaux lots. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La sortie est un lot réorganisé de représentations latentes, ajusté selon la taille de lot spécifiée. Il facilite un traitement ou une analyse ultérieure. |
