> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFlip/fr.md)

Le nœud ImageFlip retourne les images selon différents axes. Il peut retourner les images verticalement le long de l'axe des x ou horizontalement le long de l'axe des y. Le nœud utilise des opérations torch.flip pour effectuer le retournement en fonction de la méthode sélectionnée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à retourner |
| `flip_method` | STRING | Oui | "x-axis: vertically"<br>"y-axis: horizontally" | La direction de retournement à appliquer |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image de sortie retournée |