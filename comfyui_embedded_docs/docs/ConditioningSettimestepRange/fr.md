# ConditionnementDéfinirPlagePasDeTemps

Ce nœud est conçu pour ajuster l'aspect temporel du conditionnement en définissant une plage spécifique d'étapes temporelles. Il permet un contrôle précis des points de début et de fin du processus de conditionnement, permettant une génération plus ciblée et plus efficace.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | L'entrée de conditionnement représente l'état actuel du processus de génération, que ce nœud modifie en définissant une plage spécifique d'étapes temporelles. | CONDITIONING |
| `début` | Le paramètre de début spécifie le début de la plage d'étapes temporelles en pourcentage du processus de génération total, permettant un contrôle fin du moment où les effets de conditionnement commencent. | `FLOAT` |
| `fin` | Le paramètre de fin définit le point final de la plage d'étapes temporelles en pourcentage, permettant un contrôle précis de la durée et de la conclusion des effets de conditionnement. | `FLOAT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | La sortie est le conditionnement modifié avec la plage d'étapes temporelles spécifiée appliquée, prêt pour un traitement ou une génération ultérieure. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetTimestepRange/fr.md)
