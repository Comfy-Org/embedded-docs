# WanFirstLastFrameToVideo

Le nœud WanFirstLastFrameToVideo prépare le conditionnement pour la génération vidéo en combinant une image de début et une image de fin avec des invites de texte. Il encode les images des frames dans l'espace latent, crée un masque qui indique au modèle vidéo quelles frames sont déjà connues, et attache les caractéristiques CLIP vision lorsqu'elles sont fournies. Le nœud produit un conditionnement positif et négatif mis à jour ainsi qu'un latent vide qui définit la taille et la longueur de la vidéo à générer.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Conditionnement de texte positif utilisé pour guider la génération vidéo. | CONDITIONING | Oui | - |
| `négatif` | Conditionnement de texte négatif utilisé pour guider la génération vidéo. | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images de frames combinées dans l'espace latent. | VAE | Oui | - |
| `largeur` | Largeur de la vidéo générée en pixels (défaut : 832, pas : 16). | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo générée en pixels (défaut : 480, pas : 16). | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre de frames dans la séquence vidéo (défaut : 81, pas : 4). | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_du_lot` | Nombre de vidéos à générer en une fois (défaut : 1). | INT | Oui | 1 à 4096 |
| `clip_vision_image_de_départ` | Caractéristiques CLIP vision extraites de l'image de début. Si les entrées CLIP vision de début et de fin sont toutes deux fournies, leurs caractéristiques sont combinées. | CLIP_VISION_OUTPUT | Non | - |
| `clip_vision_image_de_fin` | Caractéristiques CLIP vision extraites de l'image de fin. Si les entrées CLIP vision de début et de fin sont toutes deux fournies, leurs caractéristiques sont combinées. | CLIP_VISION_OUTPUT | Non | - |
| `image_de_départ` | Image de frame de début pour la séquence vidéo. Ses premières `length` frames sont utilisées et redimensionnées à `width` × `height`. | IMAGE | Non | - |
| `image_de_fin` | Image de frame de fin pour la séquence vidéo. Ses dernières `length` frames sont utilisées et redimensionnées à `width` × `height`. | IMAGE | Non | - |

**Remarque :** Lorsqu'au moins une des entrées `start_image` ou `end_image` est fournie, le nœud construit une séquence de frames combinée où les frames de début et de fin sont remplies et les frames restantes utilisent un espace réservé gris neutre (0,5). Un masque marque les régions remplies comme connues et les régions d'espace réservé comme inconnues, permettant au modèle vidéo de générer les frames intermédiaires. Lorsqu'une image de début est fournie, la région connue s'étend également de 3 frames supplémentaires au-delà de l'image. La même image de frame encodée et le même masque sont attachés à la fois au conditionnement `positive` et `negative`. Si les deux entrées CLIP vision sont fournies, leurs états cachés sont concaténés ; si une seule est fournie, elle est utilisée seule. La longueur vidéo latente est dérivée de `length` après compression temporelle : `((length - 1) // 4) + 1`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Conditionnement positif avec l'image de frame encodée, le masque et, si fournies, les caractéristiques CLIP vision attachées. | CONDITIONING |
| `négatif` | Conditionnement négatif avec l'image de frame encodée, le masque et, si fournies, les caractéristiques CLIP vision attachées. | CONDITIONING |
| `latent` | Tenseur latent vide (tous des zéros) dimensionné pour la taille de lot, la longueur vidéo et la résolution données. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `0072e441cb80334c3c961d1bbf2d081c78bc38ed1eacca840c577a2d01b36f05`
