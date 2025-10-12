> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/fr.md)

Le nœud HunyuanImageToVideo convertit des images en représentations latentes vidéo en utilisant le modèle vidéo Hunyuan. Il prend des entrées de conditionnement et des images de départ optionnelles pour générer des latents vidéo qui peuvent être traités ultérieurement par des modèles de génération vidéo. Le nœud prend en charge différents types de guidage pour contrôler la manière dont l'image de départ influence le processus de génération vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | Entrée de conditionnement positive pour guider la génération vidéo |
| `vae` | VAE | Oui | - | Modèle VAE utilisé pour encoder les images dans l'espace latent |
| `largeur` | INT | Oui | 16 à MAX_RESOLUTION | Largeur de la vidéo de sortie en pixels (par défaut : 848, pas : 16) |
| `hauteur` | INT | Oui | 16 à MAX_RESOLUTION | Hauteur de la vidéo de sortie en pixels (par défaut : 480, pas : 16) |
| `longueur` | INT | Oui | 1 à MAX_RESOLUTION | Nombre d'images dans la vidéo de sortie (par défaut : 53, pas : 4) |
| `taille_du_lot` | INT | Oui | 1 à 4096 | Nombre de vidéos à générer simultanément (par défaut : 1) |
| `type_de_guidage` | COMBO | Oui | "v1 (concat)"<br>"v2 (replace)"<br>"custom" | Méthode d'incorporation de l'image de départ dans la génération vidéo |
| `image_de_départ` | IMAGE | Non | - | Image de départ optionnelle pour initialiser la génération vidéo |

**Note :** Lorsque `start_image` est fournie, le nœud utilise différentes méthodes de guidage selon le `guidance_type` sélectionné :

- "v1 (concat)" : Concatène le latent d'image avec le latent vidéo
- "v2 (replace)" : Remplace les images vidéo initiales par le latent d'image
- "custom" : Utilise l'image comme latent de référence pour le guidage

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `latent` | CONDITIONING | Conditionnement positif modifié avec le guidage d'image appliqué lorsque start_image est fournie |
| `latent` | LATENT | Représentation latente vidéo prête pour un traitement ultérieur par les modèles de génération vidéo |
