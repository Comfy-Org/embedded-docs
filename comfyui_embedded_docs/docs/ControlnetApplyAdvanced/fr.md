> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplyAdvanced/fr.md)

Ce nœud applique des transformations avancées de réseau de contrôle aux données de conditionnement en se basant sur une image et un modèle de réseau de contrôle. Il permet des réglages précis de l'influence du réseau de contrôle sur le contenu généré, offrant des modifications plus fines et variées du conditionnement.

## Entrées

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `positive` | `CONDITIONING` | Les données de conditionnement positives auxquelles les transformations du réseau de contrôle seront appliquées. Elles représentent les attributs ou caractéristiques souhaités à renforcer ou à conserver dans le contenu généré. |
| `negative` | `CONDITIONING` | Les données de conditionnement négatives, représentant les attributs ou caractéristiques à atténuer ou à supprimer du contenu généré. Les transformations du réseau de contrôle sont également appliquées à ces données, permettant un ajustement équilibré des caractéristiques du contenu. |
| `control_net` | `CONTROL_NET` | Le modèle de réseau de contrôle est essentiel pour définir les ajustements et améliorations spécifiques apportés aux données de conditionnement. Il interprète l'image de référence et les paramètres de force pour appliquer des transformations, influençant considérablement le résultat final en modifiant les attributs des données de conditionnement positives et négatives. |
| `image` | `IMAGE` | L'image servant de référence pour les transformations du réseau de contrôle. Elle influence les ajustements effectués par le réseau de contrôle sur les données de conditionnement, guidant le renforcement ou la suppression de caractéristiques spécifiques. |
| `strength` | `FLOAT` | Une valeur scalaire déterminant l'intensité de l'influence du réseau de contrôle sur les données de conditionnement. Des valeurs plus élevées entraînent des ajustements plus prononcés. |
| `start_percent` | `FLOAT` | Le pourcentage de début de l'effet du réseau de contrôle, permettant une application progressive des transformations sur une plage spécifiée. |
| `end_percent` | `FLOAT` | Le pourcentage de fin de l'effet du réseau de contrôle, définissant la plage sur laquelle les transformations sont appliquées. Cela permet un contrôle plus nuancé du processus d'ajustement. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `positive` | `CONDITIONING` | Les données de conditionnement positives modifiées après l'application des transformations du réseau de contrôle, reflétant les améliorations apportées en fonction des paramètres d'entrée. |
| `negative` | `CONDITIONING` | Les données de conditionnement négatives modifiées après l'application des transformations du réseau de contrôle, reflétant la suppression ou l'élimination de caractéristiques spécifiques en fonction des paramètres d'entrée. |