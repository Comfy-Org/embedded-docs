> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTemplateNode/fr.md)

Le nœud PixVerse Template vous permet de sélectionner parmi les modèles disponibles pour la génération de vidéos PixVerse. Il convertit le nom de modèle sélectionné en l'identifiant de modèle correspondant que l'API PixVerse requiert pour la création vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `modèle` | STRING | Oui | Plusieurs options disponibles | Le modèle à utiliser pour la génération de vidéos PixVerse. Les options disponibles correspondent aux modèles prédéfinis dans le système PixVerse. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `pixverse_template` | INT | L'identifiant de modèle correspondant au nom de modèle sélectionné, qui peut être utilisé par d'autres nœuds PixVerse pour la génération vidéo. |
