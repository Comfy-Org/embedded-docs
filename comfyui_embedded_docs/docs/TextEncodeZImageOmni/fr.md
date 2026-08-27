# TextEncodeZImageOmni

TextEncodeZImageOmni encode un prompt texte ainsi que jusqu'à trois images de référence optionnelles dans un format de conditionnement pour les modèles de génération d'images. Le prompt est tokenisé et encodé avec le modèle CLIP, et chaque image connectée peut éventuellement être traitée par un encodeur de vision et/ou un VAE afin que les références visuelles soient intégrées au texte. Ce nœud est marqué comme expérimental.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour tokeniser et encoder le prompt texte. | CLIP | Oui |  |
| `encodeur d'image` | Un modèle encodeur de vision optionnel. S'il est fourni, il est utilisé pour encoder les images d'entrée, et les plongements résultants sont ajoutés au conditionnement. | CLIP_VISION | Non |  |
| `invite` | Le prompt texte à encoder. Prend en charge la saisie multiligne et les prompts dynamiques. | STRING | Oui |  |
| `redimensionnement automatique des images` | Lorsqu'il est activé (par défaut : True), les images d'entrée sont automatiquement redimensionnées avant l'encodage VAE afin que leur surface totale en pixels soit proche de 1024x1024, avec des dimensions arrondies à des multiples de 8. | BOOLEAN | Non | True<br>False |
| `vae` | Un modèle VAE optionnel. S'il est fourni, il est utilisé pour encoder les images d'entrée en représentations latentes, qui sont ajoutées au conditionnement en tant que latents de référence. | VAE | Non |  |
| `image1` | La première image de référence optionnelle. | IMAGE | Non |  |
| `image2` | La deuxième image de référence optionnelle. | IMAGE | Non |  |
| `image3` | La troisième image de référence optionnelle. | IMAGE | Non |  |

**Remarque :** Le nœud accepte un maximum de trois images (`image1`, `image2`, `image3`). Les entrées `image_encoder` et `vae` ne sont utilisées que lorsqu'au moins une image est fournie ; lorsque les deux sont connectées, chaque image est traitée par les deux. Lorsque `auto_resize_images` est défini sur True et qu'un `vae` est connecté, les images sont redimensionnées pour avoir une surface totale en pixels proche de 1024x1024 avant l'encodage.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | La sortie de conditionnement finale. Elle contient le prompt texte encodé et, lorsque des images sont fournies, peut inclure des plongements d'images encodés, des latents de référence et des plongements de texte supplémentaires dérivés du gabarit avec espace réservé pour l'image. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/fr.md)

---
**Source fingerprint (SHA-256):** `b40a3150f536b6f37e2b53e6d9992fcb4fd32dceb540c0a76773a7ba1af9a7b8`
