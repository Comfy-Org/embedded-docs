> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEdit/fr.md)

Le nœud TextEncodeQwenImageEdit traite les invites textuelles et les images optionnelles pour générer des données de conditionnement pour la génération ou l'édition d'images. Il utilise un modèle CLIP pour tokeniser l'entrée et peut optionnellement encoder des images de référence à l'aide d'un VAE pour créer des latents de référence. Lorsqu'une image est fournie, il redimensionne automatiquement l'image pour maintenir des dimensions de traitement cohérentes.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Oui | - | Le modèle CLIP utilisé pour la tokenisation du texte et de l'image |
| `prompt` | STRING | Oui | - | Invite textuelle pour la génération du conditionnement, prend en charge l'entrée multiligne et les invites dynamiques |
| `vae` | VAE | Non | - | Modèle VAE optionnel pour encoder les images de référence en latents |
| `image` | IMAGE | Non | - | Image d'entrée optionnelle à des fins de référence ou d'édition |

**Note :** Lorsque `image` et `vae` sont tous deux fournis, le nœud encode l'image en latents de référence et les attache à la sortie de conditionnement. L'image est automatiquement redimensionnée pour maintenir une échelle de traitement cohérente d'environ 1024x1024 pixels.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Données de conditionnement contenant les tokens textuels et les latents de référence optionnels pour la génération d'images |
