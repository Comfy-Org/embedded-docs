# MiniMax H3 Image vers Vidéo

MiniMax H3 Image to Video prépare le conditionnement et le latent vide nécessaires pour générer une vidéo avec le modèle MiniMax H3. Il prend une invite textuelle et, éventuellement, des images pour la première et/ou la dernière image de la vidéo, et les convertit en entrées du modèle. Les images clés sont redimensionnées, encodées et attachées au conditionnement au début et à la fin de la vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip` | Modèle CLIP utilisé pour tokeniser l'invite et encoder les images clés en conditionnement. | CLIP | Oui |  |
| `vae` | Modèle VAE utilisé pour encoder les images clés dans l'espace latent lorsque des images clés sont fournies. | VAE | Oui |  |
| `prompt` | Invite textuelle décrivant la vidéo à générer. Prend en charge plusieurs lignes et les invites dynamiques. | STRING | Oui |  |
| `width` | Largeur de la vidéo en pixels (défaut : 1344). | INT | Oui | 32 to MAX_RESOLUTION (step 32) |
| `height` | Hauteur de la vidéo en pixels (défaut : 768). | INT | Oui | 32 to MAX_RESOLUTION (step 32) |
| `length` | Nombre d'images à 24 fps, arrondi à la grille 17k+5 du modèle (124 = ~5 s ; la plage entraînée est ~124-362, plus long n'est pas testé) (défaut : 124). | INT | Oui | 5 to 3600 (step 17) |
| `first_frame` | Image facultative utilisée comme première image de la vidéo. Elle est étirée à la taille complète du canevas, donc son rapport hauteur/largeur n'est pas préservé. Seule la première image du lot d'entrée est utilisée. | IMAGE | Non |  |
| `last_frame` | Image facultative utilisée comme dernière image de la vidéo. Elle est recadrée pour couvrir le canevas tout en préservant son rapport hauteur/largeur. Seule la première image du lot d'entrée est utilisée. | IMAGE | Non |  |

Lorsque `first_frame` et/ou `last_frame` sont fournis, les images clés sont encodées avec le VAE et attachées au conditionnement à l'image 0 et à l'image finale, respectivement. Lorsqu'aucun n'est fourni, le nœud fonctionne à partir de la seule invite.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Conditionnement contenant l'invite encodée et, lorsque des images clés sont fournies, les images clés encodées positionnées aux première et dernière images de la vidéo pour le modèle MiniMax H3. | CONDITIONING |
| `latent` | Latent vide représentant la vidéo et sa piste audio associée à générer, avec la largeur, la hauteur et le nombre d'images demandés. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `d1bdf3f8c66ef20ff11c35203d2c266a88dcf8cc00c65dbb0aea2b1dd16befd6`
