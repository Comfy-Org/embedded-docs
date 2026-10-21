# TextEncodeFibo2

Encodez un prompt Fibo 2.0 en conditionnement et un latent vide correspondant. Le prompt est soit du texte brut, soit une légende JSON structurée ; lorsque des images sont connectées, il devient l'instruction d'édition, ou une légende JSON du résultat avec une clé `edit_instruction`, et les images servent de latents de référence pour les deux sorties lorsqu'un VAE est connecté. Échantillonnez la sortie `latent`, dont la taille correspond à celle vers laquelle les images sont recadrées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | L'encodeur de texte Fibo 2.0 utilisé pour tokeniser et encoder le prompt. | CLIP | Oui | - |
| `prompt` | La légende à partir de laquelle générer, ou l'instruction d'édition lorsque des images sont connectées. Référencez les images sous la forme `<image_1>`, `<image_2>`, etc. Une légende JSON du résultat attendu fonctionne également, avec la modification décrite dans sa clé `edit_instruction`. | STRING | Oui | - |
| `negative_prompt` | Légende dont il faut s'éloigner, encodée comme conditionnement négatif. Une valeur vide correspond à la légende nulle avec laquelle Fibo 2.0 a été entraîné pour le guidage sans classifieur (par défaut : vide). | STRING | Oui | - |
| `vae` | VAE utilisé pour encoder les images en latents de référence. Sans lui, les images ne conditionnent que l'encodage du texte. | VAE | Non | - |
| `images` | Images à éditer, jusqu'à 16. Une seule image est mise à l'échelle et recadrée au centre à la taille du résultat, car l'édition s'aligne dessus pixel par pixel ; plusieurs images sont chacune mises à l'échelle à leur propre taille d'entraînement. | IMAGE | Non | 0 à 16 images |
| `width` | Largeur du résultat, arrondie au multiple de 16 inférieur. 0 utilise la taille avec laquelle Fibo 2.0 a été entraîné pour le rapport d'aspect de la première image, environ 1 mégapixel, ou 1024 sans images (par défaut : 0). | INT | Oui | 0 à 16384 (pas de 16) |
| `height` | Hauteur du résultat, arrondie au multiple de 16 inférieur. 0 utilise la taille avec laquelle Fibo 2.0 a été entraîné pour le rapport d'aspect de la première image, environ 1 mégapixel, ou 1024 sans images (par défaut : 0). | INT | Oui | 0 à 16384 (pas de 16) |
| `batch_size` | Nombre de latents à créer dans le lot (par défaut : 1). | INT | Oui | 1 à 4096 |

Les latents de référence sont attachés aux deux sorties, de sorte que les images accompagnent le conditionnement plutôt que uniquement la branche positive. Lorsque le VAE n'est pas connecté, les images ne sont vues que par l'encodeur de texte et aucun latent de référence n'est ajouté.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement du prompt, avec les latents de référence lorsqu'un VAE et des images sont connectés. | CONDITIONING |
| `negative` | Conditionnement de `negative_prompt`, texte uniquement, avec les mêmes latents de référence. | CONDITIONING |
| `latent` | Latent vide à la taille demandée, prêt à être échantillonné. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeFibo2/fr.md)

---
**Source fingerprint (SHA-256):** `f400d041a3dd224e30c0fa2acc803e3de11d6c10654bde122e8d569fa1cd1d79`
