Ce nœud détectera les modèles situés dans le dossier `ComfyUI/models/style_models`,
et lira également les modèles des chemins supplémentaires que vous avez configurés dans le fichier extra_model_paths.yaml.
Parfois, vous devrez **rafraîchir l'interface ComfyUI** pour qu'elle puisse lire les fichiers de modèle dans le dossier correspondant.

Le nœud StyleModelLoader est conçu pour charger un modèle de style à partir d'un chemin spécifié. Il se concentre sur la récupération et l'initialisation des modèles de style qui peuvent être utilisés pour appliquer des styles artistiques spécifiques aux images, permettant ainsi la personnalisation des sorties visuelles en fonction du modèle de style chargé.

## Entrées

| Type | Nom | Description | Data Type | Python dtype |
|------|-----|-------------|-------------|--------------|
| Requis | **`style_model_name`** | Spécifie le nom du modèle de style à charger. Ce nom est utilisé pour localiser le fichier du modèle dans une structure de répertoires prédéfinie, permettant le chargement dynamique de différents modèles de style en fonction des besoins de l'utilisateur ou de l'application. | COMBO[STRING] | `str` |

## Sorties

| Nom | Description | Data Type | Python dtype |
|-----|-------------|-------------|--------------|
| **`style_model`** | Renvoie le modèle de style chargé, prêt à être utilisé pour appliquer des styles aux images. Cela permet la personnalisation dynamique des sorties visuelles en appliquant différents styles artistiques. | `STYLE_MODEL` | `StyleModel` |
