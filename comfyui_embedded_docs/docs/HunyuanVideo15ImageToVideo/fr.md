# HunyuanVideo15ImageToVideo

Voici la traduction en français de la documentation du nœud HunyuanVideo15ImageToVideo :

Le nœud HunyuanVideo15ImageToVideo prépare les données de conditionnement et d'espace latent pour la génération vidéo basée sur le modèle HunyuanVideo 1.5. Il crée une représentation latente initiale pour une séquence vidéo et peut éventuellement intégrer une image de départ ou une sortie CLIP vision pour guider le processus de génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Les invites de conditionnement positives qui décrivent ce que la vidéo doit contenir. | CONDITIONING | Oui | - |
| `négatif` | Les invites de conditionnement négatives qui décrivent ce que la vidéo doit éviter. | CONDITIONING | Oui | - |
| `vae` | Le modèle VAE (autoencodeur variationnel) utilisé pour encoder l'image de départ dans l'espace latent. | VAE | Oui | - |
| `largeur` | La largeur des images vidéo de sortie en pixels. Doit être divisible par 16. (par défaut : 848) | INT | Non | 16 à MAX_RESOLUTION |
| `hauteur` | La hauteur des images vidéo de sortie en pixels. Doit être divisible par 16. (par défaut : 480) | INT | Non | 16 à MAX_RESOLUTION |
| `longueur` | Le nombre total d'images dans la séquence vidéo. Doit être un multiple de 4. (par défaut : 33) | INT | Non | 1 à MAX_RESOLUTION |
| `taille_du_lot` | Le nombre de séquences vidéo à générer en un seul lot. (par défaut : 1) | INT | Non | 1 à 4096 |
| `image_de_départ` | Une image de départ facultative pour initialiser la génération vidéo. Si fournie, elle est encodée et utilisée pour conditionner les premières images. Seules les premières images de la séquence, correspondant à la valeur `longueur`, sont utilisées. | IMAGE | Non | - |
| `clip_vision_output` | Plongements CLIP vision facultatifs pour fournir un conditionnement visuel supplémentaire à la génération. | CLIP_VISION_OUTPUT | Non | - |

**Remarque :** Lorsqu'une `start_image` est fournie, elle est automatiquement redimensionnée pour correspondre à la `width` et à la `height` spécifiées à l'aide d'une interpolation bilinéaire. Les premières images du lot, correspondant à la valeur `length`, sont utilisées. L'image encodée est ensuite ajoutée au conditionnement `positive` et `negative` en tant que `concat_latent_image` avec un `concat_mask` correspondant. Le masque est défini sur 0,0 pour les images couvertes par l'image de départ et sur 1,0 pour les images restantes.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Le conditionnement positif modifié, qui peut désormais inclure l'image de départ encodée ou la sortie CLIP vision. | CONDITIONING |
| `négatif` | Le conditionnement négatif modifié, qui peut désormais inclure l'image de départ encodée ou la sortie CLIP vision. | CONDITIONING |
| `latent` | Un tenseur latent vide dont les dimensions sont configurées pour la taille de lot, la longueur vidéo, la largeur et la hauteur spécifiées. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `2f41bbb080672683fb1755be575f08c79ca03e324df66953eb40631581197d47`
