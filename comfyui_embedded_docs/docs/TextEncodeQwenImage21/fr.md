# TextEncodeQwenImage21

Le nœud TextEncodeQwenImage21 encode un prompt et un prompt négatif pour le modèle Qwen-Image 2.1, en attachant éventuellement des images de référence. Les images de référence sont vues par l'encodeur de texte et, lorsqu'un VAE est connecté, sont également encodées sous forme de latents insérés dans la séquence, de sorte que le conditionnement porte à la fois l'instruction textuelle et la référence visuelle. Le nœud renvoie un conditionnement positif et négatif ainsi qu'un latent vide dimensionné sur la première image de référence, prêt à être échantillonné.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `clip` | L'encodeur de texte Qwen-Image 2.1 utilisé pour tokeniser et encoder les prompts. | CLIP | Oui | - |
| `prompt` | Prompt textuel décrivant l'image à générer ou la modification à appliquer. Prend en charge la saisie multiligne et les prompts dynamiques. | STRING | Oui | Tout texte |
| `negative_prompt` | Prompt textuel décrivant ce que le résultat doit éviter. Prend en charge la saisie multiligne et les prompts dynamiques. | STRING | Oui | Tout texte |
| `vae` | VAE utilisé pour encoder les images de référence en latents de référence. Lorsqu'il est omis, les images de référence conditionnent le résultat uniquement via l'encodeur de texte. | VAE | Non | - |
| `resolution` | Les images de référence sont redimensionnées à environ `resolution` x `resolution` pixels, par multiples de 32, en conservant le rapport d'aspect. 0 conserve chaque référence à sa propre taille, arrondie à un multiple de 32 (par défaut : 1024). | INT | Oui | 0 à 4096 (pas 32) |
| `images` | Images de référence, vues par l'encodeur de texte et insérées dans la séquence en tant que latents VAE. Emplacement extensible : connectez jusqu'à 16 images (`image_1` ... `image_16`). | IMAGE | Non | 0 à 16 images |

Le latent vide en sortie est dimensionné sur la première image de référence connectée, ou sur `resolution` lorsqu'aucune image de référence n'est connectée. Échantillonnez à partir du latent renvoyé par ce nœud : toute autre taille décale la modification. Lorsqu'un VAE est connecté, les mêmes latents de référence sont attachés à la fois au conditionnement positif et au conditionnement négatif, de sorte qu'une seule étape d'échantillonnage peut débruiter les deux.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement encodé pour le prompt, portant les latents de référence lorsqu'un VAE est connecté. | CONDITIONING |
| `negative` | Conditionnement encodé pour le prompt négatif, avec les mêmes latents de référence. | CONDITIONING |
| `latent` | Latent vide à la taille de la première image de référence, ou 1024 x 1024 lorsqu'aucune image de référence n'est connectée. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImage21/fr.md)

---
**Source fingerprint (SHA-256):** `3870f04597d12b593498c12ca139428af2d717b65aa40c889de9373ae9eb475e`
