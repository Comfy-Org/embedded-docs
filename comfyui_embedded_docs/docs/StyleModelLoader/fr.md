Ce nœud détecte les modèles situés dans le dossier `ComfyUI/models/style_models`, et lit également les modèles provenant de chemins supplémentaires configurés dans le fichier extra_model_paths.yaml. Il peut parfois être nécessaire d'**actualiser l'interface ComfyUI** pour lui permettre de lire les fichiers de modèles depuis le dossier correspondant.

Le nœud StyleModelLoader est conçu pour charger un modèle de style à partir d'un chemin spécifié. Il se concentre sur la récupération et l'initialisation des modèles de style pouvant être utilisés pour appliquer des styles artistiques spécifiques aux images, permettant ainsi la personnalisation des rendus visuels en fonction du modèle de style chargé.

## Entrées

| Nom du paramètre | Description | Type Comfy | Type Python |
| --- | --- | --- | --- |
| `nom_du_modèle_de_style` | Spécifie le nom du modèle de style à charger. Ce nom est utilisé pour localiser le fichier du modèle dans une structure de répertoires prédéfinie, permettant le chargement dynamique de différents modèles de style en fonction des entrées utilisateur ou des besoins de l'application. | COMBO[STRING] | `str` |

## Sorties

| Nom du paramètre | Description | Type Comfy | Type Python |
| --- | --- | --- | --- |
| `style_model` | Renvoie le modèle de style chargé, prêt à être utilisé pour appliquer des styles aux images. Cela permet la personnalisation dynamique des rendus visuels en appliquant différents styles artistiques. | `STYLE_MODEL` | `StyleModel` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StyleModelLoader/fr.md)
