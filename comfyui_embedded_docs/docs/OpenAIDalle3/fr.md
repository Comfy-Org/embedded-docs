> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle3/fr.md)

Génère des images de manière synchrone via le point de terminaison DALL·E 3 d'OpenAI. Ce nœud prend une invite textuelle et crée des images correspondantes en utilisant le modèle DALL·E 3 d'OpenAI, vous permettant de spécifier la qualité, le style et les dimensions de l'image.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Invite textuelle pour DALL·E (par défaut : "") |
| `seed` | INT | Non | 0 à 2147483647 | pas encore implémenté dans le backend (par défaut : 0) |
| `qualité` | COMBO | Non | "standard"<br>"hd" | Qualité de l'image (par défaut : "standard") |
| `style` | COMBO | Non | "natural"<br>"vivid" | Vivid amène le modèle à privilégier la génération d'images hyper-réalistes et dramatiques. Natural amène le modèle à produire des images plus naturelles, moins hyper-réalistes. (par défaut : "natural") |
| `taille` | COMBO | Non | "1024x1024"<br>"1024x1792"<br>"1792x1024" | Dimensions de l'image (par défaut : "1024x1024") |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | L'image générée par DALL·E 3 |
