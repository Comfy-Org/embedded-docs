# MiniMax H3 Image vers Vidéo

Ce nœud prépare le conditionnement et le latent vide nécessaires pour générer une vidéo avec le modèle MiniMax H3. Il prend un prompt texte et, éventuellement, des images pour la première et/ou la dernière image de la vidéo, puis les convertit en entrées de modèle. Les images clés sont redimensionnées, encodées et attachées au conditionnement au début et à la fin de la vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip` | Modèle CLIP utilisé pour tokeniser le prompt et encoder les images clés dans le conditionnement. | CLIP | Oui |  |
| `vae` | Modèle VAE utilisé pour encoder les images clés dans l'espace latent lorsque des images clés sont fournies. | VAE | Oui |  |
| `prompt` | Prompt texte décrivant la vidéo à générer. Prend en charge plusieurs lignes et les prompts dynamiques. | STRING | Oui |  |
| `width` | Largeur de la vidéo en pixels (par défaut : 1344). | INT | Oui | 32 à MAX_RESOLUTION (pas 32) |
| `height` | Hauteur de la vidéo en pixels (par défaut : 768). | INT | Oui | 32 à MAX_RESOLUTION (pas 32) |
| `length` | Nombre de trames à 24 fps, arrondi au supérieur sur la grille 17k+5 du modèle (124 = ~5 s ; plage d'entraînement ~124-362, au-delà non testé) (par défaut : 124). | INT | Oui | 5 à 3600 (pas 17) |
| `first_frame` | Image facultative utilisée comme première image de la vidéo. Elle est étirée à la taille totale du canevas, donc son rapport d'aspect n'est pas préservé. Seule la première image du lot d'entrée est utilisée. | IMAGE | Non |  |
| `last_frame` | Image facultative utilisée comme dernière image de la vidéo. Elle est recadrée pour couvrir le canevas tout en préservant son rapport d'aspect. Seule la première image du lot d'entrée est utilisée. | IMAGE | Non |  |

Lorsque `first_frame` et/ou `last_frame` sont fournis, les images clés sont encodées avec le VAE et attachées au conditionnement respectivement à la trame 0 et à la trame finale. Lorsque aucun des deux n'est fourni, le nœud fonctionne uniquement à partir du prompt. La `length` demandée est arrondie au supérieur au nombre de trames valide le plus proche (17k + 5), de sorte que le nombre effectif de trames peut être légèrement supérieur à celui demandé.

Le latent audio-vidéo est créé sous forme de paire vide correspondant à la `width`, à la `height` et au nombre de trames arrondi demandés. La partie audio est dimensionnée à partir du même nombre de trames, à 40 trames audio par seconde.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Conditionnement contenant le prompt encodé et, lorsque des images clés sont fournies, les images clés encodées et le nombre de trames pour le modèle MiniMax H3. | CONDITIONING |
| `latent` | Latent audio-vidéo vide représentant le contenu à générer, avec la largeur, la hauteur et le nombre de trames demandés. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `d1bdf3f8c66ef20ff11c35203d2c266a88dcf8cc00c65dbb0aea2b1dd16befd6`
