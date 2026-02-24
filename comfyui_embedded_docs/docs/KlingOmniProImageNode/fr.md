> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageNode/fr.md)

Le nœud Kling Omni Image (Pro) génère ou modifie des images en utilisant le modèle Kling AI. Il crée des images à partir d'une description textuelle et permet de fournir des images de référence pour guider le style ou le contenu. Le nœud envoie une requête à une API externe, qui traite la tâche et renvoie l'image finale.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
| :--- | :--- | :--- | :--- | :--- |
| `model_name` | COMBO | Oui | `"kling-image-o1"` | Le modèle Kling AI spécifique à utiliser pour la génération d'image. |
| `prompt` | STRING | Oui | - | Une description textuelle du contenu de l'image. Elle peut inclure à la fois des descriptions positives et négatives. Le texte doit compter entre 1 et 2500 caractères. |
| `resolution` | COMBO | Oui | `"1K"`<br>`"2K"` | La résolution cible pour l'image générée. |
| `aspect_ratio` | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"21:9"` | Le rapport d'aspect (largeur sur hauteur) souhaité pour l'image générée. |
| `reference_images` | IMAGE | Non | - | Jusqu'à 10 images de référence supplémentaires. Chaque image doit mesurer au moins 300 pixels en largeur et en hauteur, et son rapport d'aspect doit être compris entre 1:2,5 et 2,5:1. |

## Sorties

| Nom de sortie | Type de données | Description |
| :--- | :--- | :--- |
| `image` | IMAGE | L'image finale générée ou modifiée par le modèle Kling AI. |
