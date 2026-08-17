# TextEncodeZImageOmni

Le nœud TextEncodeZImageOmni est un nœud de conditionnement avancé qui encode une invite texte ainsi que des images de référence optionnelles dans un format de conditionnement adapté aux modèles de génération d’images. Il peut traiter jusqu’à trois images, les encoder éventuellement avec un encodeur vision et/ou un VAE pour produire des latents de référence, et intègre ces références visuelles à l’invite texte à l’aide d’une structure de gabarit spécifique.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour tokeniser et encoder l’invite texte. | CLIP | Oui |  |
| `image_encoder` | Un modèle d’encodeur vision optionnel. S’il est fourni, il est utilisé pour encoder les images d’entrée, et les embeddings résultants sont ajoutés au conditionnement. | CLIPVision | Non |  |
| `prompt` | L’invite texte à encoder. Ce champ prend en charge les saisies multilignes et les invites dynamiques. | STRING | Oui |  |
| `auto_resize_images` | Lorsque cette option est activée (par défaut : True), les images d’entrée sont automatiquement redimensionnées en fonction de leur surface en pixels avant d’être transmises au VAE pour l’encodage. Il s’agit d’un paramètre avancé. | BOOLEAN | Non |  |
| `vae` | Un modèle VAE optionnel. S’il est fourni, il est utilisé pour encoder les images d’entrée en représentations latentes, qui sont ajoutées au conditionnement en tant que latents de référence. | VAE | Non |  |
| `image1` | La première image de référence optionnelle. | IMAGE | Non |  |
| `image2` | La deuxième image de référence optionnelle. | IMAGE | Non |  |
| `image3` | La troisième image de référence optionnelle. | IMAGE | Non |  |

**Remarque :** Le nœud peut accepter au maximum trois images (`image1`, `image2`, `image3`). Les entrées `image_encoder` et `vae` ne sont utilisées que si au moins une image est fournie. Lorsque `auto_resize_images` est défini sur True et qu’un `vae` est connecté, les images sont redimensionnées pour avoir une surface totale en pixels proche de 1024x1024 pixels, avec des dimensions arrondies à des multiples de 8, avant l’encodage. Si aucune image n’est fournie, le nœud encode l’invite texte sans aucune référence visuelle.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | La sortie de conditionnement finale, qui contient l’invite texte encodée et peut inclure des embeddings d’images encodées et/ou des latents de référence si des images ont été fournies. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/fr.md)

---
**Source fingerprint (SHA-256):** `b40a3150f536b6f37e2b53e6d9992fcb4fd32dceb540c0a76773a7ba1af9a7b8`
