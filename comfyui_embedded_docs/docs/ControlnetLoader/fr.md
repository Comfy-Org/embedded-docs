# Charger le modèle ControlNet

Ce nœud détecte les modèles situés dans le dossier `ComfyUI/models/controlnet`, et lit également les modèles provenant de chemins supplémentaires configurés dans le fichier extra_model_paths.yaml. Il peut parfois être nécessaire d'**actualiser l'interface ComfyUI** pour lui permettre de lire les fichiers de modèles depuis le dossier correspondant.

Le nœud ControlNetLoader est conçu pour charger un modèle ControlNet à partir d'un chemin spécifié. Il joue un rôle crucial dans l'initialisation des modèles ControlNet, essentiels pour appliquer des mécanismes de contrôle sur le contenu généré ou pour modifier du contenu existant en fonction de signaux de contrôle.

## Entrées

| Champ | Description | Type Comfy |
| --- | --- | --- |
| `control_net_name` | Spécifie le nom du modèle ControlNet à charger, utilisé pour localiser le fichier du modèle dans une structure de répertoires prédéfinie. | `COMBO[STRING]` |

## Sorties

| Champ | Description | Type Comfy |
| --- | --- | --- |
| `control_net` | Renvoie le modèle ControlNet chargé, prêt à être utilisé pour contrôler ou modifier les processus de génération de contenu. | `CONTROL_NET` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetLoader/fr.md)
