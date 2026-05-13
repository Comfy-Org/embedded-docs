> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HypernetworkLoader/fr.md)

Ce nœud détecte les modèles situés dans le dossier `ComfyUI/models/hypernetworks`, et lit également les modèles depuis les chemins supplémentaires configurés dans le fichier extra_model_paths.yaml. Il peut parfois être nécessaire d'**actualiser l'interface ComfyUI** pour lui permettre de lire les fichiers de modèles depuis le dossier correspondant.

Le nœud HypernetworkLoader est conçu pour améliorer ou modifier les capacités d'un modèle donné en appliquant un hypernetwork. Il charge un hypernetwork spécifié et l'applique au modèle, ce qui peut altérer son comportement ou ses performances en fonction du paramètre de force. Ce processus permet des ajustements dynamiques de l'architecture ou des paramètres du modèle, offrant ainsi des systèmes d'IA plus flexibles et adaptatifs.

## Entrées

| Champ                | Type Comfy        | Description                                                                                  |
|----------------------|-------------------|----------------------------------------------------------------------------------------------|
| `modèle`              | `MODEL`           | Le modèle de base auquel l'hypernetwork sera appliqué, déterminant l'architecture à améliorer ou modifier. |
| `nom_hypernetwork`  | `COMBO[STRING]`   | Le nom de l'hypernetwork à charger et à appliquer au modèle, influençant le comportement ou les performances modifiés du modèle. |
| `force`           | `FLOAT`           | Un scalaire ajustant l'intensité de l'effet de l'hypernetwork sur le modèle, permettant un réglage fin des modifications. |

## Sorties

| Champ    | Type de données | Description                                                              |
|----------|-----------------|--------------------------------------------------------------------------|
| `modèle`  | `MODEL`         | Le modèle modifié après application de l'hypernetwork, illustrant l'impact de l'hypernetwork sur le modèle d'origine. |