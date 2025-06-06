Le nœud CLIPVisionEncode est conçu pour encoder des images à l'aide d'un modèle de vision CLIP, transformant l'entrée visuelle en un format adapté à un traitement ou une analyse ultérieure. Ce nœud simplifie la complexité de l'encodage d'images, offrant une interface simplifiée pour convertir les images en représentations encodées.
## Types d'entrée

| Paramètre            | Comfy dtype          | Description |
|----------------------|-----------------------|-------------|
| `clip_vision`        | `CLIP_VISION`        | Le modèle de vision CLIP utilisé pour encoder l'image. Il est crucial pour le processus d'encodage, car il détermine la méthode et la qualité de l'encodage. |
| `image`              | `IMAGE`              | L'image à encoder. Cette entrée est essentielle pour générer la représentation encodée du contenu visuel. |

## Types de sortie

| Paramètre             | Comfy dtype            | Description |
|-----------------------|------------------------|-------------|
| `clip_vision_output`  | `CLIP_VISION_OUTPUT`  | La représentation encodée de l'image d'entrée, produite par le modèle de vision CLIP. Cette sortie est adaptée à un traitement ou une analyse ultérieure. |