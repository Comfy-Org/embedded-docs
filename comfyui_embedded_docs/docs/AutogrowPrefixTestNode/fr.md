> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/fr.md)

Le nœud AutogrowPrefixTestNode est un nœud logique conçu pour tester la fonctionnalité d'entrée à croissance automatique (autogrow). Il accepte un nombre dynamique d'entrées de type float, combine leurs valeurs en une chaîne de caractères séparée par des virgules, et renvoie cette chaîne en sortie.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `autogrow` | AUTOGROW | Oui | 1 à 10 entrées | Un groupe d'entrées dynamique qui peut accepter entre 1 et 10 valeurs de type float. Chaque entrée dans ce groupe est de type FLOAT. |

**Note :** L'entrée `autogrow` est une entrée dynamique spéciale. Vous pouvez ajouter plusieurs entrées de type float à ce groupe, jusqu'à un maximum de 10. Le nœud traitera toutes les valeurs fournies.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | STRING | Une chaîne de caractères unique contenant toutes les valeurs d'entrée de type float, séparées par des virgules. |
