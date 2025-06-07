Ce nœud a été renommé en Appliquer ControlNet dans la nouvelle version de ComfyUI, remplaçant l'ancienne version nommée Appliquer ControlNet (OLD). Étant donné que l'ancien Appliquer ControlNet (OLD) est actuellement quelque peu similaire à un état activé, la documentation la plus récente pour ce nœud a été déplacée vers `Appliquer ControlNet`pour clarification.

Ce nœud applique des transformations avancées de réseau de contrôle aux données de conditionnement basées sur une image et un modèle de réseau de contrôle. Il permet des ajustements précis de l'influence du réseau de contrôle sur le contenu généré, permettant des modifications plus précises et variées du conditionnement.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `positive` | `CONDITIONING` | Les données de conditionnement positives auxquelles les transformations du réseau de contrôle seront appliquées. Elles représentent les attributs ou caractéristiques souhaités à améliorer ou maintenir dans le contenu généré. |
| `negative` | `CONDITIONING` | Les données de conditionnement négatives, représentant les attributs ou caractéristiques à diminuer ou supprimer du contenu généré. Les transformations du réseau de contrôle sont également appliquées à ces données, permettant un ajustement équilibré des caractéristiques du contenu. |
| `control_net` | `CONTROL_NET` | Le modèle de réseau de contrôle est crucial pour définir les ajustements et améliorations spécifiques aux données de conditionnement. Il interprète l'image de référence et les paramètres de force pour appliquer des transformations, influençant significativement le résultat final en modifiant les attributs dans les données de conditionnement positives et négatives. |
| `image` | `IMAGE` | L'image servant de référence pour les transformations du réseau de contrôle. Elle influence les ajustements effectués par le réseau de contrôle sur les données de conditionnement, guidant l'amélioration ou la suppression de caractéristiques spécifiques. |
| `strength` | `FLOAT` | Une valeur scalaire déterminant l'intensité de l'influence du réseau de contrôle sur les données de conditionnement. Des valeurs plus élevées entraînent des ajustements plus prononcés. |
| `start_percent` | `FLOAT` | Le pourcentage de départ de l'effet du réseau de contrôle, permettant une application progressive des transformations sur une plage spécifiée. |
| `end_percent` | `FLOAT` | Le pourcentage de fin de l'effet du réseau de contrôle, définissant la plage sur laquelle les transformations sont appliquées. Cela permet un contrôle plus nuancé du processus d'ajustement. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `positive` | `CONDITIONING` | Les données de conditionnement positives modifiées après l'application des transformations du réseau de contrôle, reflétant les améliorations effectuées en fonction des paramètres d'entrée. |
| `negative` | `CONDITIONING` | Les données de conditionnement négatives modifiées après l'application des transformations du réseau de contrôle, reflétant la suppression ou le retrait de caractéristiques spécifiques en fonction des paramètres d'entrée. |
