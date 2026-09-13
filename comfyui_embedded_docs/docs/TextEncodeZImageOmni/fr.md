# TextEncodeZImageOmni

TextEncodeZImageOmni encode un prompt textuel avec jusqu’à trois images de référence optionnelles dans un format de conditionnement pour les modèles de génération d’images. Le prompt est tokenisé et encodé avec le modèle CLIP, et chaque image connectée peut éventuellement être traitée par un encodeur visuel et/ou un VAE afin que les références visuelles soient intégrées aux côtés du texte. Ce nœud est marqué comme expérimental.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour tokeniser et encoder le prompt textuel. | CLIP | Oui |  |
| `encodeur d'image` | Un modèle d’encodeur visuel optionnel. S’il est fourni, il est utilisé pour encoder les images d’entrée, et les embeddings résultants sont ajoutés au conditionnement. | CLIP_VISION | Non |  |
| `invite` | Le prompt textuel à encoder. Prend en charge la saisie multiligne et les prompts dynamiques. | STRING | Oui |  |
| `redimensionnement automatique des images` | Lorsque cette option est activée (par défaut : True), les images d’entrée sont automatiquement redimensionnées avant l’encodage VAE afin que leur surface totale en pixels soit proche de 1024x1024, les dimensions étant arrondies à des multiples de 8. | BOOLEAN | Oui | True<br>False |
| `vae` | Un modèle VAE optionnel. S’il est fourni, il est utilisé pour encoder les images d’entrée en représentations latentes, qui sont ajoutées au conditionnement en tant que latents de référence. | VAE | Non |  |
| `image1` | La première image de référence optionnelle. | IMAGE | Non |  |
| `image2` | La deuxième image de référence optionnelle. | IMAGE | Non |  |
| `image3` | La troisième image de référence optionnelle. | IMAGE | Non |  |

**Remarque :** Le nœud accepte au maximum trois images (`image1`, `image2`, `image3`). Les entrées `image_encoder` et `vae` ne sont utilisées que lorsqu’au moins une image est fournie ; lorsque les deux entrées sont connectées, chaque image est traitée par les deux. Lorsque `auto_resize_images` vaut True et qu’un `vae` est connecté, les images sont redimensionnées pour avoir une surface totale en pixels proche de 1024x1024 avant l’encodage. Si aucune image n’est fournie, seul le prompt textuel est encodé.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | La sortie de conditionnement finale. Elle contient le prompt textuel encodé et, lorsque des images sont fournies, peut inclure des embeddings d’images encodés, des latents de référence et des embeddings textuels supplémentaires dérivés du gabarit d’espace réservé d’image. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/fr.md)

---
**Source fingerprint (SHA-256):** `b40a3150f536b6f37e2b53e6d9992fcb4fd32dceb540c0a76773a7ba1af9a7b8`
