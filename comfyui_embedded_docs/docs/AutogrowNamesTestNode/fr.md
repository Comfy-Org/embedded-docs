> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/fr.md)

Ce nœud est un test pour la fonctionnalité d'entrée Autogrow. Il accepte un nombre dynamique d'entrées de type FLOAT, chacune étiquetée avec un nom spécifique, et combine leurs valeurs en une seule chaîne de caractères séparée par des virgules.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `autogrow` | FLOAT | Oui | N/A | Un groupe d'entrées dynamique. Vous pouvez ajouter plusieurs entrées de type FLOAT, chacune avec un nom prédéfini dans la liste : "a", "b" ou "c". Le nœud acceptera n'importe quelle combinaison de ces entrées nommées. |

**Note :** L'entrée `autogrow` est dynamique. Vous pouvez ajouter ou supprimer des entrées individuelles de type FLOAT (nommées "a", "b" ou "c") selon les besoins de votre flux de travail. Le nœud traite toutes les valeurs fournies.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | STRING | Une chaîne de caractères unique contenant les valeurs de toutes les entrées FLOAT fournies, jointes par des virgules. |
