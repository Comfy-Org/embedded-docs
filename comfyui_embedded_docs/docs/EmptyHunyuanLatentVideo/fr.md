> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanLatentVideo/fr.md)

Le nœud `EmptyHunyuanLatentVideo` est similaire au nœud `EmptyLatentImage`. Vous pouvez le considérer comme une toile vierge pour la génération vidéo, où la largeur, la hauteur et la longueur définissent les propriétés de la toile, et la taille du lot détermine le nombre de toiles à créer. Ce nœud crée des toiles vides prêtes pour les tâches ultérieures de génération vidéo.

## Entrées

| Paramètre     | Type Comfy | Description                                                                                |
| ------------ | ---------- | ------------------------------------------------------------------------------------------ |
| `width`      | `INT`      | Largeur de la vidéo, valeur par défaut 848, minimum 16, maximum `nodes.MAX_RESOLUTION`, pas de 16.        |
| `height`     | `INT`      | Hauteur de la vidéo, valeur par défaut 480, minimum 16, maximum `nodes.MAX_RESOLUTION`, pas de 16.       |
| `length`     | `INT`      | Longueur de la vidéo, valeur par défaut 25, minimum 1, maximum `nodes.MAX_RESOLUTION`, pas de 4.          |
| `batch_size` | `INT`      | Taille du lot, valeur par défaut 1, minimum 1, maximum 4096.                                           |

## Sorties

| Paramètre  | Type Comfy | Description                                                                               |
| ---------- | ---------- | ----------------------------------------------------------------------------------------- |
| `samples`  | `LATENT`   | Échantillons vidéo latents générés contenant des tenseurs nuls, prêts pour les tâches de traitement et de génération. |