> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/fr.md)

Génère des vidéos basées sur une image d'entrée et une invite textuelle. Ce nœud prend une image et crée une vidéo animée en appliquant les paramètres de mouvement et de qualité spécifiés pour transformer l'image statique en une séquence animée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | Image d'entrée à transformer en vidéo |
| `prompt` | STRING | Oui | - | Invite pour la génération de la vidéo |
| `qualité` | COMBO | Oui | `res_540p`<br>`res_1080p` | Paramètre de qualité vidéo (par défaut : res_540p) |
| `durée_secondes` | COMBO | Oui | `dur_2`<br>`dur_5`<br>`dur_10` | Durée de la vidéo générée en secondes |
| `mode_mouvement` | COMBO | Oui | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` | Style de mouvement appliqué à la génération de la vidéo |
| `graine` | INT | Oui | 0-2147483647 | Graine pour la génération de vidéo (par défaut : 0) |
| `prompt_négatif` | STRING | Non | - | Une description textuelle optionnelle des éléments indésirables sur une image |
| `modèle_pixverse` | CUSTOM | Non | - | Un modèle optionnel pour influencer le style de génération, créé par le nœud PixVerse Template |

**Note :** Lors de l'utilisation de la qualité 1080p, le mode de mouvement est automatiquement défini sur normal et la durée est limitée à 5 secondes. Pour les durées autres que 5 secondes, le mode de mouvement est également automatiquement défini sur normal.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Vidéo générée basée sur l'image d'entrée et les paramètres |
