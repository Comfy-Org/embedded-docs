# Extension WanSoundImageToVideo

Le nœud WanSoundImageToVideoExtend étend un latent vidéo existant en générant des images supplémentaires, éventuellement guidé par l’audio, une image de référence et une vidéo de contrôle. Il prend un latent vidéo de départ et produit une séquence vidéo plus longue, en utilisant le conditionnement fourni et les indices audio pour influencer le nouveau contenu.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Prompts de conditionnement positifs qui guident ce que la vidéo doit contenir | CONDITIONING | Oui | - |
| `négatif` | Prompts de conditionnement négatifs qui précisent ce que la vidéo doit éviter | CONDITIONING | Oui | - |
| `vae` | Autoencodeur variationnel utilisé pour encoder l’image de référence et la vidéo de contrôle dans l’espace latent | VAE | Oui | - |
| `longueur` | Nombre total d’images à générer pour la séquence vidéo (défaut : 77, pas : 4) | INT | Oui | 1 to MAX_RESOLUTION |
| `latent vidéo` | Latent vidéo initial qui sert de point de départ à l’extension. La largeur, la hauteur, la taille de lot et le décalage d’images de la sortie sont dérivés de ce latent. Ses 19 dernières images sont utilisées comme conditionnement de mouvement de référence. | LATENT | Oui | - |
| `sortie de l'encodeur audio` | Embeddings audio optionnels qui peuvent influencer la génération vidéo en fonction des caractéristiques du son. Lorsqu’ils sont fournis, l’audio est interpolé et converti en un compartiment d’embeddings audio qui est ajouté au conditionnement. | AUDIOENCODEROUTPUT | Non | - |
| `image de référence` | Image de référence optionnelle qui fournit un guide visuel pour la génération vidéo. L’image est agrandie pour correspondre aux dimensions cibles et encodée en un latent, puis ajoutée au conditionnement positif et négatif. Seule la première image du lot est utilisée. | IMAGE | Non | - |
| `vidéo de contrôle` | Vidéo de contrôle optionnelle qui guide le mouvement et la structure de la vidéo générée. La vidéo est agrandie, encodée, puis ajoutée au conditionnement positif et négatif. La vidéo de contrôle est tronquée à la valeur `length` spécifiée. | IMAGE | Non | - |

Remarque : le latent de sortie est initialisé avec des zéros et les dimensions cibles. Le `video_latent` d’entrée n’est pas copié dans cette sortie ; ses 19 dernières images sont utilisées comme référence de mouvement à la place.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Conditionnement positif traité avec le contexte vidéo appliqué, y compris les embeddings audio, les latents de référence, le mouvement de référence et la vidéo de contrôle si fournie | CONDITIONING |
| `négatif` | Conditionnement négatif traité avec le contexte vidéo appliqué, y compris les embeddings audio (mis à zéro), les latents de référence, le mouvement de référence et la vidéo de contrôle si fournie | CONDITIONING |
| `latent` | Représentation du latent vidéo de la séquence étendue, initialisée avec des zéros et des dimensions dérivées du `video_latent` d’entrée et de la `length` cible | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/fr.md)

---
**Source fingerprint (SHA-256):** `32b58aaba566f346a0388ba804fc92e7ad426bf2e9e7039e5fdb0bf6a746e972`
