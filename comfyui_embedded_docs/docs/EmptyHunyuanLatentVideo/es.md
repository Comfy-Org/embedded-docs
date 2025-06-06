

Le nœud `EmptyHunyuanLatentVideo` est similaire au nœud `EmptyLatent Image`.
Vous pouvez le considérer comme un canevas vierge pour la génération de vidéos, où la largeur, la hauteur et la longueur définissent les propriétés du canevas, et la taille du lot détermine le nombre de canevas à créer. Ce nœud crée des canevas vides prêts pour les tâches ultérieures de génération de vidéos.

## Types d'entrée Empty Hunyuan Latent Video

| Paramètre    | Type Comfy | Description                                                                               |
| ------------ | ---------- | ----------------------------------------------------------------------------------------- |
| `width`      | `INT`      | Largeur de la vidéo, par défaut 848, minimum 16, maximum `nodes.MAX_RESOLUTION`, pas de 16. |
| `height`     | `INT`      | Hauteur de la vidéo, par défaut 480, minimum 16, maximum `nodes.MAX_RESOLUTION`, pas de 16. |
| `length`     | `INT`      | Longueur de la vidéo, par défaut 25, minimum 1, maximum `nodes.MAX_RESOLUTION`, pas de 4. |
| `batch_size` | `INT`      | Taille du lot, par défaut 1, minimum 1, maximum 4096.                                    |

## Types de sortie Empty Hunyuan Latent Video

| Paramètre    | Type Comfy | Description                                                                              |
| ------------ | ---------- | ---------------------------------------------------------------------------------------- |
| `samples`    | `LATENT`   | Échantillons vidéo latents générés contenant des tenseurs nuls, prêts pour le traitement et la génération. |
