# MiniMax H3 Image vers Vidéo

Ce nœud prépare le conditionnement et le latent vide nécessaires pour générer une vidéo avec le modèle MiniMax H3. Il prend un prompt textuel et, optionnellement, des images pour la première et/ou la dernière frame de la vidéo, et les convertit en entrées du modèle. Les images clés sont redimensionnées, encodées et attachées au conditionnement au début et à la fin de la vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip` | Modèle CLIP utilisé pour tokeniser le prompt et encoder les images clés en conditionnement. | CLIP | Oui |  |
| `vae` | Modèle VAE utilisé pour encoder les images clés dans l’espace latent lorsque des images clés sont fournies. | VAE | Oui |  |
| `invite` | Prompt textuel décrivant la vidéo à générer. Prend en charge plusieurs lignes et les prompts dynamiques. | STRING | Oui |  |
| `largeur` | Largeur de la vidéo en pixels (défaut : 1344). | INT | Oui | 32 à MAX_RESOLUTION (pas de 32) |
| `hauteur` | Hauteur de la vidéo en pixels (défaut : 768). | INT | Oui | 32 à MAX_RESOLUTION (pas de 32) |
| `longueur` | Nombre de frames à 24 fps, ajusté à la grille 17k+5 du modèle (124 = ~5s ; la plage entraînée est ~124-362, plus long est non testé) (défaut : 124). | INT | Oui | 5 à 3600 (pas de 17) |
| `première_image` | Image optionnelle utilisée comme première frame de la vidéo. Elle est étirée à la taille du canevas complet, donc son ratio d’aspect n’est pas préservé. Seule la première image du lot d’entrée est utilisée. | IMAGE | Non |  |
| `dernière_image` | Image optionnelle utilisée comme dernière frame de la vidéo. Elle est recadrée pour couvrir le canevas tout en préservant son ratio d’aspect. Seule la première image du lot d’entrée est utilisée. | IMAGE | Non |  |

Lorsque `first_frame` et/ou `last_frame` sont fournis, les images clés sont encodées avec le VAE et attachées au conditionnement à la frame 0 et à la frame finale, respectivement. Lorsqu’aucun n’est fourni, le nœud fonctionne à partir du seul prompt.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positif` | Conditionnement contenant le prompt encodé et, lorsque des images clés sont fournies, les images clés encodées et le nombre de frames pour le modèle MiniMax H3. | CONDITIONING |
| `latent` | Latent vide représentant la vidéo à générer, avec la largeur, la hauteur et le nombre de frames demandés. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `46efc87bd46f4a86cb6df37c75f960419a2a98b34480e7dc0023c9d87903870b`
