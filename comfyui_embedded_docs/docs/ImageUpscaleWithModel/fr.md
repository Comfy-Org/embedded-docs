> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageUpscaleWithModel/fr.md)

Ce nœud est conçu pour le suréchantillonnage d'images à l'aide d'un modèle de suréchantillonnage spécifié. Il gère efficacement le processus de suréchantillonnage en adaptant l'image au périphérique approprié, en optimisant l'utilisation de la mémoire et en appliquant le modèle de suréchantillonnage par tuiles pour éviter d'éventuelles erreurs de dépassement de mémoire.

## Entrées

| Paramètre        | Type Comfy       | Description                                                                 |
|------------------|------------------|-----------------------------------------------------------------------------|
| `upscale_model`  | `UPSCALE_MODEL`  | Le modèle de suréchantillonnage à utiliser pour agrandir l'image. Il est essentiel pour définir l'algorithme de suréchantillonnage et ses paramètres. |
| `image`          | `IMAGE`          | L'image à suréchantillonner. Cette entrée est indispensable pour déterminer le contenu source qui subira le processus de suréchantillonnage. |

## Sorties

| Paramètre | Type de données | Description                                        |
|-----------|-----------------|----------------------------------------------------|
| `image`   | `IMAGE`         | L'image suréchantillonnée, traitée par le modèle de suréchantillonnage. Cette sortie est le résultat de l'opération de suréchantillonnage, mettant en évidence l'amélioration de la résolution ou de la qualité. |