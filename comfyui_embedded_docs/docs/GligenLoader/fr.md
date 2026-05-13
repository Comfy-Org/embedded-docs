> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLIGENLoader/fr.md)

Ce nœud détecte les modèles situés dans le dossier `ComfyUI/models/gligen`, et il lit également les modèles depuis des chemins supplémentaires configurés dans le fichier extra_model_paths.yaml. Il peut être nécessaire de **rafraîchir l'interface ComfyUI** pour lui permettre de lire les fichiers de modèles depuis le dossier correspondant.

Le nœud `GLIGENLoader` est conçu pour charger des modèles GLIGEN, qui sont des modèles génératifs spécialisés. Il facilite le processus de récupération et d'initialisation de ces modèles à partir de chemins spécifiés, les rendant prêts pour d'autres tâches génératives.

## Entrées

| Champ          | Type Comfy        | Description                                                                                     |
|----------------|-------------------|-------------------------------------------------------------------------------------------------|
| `nom_gligen`  | `COMBO[STRING]`   | Le nom du modèle GLIGEN à charger, spécifiant quel fichier de modèle récupérer et charger, essentiel pour l'initialisation du modèle GLIGEN. |

## Sorties

| Champ     | Type de données | Description                                                                                     |
|-----------|-----------------|-------------------------------------------------------------------------------------------------|
| `gligen`  | `GLIGEN`        | Le modèle GLIGEN chargé, prêt à être utilisé dans des tâches génératives, représentant le modèle entièrement initialisé chargé depuis le chemin spécifié. |