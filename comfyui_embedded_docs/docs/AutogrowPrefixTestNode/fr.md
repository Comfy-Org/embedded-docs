# AutogrowPrefixTestNode

Le nœud AutogrowPrefixTestNode est un nœud logique qui teste la fonctionnalité d'entrée à croissance automatique (autogrow). Il accepte un nombre dynamique d'entrées flottantes, convertit chaque valeur en texte, les combine en une chaîne séparée par des virgules, puis sort cette chaîne.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `autogrow` | Un groupe d'entrées dynamique qui accepte entre 1 et 10 valeurs flottantes. Chaque valeur est un nombre à virgule flottante, et les entrées générées sont nommées avec le préfixe `float`. | AUTOGROW | Oui | 1 à 10 entrées |

**Remarque :** L'entrée `autogrow` est une entrée dynamique spéciale. Vous pouvez ajouter plusieurs entrées flottantes à ce groupe, d'un minimum de 1 jusqu'à un maximum de 10. Le nœud traite toutes les valeurs fournies et inclut chaque entrée connectée dans la chaîne de sortie.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Une chaîne unique contenant toutes les valeurs flottantes d'entrée, séparées par des virgules. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/fr.md)

---
**Source fingerprint (SHA-256):** `9b815f59961a4c661815f44b9c78e15e9084db1e4be89d502b9d92438f18e70b`
