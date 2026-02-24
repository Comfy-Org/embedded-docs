> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeTextLists/fr.md)

Ce nœud fusionne plusieurs listes de texte en une seule liste combinée. Il est conçu pour recevoir des entrées de texte sous forme de listes et les concaténer. Le nœud enregistre le nombre total de textes dans la liste fusionnée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `texts` | STRING | Oui | N/A | Les listes de texte à fusionner. Plusieurs listes peuvent être connectées à l'entrée, elles seront concaténées en une seule. |

**Note :** Ce nœud est configuré comme un processus de groupe (`is_group_process = True`), ce qui signifie qu'il traite automatiquement plusieurs entrées de liste en les concaténant avant l'exécution de la fonction de traitement principale.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `texts` | STRING | La liste unique et fusionnée contenant tous les textes d'entrée. |
