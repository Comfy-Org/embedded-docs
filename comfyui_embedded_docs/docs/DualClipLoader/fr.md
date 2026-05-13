> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCLIPLoader/fr.md)

Le nœud DualCLIPLoader est conçu pour charger deux modèles CLIP simultanément, facilitant les opérations nécessitant l'intégration ou la comparaison des caractéristiques des deux modèles.

Ce nœud détectera les modèles situés dans le dossier `ComfyUI/models/text_encoders`.

## Entrées

| Paramètre    | Type Comfy     | Description                                                                                                                                                                                     |
| ------------ | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `nom_clip1` | COMBO[STRING] | Spécifie le nom du premier modèle CLIP à charger. Ce paramètre est essentiel pour identifier et récupérer le modèle correct à partir d'une liste prédéfinie de modèles CLIP disponibles.       |
| `nom_clip2` | COMBO[STRING] | Spécifie le nom du second modèle CLIP à charger. Ce paramètre permet de charger un deuxième modèle CLIP distinct pour une analyse comparative ou intégrative en parallèle du premier modèle.   |
| `type`       | `option`      | Choisissez parmi "sdxl", "sd3", "flux" pour vous adapter à différents modèles.                                                                                                                 |

* L'ordre de chargement n'affecte pas le résultat final

## Sorties

| Paramètre | Type de données | Description                                                                                                           |
| --------- | --------------- | --------------------------------------------------------------------------------------------------------------------- |
| `clip`    | CLIP            | La sortie est un modèle CLIP combiné qui intègre les caractéristiques ou fonctionnalités des deux modèles CLIP spécifiés. |