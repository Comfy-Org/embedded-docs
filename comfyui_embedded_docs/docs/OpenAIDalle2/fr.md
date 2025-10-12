> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/fr.md)

Génère des images de manière synchrone via le point de terminaison DALL·E 2 d'OpenAI.

## Fonctionnement

Ce nœud se connecte à l'API DALL·E 2 d'OpenAI pour créer des images basées sur des descriptions textuelles. Lorsque vous fournissez une invite textuelle, le nœud l'envoie aux serveurs d'OpenAI qui génèrent les images correspondantes et les renvoient à ComfyUI. Le nœud peut fonctionner dans deux modes : la génération d'image standard utilisant uniquement une invite textuelle, ou le mode d'édition d'image lorsqu'une image et un masque sont fournis. En mode édition, il utilise le masque pour déterminer quelles parties de l'image originale doivent être modifiées tout en conservant les autres zones inchangées.

## Entrées

| Paramètre | Type de données | Type d'entrée | Défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `prompt` | STRING | requis | "" | - | Invite textuelle pour DALL·E |
| `seed` | INT | optionnel | 0 | 0 à 2147483647 | pas encore implémenté dans le backend |
| `size` | COMBO | optionnel | "1024x1024" | "256x256", "512x512", "1024x1024" | Taille de l'image |
| `n` | INT | optionnel | 1 | 1 à 8 | Nombre d'images à générer |
| `image` | IMAGE | optionnel | Aucun | - | Image de référence optionnelle pour l'édition d'image. |
| `mask` | MASK | optionnel | Aucun | - | Masque optionnel pour l'inpainting (les zones blanches seront remplacées) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | L'image ou les images générées ou éditées par DALL·E 2 |