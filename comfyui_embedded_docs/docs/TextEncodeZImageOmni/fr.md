Voici la traduction en français de la documentation du nœud TextEncodeZImageOmni :

Le nœud TextEncodeZImageOmni est un nœud de conditionnement avancé qui encode une invite textuelle ainsi que des images de référence optionnelles dans un format de conditionnement adapté aux modèles de génération d'images. Il peut traiter jusqu'à trois images, en les encodant éventuellement avec un encodeur visuel et/ou un VAE pour produire des latentes de référence, et intègre ces références visuelles à l'invite textuelle en utilisant une structure de modèle spécifique.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour tokeniser et encoder l'invite textuelle. | CLIP | Oui |  |
| `encodeur d'image` | Un modèle d'encodeur visuel optionnel. S'il est fourni, il sera utilisé pour encoder les images d'entrée, et les embeddings résultants seront ajoutés au conditionnement. | CLIPVision | Non |  |
| `invite` | L'invite textuelle à encoder. Ce champ prend en charge les entrées multilignes et les invites dynamiques. | STRING | Oui |  |
| `redimensionnement automatique des images` | Lorsqu'il est activé (par défaut : True), les images d'entrée sont automatiquement redimensionnées en fonction de leur surface en pixels avant d'être transmises au VAE pour encodage. | BOOLEAN | Non |  |
| `vae` | Un modèle VAE optionnel. S'il est fourni, il sera utilisé pour encoder les images d'entrée en représentations latentes, qui sont ajoutées au conditionnement en tant que latentes de référence. | VAE | Non |  |
| `image1` | La première image de référence optionnelle. | IMAGE | Non |  |
| `image2` | La deuxième image de référence optionnelle. | IMAGE | Non |  |
| `image3` | La troisième image de référence optionnelle. | IMAGE | Non |  |

**Remarque :** Le nœud peut accepter un maximum de trois images (`image1`, `image2`, `image3`). Les entrées `image_encoder` et `vae` ne sont utilisées que si au moins une image est fournie. Lorsque `auto_resize_images` est True et qu'un `vae` est connecté, les images sont redimensionnées pour avoir une surface totale en pixels proche de 1024x1024 avant encodage.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | La sortie de conditionnement finale, qui contient l'invite textuelle encodée et peut inclure des embeddings d'images encodées et/ou des latentes de référence si des images ont été fournies. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/fr.md)

---
**Source fingerprint (SHA-256):** `daa4205acdf72503180eeedb4142708d239d4ff0f689012a298264ae2d8ea949`
