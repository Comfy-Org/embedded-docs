# HunyuanVideo15ImageToVideo

Le nœud HunyuanVideo15ImageToVideo prépare les données de conditionnement et d’espace latent pour la génération vidéo basée sur le modèle HunyuanVideo 1.5. Il crée une représentation latente initiale pour une séquence vidéo et peut éventuellement intégrer une image de départ ou une sortie de vision CLIP pour guider le processus de génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Les prompts de conditionnement positif qui décrivent ce que la vidéo doit contenir. | CONDITIONING | Oui | - |
| `négatif` | Les prompts de conditionnement négatif qui décrivent ce que la vidéo doit éviter. | CONDITIONING | Oui | - |
| `vae` | Le modèle VAE (autoencodeur variationnel) utilisé pour encoder l’image de départ dans l’espace latent. | VAE | Oui | - |
| `largeur` | La largeur des images vidéo de sortie en pixels. Doit être divisible par 16. (par défaut : 848) | INT | Oui | 16 to MAX_RESOLUTION, step: 16 |
| `hauteur` | La hauteur des images vidéo de sortie en pixels. Doit être divisible par 16. (par défaut : 480) | INT | Oui | 16 to MAX_RESOLUTION, step: 16 |
| `longueur` | Le nombre total d’images dans la séquence vidéo. Les valeurs augmentent par pas de 4 à partir de 1 (1, 5, 9, 13, ...). (par défaut : 33) | INT | Oui | 1 to MAX_RESOLUTION, step: 4 |
| `taille_du_lot` | Le nombre de séquences vidéo à générer en un seul lot. (par défaut : 1) | INT | Oui | 1 à 4096 |
| `image_de_départ` | Une image de départ facultative pour initialiser la génération vidéo. Si elle est fournie, elle est encodée et utilisée pour conditionner les premières images. Seules les premières images `length` de l’image sont utilisées. | IMAGE | Non | - |
| `clip_vision_output` | Embeddings de vision CLIP facultatifs pour fournir un conditionnement visuel supplémentaire à la génération. | CLIP_VISION_OUTPUT | Non | - |

**Remarque :** Lorsqu’une `start_image` est fournie, elle est automatiquement redimensionnée pour correspondre aux `width` et `height` spécifiés à l’aide d’une interpolation bilinéaire. Les premières `length` images du lot sont utilisées, et seuls les 3 premiers canaux de couleur de chaque image sont encodés. L’image encodée est ensuite ajoutée aux conditionnements `positive` et `negative` sous la forme d’un `concat_latent_image` avec un `concat_mask` correspondant. Le masque est défini sur 0.0 pour les images couvertes par l’image de départ et sur 1.0 pour les images restantes. Lorsqu’un `clip_vision_output` est fourni, il est également ajouté aux conditionnements `positive` et `negative`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Le conditionnement positif modifié, qui peut désormais inclure l’image de départ encodée ou la sortie de vision CLIP. | CONDITIONING |
| `négatif` | Le conditionnement négatif modifié, qui peut désormais inclure l’image de départ encodée ou la sortie de vision CLIP. | CONDITIONING |
| `latent` | Un tenseur latent vide avec des dimensions configurées pour la taille du lot, la longueur de la vidéo, la largeur et la hauteur spécifiées. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `dbedf7f378ae9613c8f47fe9876a4576c815055b4cdb6bf687b7575fcd7ea80a`
