
Le nœud LatentBatchSeedBehavior est conçu pour modifier le comportement de la graine d'un lot d'échantillons latents. Il permet soit de randomiser, soit de fixer la graine à travers le lot, influençant ainsi le processus de génération en introduisant soit de la variabilité, soit en maintenant la cohérence dans les sorties générées.

## Entrées

| Paramètre       | Data Type | Description |
|-----------------|--------------|-------------|
| `samples`       | `LATENT`     | Le paramètre 'samples' représente le lot d'échantillons latents à traiter. Sa modification dépend du comportement de la graine choisi, affectant la cohérence ou la variabilité des sorties générées. |
| `seed_behavior`  | COMBO[STRING] | Le paramètre 'seed_behavior' détermine si la graine pour le lot d'échantillons latents doit être randomisée ou fixée. Ce choix impacte significativement le processus de génération en introduisant soit de la variabilité, soit en assurant la cohérence à travers le lot. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La sortie est une version modifiée des échantillons latents d'entrée, avec des ajustements effectués en fonction du comportement de la graine spécifié. Elle maintient ou modifie l'index du lot pour refléter le comportement de la graine choisi. |
