> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/fr.md)

Le nœud HunyuanVideo15ImageToVideo prépare les données de conditionnement et d'espace latent pour la génération vidéo basée sur le modèle HunyuanVideo 1.5. Il crée une représentation latente initiale pour une séquence vidéo et peut intégrer en option une image de départ ou une sortie de vision CLIP pour guider le processus de génération.

## Entrées

| Paramètre | Type de Données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | Les prompts de conditionnement positifs qui décrivent ce que la vidéo doit contenir. |
| `negative` | CONDITIONING | Oui | - | Les prompts de conditionnement négatifs qui décrivent ce que la vidéo doit éviter. |
| `vae` | VAE | Oui | - | Le modèle VAE (Autoencodeur Variationnel) utilisé pour encoder l'image de départ dans l'espace latent. |
| `width` | INT | Non | 16 à MAX_RESOLUTION | La largeur des images de sortie de la vidéo en pixels. Doit être divisible par 16. (par défaut : 848) |
| `height` | INT | Non | 16 à MAX_RESOLUTION | La hauteur des images de sortie de la vidéo en pixels. Doit être divisible par 16. (par défaut : 480) |
| `length` | INT | Non | 1 à MAX_RESOLUTION | Le nombre total d'images dans la séquence vidéo. (par défaut : 33) |
| `batch_size` | INT | Non | 1 à 4096 | Le nombre de séquences vidéo à générer en un seul lot. (par défaut : 1) |
| `start_image` | IMAGE | Non | - | Une image de départ optionnelle pour initialiser la génération vidéo. Si elle est fournie, elle est encodée et utilisée pour conditionner les premières images. |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Non | - | Des embeddings de vision CLIP optionnels pour fournir un conditionnement visuel supplémentaire à la génération. |

**Note :** Lorsqu'une `start_image` est fournie, elle est automatiquement redimensionnée pour correspondre à la `width` et `height` spécifiées en utilisant une interpolation bilinéaire. Les premières `length` images du lot d'images sont utilisées. L'image encodée est ensuite ajoutée aux conditionnements `positive` et `negative` en tant que `concat_latent_image` avec un `concat_mask` correspondant.

## Sorties

| Nom de la Sortie | Type de Données | Description |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Le conditionnement positif modifié, qui peut maintenant inclure l'image de départ encodée ou la sortie de vision CLIP. |
| `negative` | CONDITIONING | Le conditionnement négatif modifié, qui peut maintenant inclure l'image de départ encodée ou la sortie de vision CLIP. |
| `latent` | LATENT | Un tenseur latent vide avec des dimensions configurées pour la taille de lot, la longueur vidéo, la largeur et la hauteur spécifiées. |
