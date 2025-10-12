> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetModelHooksOnCond/fr.md)

Ce nœud attache des crochets personnalisés aux données de conditionnement, vous permettant d'intercepter et de modifier le processus de conditionnement pendant l'exécution du modèle. Il prend un ensemble de crochets et les applique aux données de conditionnement fournies, permettant une personnalisation avancée du flux de travail de génération texte-à-image. Le conditionnement modifié avec les crochets attachés est ensuite renvoyé pour être utilisé dans les étapes de traitement ultérieures.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | Oui | - | Les données de conditionnement auxquelles les crochets seront attachés |
| `hooks` | HOOKS | Oui | - | Les définitions de crochets qui seront appliquées aux données de conditionnement |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | Les données de conditionnement modifiées avec les crochets attachés |