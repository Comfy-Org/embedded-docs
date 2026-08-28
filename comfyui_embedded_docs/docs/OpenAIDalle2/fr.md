# OpenAI DALL·E 2

Génère des images de manière synchrone via le endpoint DALL·E 2 d'OpenAI.

## Comment ça marche

Ce nœud se connecte à l'API DALL·E 2 d'OpenAI pour créer des images à partir de descriptions textuelles. Lorsque vous fournissez un prompt texte, le nœud l'envoie aux serveurs d'OpenAI qui génèrent les images correspondantes et les renvoient à ComfyUI. Le nœud peut fonctionner selon deux modes : la génération d'image standard utilisant uniquement un prompt texte, ou le mode édition d'image lorsqu'une image et un masque sont fournis. En mode édition, il utilise le masque pour déterminer quelles parties de l'image d'origine doivent être modifiées tout en laissant les autres zones inchangées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt texte pour DALL·E (défaut : vide) | STRING | Oui | - |
| `seed` | Pas encore implémenté dans le backend (défaut : 0) | INT | Non | 0 à 2147483647 |
| `taille` | Taille de l'image (défaut : "1024x1024") | COMBO | Non | "256x256"<br>"512x512"<br>"1024x1024" |
| `n` | Nombre d'images à générer (défaut : 1) | INT | Non | 1 à 8 |
| `image` | Image de référence optionnelle pour l'édition d'image. | IMAGE | Non | - |
| `mask` | Masque optionnel pour l'inpainting (les zones blanches seront remplacées) | MASK | Non | - |

**Note :** Le mode édition d'image n'est activé que lorsque `image` et `mask` sont fournis ensemble. Si un seul d'entre eux est fourni, une erreur est générée. Le `mask` doit avoir la même taille que l'`image` ; sinon, une erreur est générée. En mode édition, les zones blanches du masque indiquent les régions qui seront remplacées.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `IMAGE` | L'image (ou les images) générée(s) ou modifiée(s) par DALL·E 2 | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/fr.md)

---
**Source fingerprint (SHA-256):** `c6bba5dd44ebed1d795e6ec93bdd2e19685e8ae9f24be9145ad9d74d3a9b7a0c`
