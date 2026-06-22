# OpenAI DALL·E 3

Génère des images de manière synchrone via le point d'accès DALL·E 3 d'OpenAI. Ce nœud prend une invite textuelle et crée les images correspondantes en utilisant le modèle DALL·E 3 d'OpenAI, vous permettant de spécifier la qualité, le style et les dimensions de l'image.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Invite textuelle pour DALL·E (par défaut : "") | STRING | Oui | - |
| `seed` | Pas encore implémenté dans le backend (par défaut : 0) | INT | Non | 0 à 2147483647 |
| `qualité` | Qualité de l'image (par défaut : "standard") | COMBO | Non | "standard"<br>"hd" |
| `style` | Le style "vivid" incite le modèle à générer des images hyper-réalistes et dramatiques. Le style "natural" produit des images plus naturelles, moins hyper-réalistes. (par défaut : "natural") | COMBO | Non | "natural"<br>"vivid" |
| `taille` | Taille de l'image (par défaut : "1024x1024") | COMBO | Non | "1024x1024"<br>"1024x1792"<br>"1792x1024" |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `IMAGE` | L'image générée par DALL·E 3 | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle3/fr.md)

---
**Source fingerprint (SHA-256):** `e36bfe2a6ecec050906f220de3a3edf06eff0bfd6e21f08ce90579172a07d7eb`
