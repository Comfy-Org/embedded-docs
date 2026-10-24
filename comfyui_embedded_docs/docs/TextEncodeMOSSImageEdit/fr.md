# Text Encode MOSS-Image Edit

Encode une instruction de modification avec des images de référence en tant que conditionnement pour un LoRA d’édition MOSS-Image. Connectez la sortie comme conditionnement positif et exécutez une seconde instance avec les mêmes références pour le conditionnement négatif. Les références sont utilisées à la taille à laquelle elles arrivent ; redimensionnez-les donc avant de les connecter. Ce nœud est marqué comme expérimental dans ComfyUI. Sans VAE, les images n’entrent que dans l’encodeur de texte.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP qui tokenise l’instruction et l’encode. | CLIP | Oui | - |
| `prompt` | L’instruction décrivant la modification. Prend en charge le texte multiligne et les prompts dynamiques. | STRING | Oui | Tout texte |
| `vae` | Le VAE utilisé pour encoder les images de référence en latents de référence. Facultatif : sans lui, les images n’entrent que dans l’encodeur de texte.| VAE | Non | - |
| `edit_format` | La disposition avec laquelle le LoRA d’édition a été entraîné. Elle sélectionne la méthode des latents de référence et détermine si l’encodeur de texte voit également les références. | COMBO | Oui | `"ai-toolkit"`<br>`"ai-toolkit (kv_cache off)"`<br>`"Moss-Image-Edit"` |
| `images` | Emplacement extensible : connectez une ou plusieurs images de référence (`image_1`, `image_2`, ...). Chaque image est utilisée à la taille à laquelle elle arrive, son canal alpha est supprimé et elle est encodée par le VAE en un latent de référence. Avec un VAE connecté, le canal alpha est supprimé et chaque image est encodée en latent de référence ; sans VAE, les images n’entrent que dans l’encodeur de texte.| IMAGE | Oui | 1 image ou plus |
| `image_strength` | Met à l’échelle l’attention du modèle sur les images vues par l’encodeur de texte (formats ai-toolkit, ou sans VAE) : 0 les ignore, 1 inchangé, au-dessus de 1 les accentue. Avancé. Par défaut : 1.0. | FLOAT | Oui | 0.0 to 100.0 (step 0.05) |

**Remarque :** With `"ai-toolkit"` and `"ai-toolkit (kv_cache off)"`, or when no VAE is connected and `image_strength` is above 0, the text encoder also sees every reference, downscaled to at most 384x384 pixels and preceded by a `Picture N:` marker in the prompt, so the instruction can refer to them by number. With `"Moss-Image-Edit"` and a VAE connected, the references reach the model only as reference latents and the text encoder sees the instruction alone. `"ai-toolkit (kv_cache off)"` additionally keeps the references attending to the image being generated, so they are recomputed on every sampling step.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `conditioning` | L’instruction encodée avec les latents de référence et la méthode de latents de référence correspondante associés. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMOSSImageEdit/fr.md)

---
**Source fingerprint (SHA-256):** `673f098df6a8e466a5c8060009f446eac8f7556311a870de626c5f4bfc3ab196`
