## Entrées

| Paramètre    | Type Comfy | Description                                                                               |
| ------------ | ---------- | ----------------------------------------------------------------------------------------- |
| `width`      | `INT`      | Largeur de la vidéo, par défaut 848, minimum 16, maximum `nodes.MAX_RESOLUTION`, pas de 16. |
| `height`     | `INT`      | Hauteur de la vidéo, par défaut 480, minimum 16, maximum `nodes.MAX_RESOLUTION`, pas de 16. |
| `length`     | `INT`      | Longueur de la vidéo, par défaut 25, minimum 1, maximum `nodes.MAX_RESOLUTION`, pas de 4. |
| `batch_size` | `INT`      | Taille du lot, par défaut 1, minimum 1, maximum 4096.                                    |

## Sorties

| Paramètre    | Type Comfy | Description                                                                              |
| ------------ | ---------- | ---------------------------------------------------------------------------------------- |
| `samples`    | `LATENT`   | Échantillons vidéo latents générés contenant des tenseurs nuls, prêts pour le traitement et la génération. |
