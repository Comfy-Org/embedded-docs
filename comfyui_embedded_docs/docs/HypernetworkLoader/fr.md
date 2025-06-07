Ce nœud détecte les modèles situés dans le dossier `ComfyUI/models/hypernetworks` et lit également les modèles des chemins supplémentaires que vous avez configurés dans le fichier extra_model_paths.yaml. Parfois, vous devrez **rafraîchir l'interface ComfyUI** pour qu'elle puisse lire les fichiers de modèle dans le dossier correspondant.

Le nœud HypernetworkLoader est conçu pour améliorer ou modifier les capacités d'un modèle donné en appliquant un hypernetwork. Il charge un hypernetwork spécifié et l'applique au modèle, modifiant potentiellement son comportement ou ses performances en fonction du paramètre de force. Ce processus permet des ajustements dynamiques de l'architecture ou des paramètres du modèle, rendant les systèmes d'IA plus flexibles et adaptatifs.

## Entrées

| Champ                 | Comfy dtype       | Description                                                                                  |
|-----------------------|-------------------|----------------------------------------------------------------------------------------------|
| `model`               | `MODEL`           | Le modèle de base auquel l'hypernetwork sera appliqué, déterminant l'architecture à améliorer ou modifier. |
| `hypernetwork_name`  | `COMBO[STRING]`   | Le nom de l'hypernetwork à charger et appliquer au modèle, influençant le comportement ou les performances modifiées du modèle. |
| `strength`            | `FLOAT`           | Un scalaire ajustant l'intensité de l'effet de l'hypernetwork sur le modèle, permettant un ajustement précis des modifications. |

## Sorties

| Champ   | Data Type | Description                                                              |
|---------|-------------|--------------------------------------------------------------------------|
| `model` | `MODEL`     | Le modèle modifié après l'application de l'hypernetwork, illustrant l'impact de l'hypernetwork sur le modèle original. |
