> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3InfiniteStyleLibrary/fr.md)

Ce nœud vous permet de sélectionner un style dans la bibliothèque de styles infinis de Recraft en utilisant un UUID préexistant. Il récupère les informations du style en fonction de l'identifiant fourni et les retourne pour utilisation dans d'autres nœuds Recraft.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `style_id` | STRING | Oui | Tout UUID valide | UUID du style provenant de la bibliothèque de styles infinis. |

**Note :** L'entrée `style_id` ne peut pas être vide. Si une chaîne vide est fournie, le nœud générera une exception.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | L'objet style sélectionné provenant de la bibliothèque de styles infinis de Recraft |