# Text Encode MOSS-Image Edit

Encode une instruction de modification avec des images de référence en tant que conditionnement pour un LoRA d’édition MOSS-Image. Connectez la sortie comme conditionnement positif et exécutez une seconde instance avec les mêmes références pour le conditionnement négatif. Les références sont utilisées à la taille à laquelle elles arrivent ; redimensionnez-les donc avant de les connecter. Ce nœud est marqué comme expérimental dans ComfyUI.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP qui tokenise l’instruction et l’encode. | CLIP | Oui | - |
| `prompt` | L’instruction décrivant la modification. Prend en charge le texte multiligne et les prompts dynamiques. | STRING | Oui | Tout texte |
| `vae` | Le VAE utilisé pour encoder les images de référence en latents de référence. | VAE | Oui | - |
| `edit_format` | La disposition avec laquelle le LoRA d’édition a été entraîné. Elle sélectionne la méthode des latents de référence et détermine si l’encodeur de texte voit également les références. | COMBO | Oui | `"ai-toolkit"`<br>`"ai-toolkit (kv_cache off)"`<br>`"Moss-Image-Edit"` |
| `images` | Emplacement extensible : connectez une ou plusieurs images de référence (`image_1`, `image_2`, ...). Chaque image est utilisée à la taille à laquelle elle arrive, son canal alpha est supprimé et elle est encodée par le VAE en un latent de référence. | IMAGE | Oui | 1 image ou plus |

**Remarque :** Avec `"ai-toolkit"` et `"ai-toolkit (kv_cache off)"`, l’encodeur de texte voit également chaque référence, réduite à 384x384 pixels au maximum et précédée d’un marqueur `Picture N:` dans le prompt, afin que l’instruction puisse y faire référence par numéro. Avec `"Moss-Image-Edit"`, les références n’atteignent le modèle que sous forme de latents de référence et l’encodeur de texte ne voit que l’instruction. `"ai-toolkit (kv_cache off)"` maintient en outre les références en attention sur l’image en cours de génération ; elles sont donc recalculées à chaque étape d’échantillonnage.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `conditioning` | L’instruction encodée avec les latents de référence et la méthode de latents de référence correspondante associés. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMOSSImageEdit/fr.md)

---
**Source fingerprint (SHA-256):** `30e4edbb129f647cdce4ec95f78c002ecdc9a4f8fc5a45f1477fdc555b541dae`
