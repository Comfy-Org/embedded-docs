# p-h3-image Conditioning

Ce nœud transforme un prompt en conditionnement et en latent vide pour une seule image fixe avec p-h3-image. Sans images, il s'agit de texte vers image ; avec des images connectées, `image_1` est l'image en cours d'édition et les autres emplacements servent de références, que le prompt désigne par `<Picture 1>`, `<Picture 2>`, etc. L'échantillonneur nécessite un modèle patché par le nœud MiniMax H3 sigma shift, avec les deux valeurs de décalage à 1.0.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP p-h3-image utilisé pour tokeniser le prompt, y compris les éventuelles images de référence, et pour encoder le conditionnement. | CLIP | Oui | - |
| `prompt` | Ce qu'il faut générer, ou comment modifier `image_1`. Lorsque des images sont connectées, une instruction courte est préfixée par `Edit <Picture 1>. `. Une instruction qui commence déjà par `Edit <Picture` ou une consigne d'édition produite par un suréchantillonneur de prompt est utilisée exactement telle qu'elle est écrite. | STRING | Oui | - |
| `width` | Largeur de sortie en pixels, arrondie à un multiple de 32. 0 utilise la largeur de `image_1` après redimensionnement, ou 2912 lorsqu'aucune image n'est connectée (par défaut : 0). | INT | Oui | 0 à MAX_RESOLUTION |
| `height` | Hauteur de sortie en pixels, arrondie à un multiple de 32. 0 utilise la hauteur de `image_1` après redimensionnement, ou 2912 lorsqu'aucune image n'est connectée (par défaut : 0). | INT | Oui | 0 à MAX_RESOLUTION |
| `vae` | Le VAE p-h3-image. Requis dès qu'un emplacement d'image est connecté, car les latents de référence sont encodés avec celui-ci. | VAE | Non | - |
| `images` | Groupe extensible de jusqu'à 9 images, de `image_1` à `image_9`. `image_1` est l'image en cours d'édition, les autres emplacements sont des références. | AUTOGROW | Non | 0 à 9 images |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement pour l'échantillonneur p-h3-image. Lorsque des images sont connectées, il transporte aussi les latents de référence empaquetés. | CONDITIONING |
| `latent` | Latent vide pour une image fixe, incluant les deux latents audio attendus par le modèle. | LATENT |

**Remarque :** Les images nécessitent l'entrée `vae`. Exécuter le nœud avec une image connectée et sans VAE déclenche une erreur.

**Remarque :** Le conditionnement couvre une seule image fixe. Pour la vidéo ou l'audio, utilisez plutôt les nœuds vidéo MiniMax H3.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PH3ImageConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `f1f5e5b2d3ff9bc2f3b81f3d0dd722e725c7930c6f95bf44ad83bc64357d2fb7`
