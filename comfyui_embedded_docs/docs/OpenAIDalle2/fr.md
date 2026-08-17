# OpenAI DALL·E 2

OpenAI DALL·E 2 génère des images de manière synchrone via le point de terminaison DALL·E 2 d'OpenAI. Fournissez un prompt textuel pour créer de nouvelles images, ou fournissez à la fois une image et un masque pour modifier une image existante.

## Fonctionnement

Ce nœud se connecte à l'API DALL·E 2 d'OpenAI pour créer des images à partir de descriptions textuelles. Lorsque vous fournissez un prompt textuel, le nœud l'envoie aux serveurs d'OpenAI qui génèrent les images correspondantes et les renvoient à ComfyUI. Le nœud peut fonctionner selon deux modes : la génération d'images standard à l'aide d'un simple prompt textuel, ou le mode édition d'image lorsqu'une image et un masque sont fournis. En mode édition, il utilise le masque pour déterminer les parties de l'image d'origine qui doivent être modifiées tout en laissant les autres zones inchangées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt textuel pour DALL·E (par défaut : vide) | STRING | Oui | - |
| `seed` | Pas encore implémenté dans le backend (par défaut : 0) | INT | Non | 0 à 2147483647 |
| `size` | Taille de l'image (par défaut : "1024x1024") | COMBO | Non | "256x256"<br>"512x512"<br>"1024x1024" |
| `n` | Nombre d'images à générer (par défaut : 1) | INT | Non | 1 à 8 |
| `image` | Image de référence optionnelle pour l'édition d'image. | IMAGE | Non | - |
| `mask` | Masque optionnel pour l'inpainting (les zones blanches seront remplacées) | MASK | Non | - |

Note : `image` et `mask` doivent être fournis ensemble. Lorsque les deux sont fournis, le nœud passe en mode édition d'image. Si un seul d'entre eux est fourni, une erreur est déclenchée. Le `mask` doit avoir la même taille que l'`image`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | Les images générées ou modifiées par DALL·E 2 | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/fr.md)

---
**Source fingerprint (SHA-256):** `c6bba5dd44ebed1d795e6ec93bdd2e19685e8ae9f24be9145ad9d74d3a9b7a0c`
