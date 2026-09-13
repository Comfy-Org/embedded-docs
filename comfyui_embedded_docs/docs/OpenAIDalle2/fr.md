# OpenAIDalle2

Génère des images de manière synchrone via le point de terminaison DALL·E 2 d’OpenAI. Le nœud envoie une invite textuelle à l’API DALL·E 2 d’OpenAI et renvoie la ou les images résultantes à ComfyUI. Il peut également modifier une image existante lorsque `image` et `mask` sont tous deux fournis ensemble.

## Fonctionnement

Ce nœud se connecte à l’API DALL·E 2 d’OpenAI pour créer des images à partir de descriptions textuelles. Lorsque vous fournissez une invite textuelle, le nœud l’envoie aux serveurs d’OpenAI qui génèrent les images correspondantes et les renvoient à ComfyUI. Le nœud peut fonctionner selon deux modes : la génération d’images standard en utilisant uniquement une invite textuelle, ou le mode d’édition d’image lorsque `image` et `mask` sont tous deux fournis. En mode édition, il utilise le masque pour déterminer les parties de l’image originale qui doivent être modifiées tout en laissant les autres zones inchangées.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Invite textuelle pour DALL·E (par défaut : vide) | STRING | Oui | - |
| `seed` | pas encore implémenté dans le backend (par défaut : 0) | INT | Non | 0 à 2147483647 |
| `size` | Taille de l’image (par défaut : "1024x1024") | COMBO | Non | "256x256"<br>"512x512"<br>"1024x1024" |
| `n` | Nombre d’images à générer (par défaut : 1) | INT | Non | 1 à 8 |
| `image` | Image de référence facultative pour l’édition d’image. | IMAGE | Non | - |
| `mask` | Masque facultatif pour l’inpainting (les zones blanches seront remplacées) | MASK | Non | - |

**Remarque :** Le mode d’édition d’image n’est activé que lorsque `image` et `mask` sont tous deux fournis ensemble. Si un seul des deux est fourni, une erreur est levée. Le `mask` doit avoir la même taille que l’`image` ; sinon, une erreur est levée. En mode édition, les zones blanches du masque indiquent les régions qui seront remplacées.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `IMAGE` | La ou les images générées ou modifiées par DALL·E 2 | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/fr.md)

---
**Source fingerprint (SHA-256):** `c6bba5dd44ebed1d795e6ec93bdd2e19685e8ae9f24be9145ad9d74d3a9b7a0c`
