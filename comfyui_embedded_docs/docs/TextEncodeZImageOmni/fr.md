> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/fr.md)

Voici la traduction en français de la documentation du nœud TextEncodeZImageOmni :

Le nœud TextEncodeZImageOmni est un nœud de conditionnement avancé qui encode une invite textuelle ainsi que des images de référence optionnelles dans un format de conditionnement adapté aux modèles de génération d'images. Il peut traiter jusqu'à trois images, en les encodant éventuellement avec un encodeur visuel et/ou un VAE pour produire des latentes de référence, et intègre ces références visuelles à l'invite textuelle en utilisant une structure de modèle spécifique.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `clip` | CLIP | Oui | | Le modèle CLIP utilisé pour tokeniser et encoder l'invite textuelle. |
| `encodeur d'image` | CLIPVision | Non | | Un modèle d'encodeur visuel optionnel. S'il est fourni, il sera utilisé pour encoder les images d'entrée, et les embeddings résultants seront ajoutés au conditionnement. |
| `invite` | STRING | Oui | | L'invite textuelle à encoder. Ce champ prend en charge les entrées multilignes et les invites dynamiques. |
| `redimensionnement automatique des images` | BOOLEAN | Non | | Lorsqu'il est activé (par défaut : True), les images d'entrée sont automatiquement redimensionnées en fonction de leur surface en pixels avant d'être transmises au VAE pour encodage. |
| `vae` | VAE | Non | | Un modèle VAE optionnel. S'il est fourni, il sera utilisé pour encoder les images d'entrée en représentations latentes, qui sont ajoutées au conditionnement en tant que latentes de référence. |
| `image1` | IMAGE | Non | | La première image de référence optionnelle. |
| `image2` | IMAGE | Non | | La deuxième image de référence optionnelle. |
| `image3` | IMAGE | Non | | La troisième image de référence optionnelle. |

**Remarque :** Le nœud peut accepter un maximum de trois images (`image1`, `image2`, `image3`). Les entrées `image_encoder` et `vae` ne sont utilisées que si au moins une image est fournie. Lorsque `auto_resize_images` est True et qu'un `vae` est connecté, les images sont redimensionnées pour avoir une surface totale en pixels proche de 1024x1024 avant encodage.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `CONDITIONING` | CONDITIONING | La sortie de conditionnement finale, qui contient l'invite textuelle encodée et peut inclure des embeddings d'images encodées et/ou des latentes de référence si des images ont été fournies. |

---
**Source fingerprint (SHA-256):** `daa4205acdf72503180eeedb4142708d239d4ff0f689012a298264ae2d8ea949`
