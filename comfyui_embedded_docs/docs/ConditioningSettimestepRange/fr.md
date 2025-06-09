Ce nœud est conçu pour ajuster l'aspect temporel du conditionnement en définissant une plage spécifique de pas de temps. Il permet un contrôle précis sur les points de début et de fin du processus de conditionnement, permettant une génération plus ciblée et efficace.

## Entrées

| Paramètre | Type de Donnée | Description |
| --- | --- | --- |
| `CONDITIONING` | CONDITIONING | L'entrée de conditionnement représente l'état actuel du processus de génération, que ce nœud modifie en définissant une plage spécifique de pas de temps. |
| `start` | `FLOAT` | Le paramètre de début spécifie le commencement de la plage de pas de temps en pourcentage du processus de génération total, permettant un contrôle précis du moment où les effets de conditionnement commencent. |
| `end` | `FLOAT` | Le paramètre de fin définit le point final de la plage de pas de temps en pourcentage, permettant un contrôle précis de la durée et de la conclusion des effets de conditionnement. |

## Sorties

| Paramètre | Type de Donnée | Description |
| --- | --- | --- |
| `CONDITIONING` | CONDITIONING | La sortie est le conditionnement modifié avec la plage de pas de temps spécifiée appliquée, prêt pour un traitement ou une génération ultérieure. |
