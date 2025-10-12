> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayTextToImageNode/fr.md)

Le nœud Runway Text to Image génère des images à partir de prompts texte en utilisant le modèle Gen 4 de Runway. Vous pouvez fournir une description textuelle et optionnellement inclure une image de référence pour guider le processus de génération d'image. Le nœud gère la communication API et renvoie l'image générée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Prompt texte pour la génération (par défaut : "") |
| `ratio` | COMBO | Oui | "16:9"<br>"1:1"<br>"21:9"<br>"2:3"<br>"3:2"<br>"4:5"<br>"5:4"<br>"9:16"<br>"9:21" | Ratio d'aspect pour l'image générée |
| `reference_image` | IMAGE | Non | - | Image de référence optionnelle pour guider la génération |

**Remarque :** L'image de référence doit avoir des dimensions ne dépassant pas 7999x7999 pixels et un ratio d'aspect compris entre 0,5 et 2,0. Lorsqu'une image de référence est fournie, elle guide le processus de génération d'image.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | IMAGE | L'image générée basée sur le prompt texte et l'image de référence optionnelle |
