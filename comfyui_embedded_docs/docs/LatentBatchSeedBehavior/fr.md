Le nœud LatentBatchSeedBehavior est conçu pour modifier le comportement de la graine (seed) d'un lot d'échantillons latents. Il permet soit de randomiser, soit de fixer la graine sur l'ensemble du lot, influençant ainsi le processus de génération en introduisant de la variabilité ou en maintenant une cohérence dans les résultats générés.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `échantillons` | Le paramètre 'samples' représente le lot d'échantillons latents à traiter. Sa modification dépend du comportement de la graine choisi, affectant la cohérence ou la variabilité des résultats générés. | `LATENT` |
| `comportement_de_graine` | Le paramètre 'seed_behavior' détermine si la graine du lot d'échantillons latents doit être randomisée ou fixée. Ce choix impacte significativement le processus de génération en introduisant de la variabilité ou en assurant une cohérence sur l'ensemble du lot. | COMBO[STRING] |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `latent` | La sortie est une version modifiée des échantillons latents d'entrée, avec des ajustements effectués en fonction du comportement de la graine spécifié. Elle conserve ou modifie l'index du lot pour refléter le comportement de la graine choisi. | `LATENT` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatchSeedBehavior/fr.md)
