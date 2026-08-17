# AutogrowPrefixTestNode

Le nœud AutogrowPrefixTestNode est un nœud logique conçu pour tester la fonctionnalité d'entrée à croissance automatique. Il accepte un nombre dynamique d'entrées flottantes, combine leurs valeurs en une chaîne séparée par des virgules, et renvoie cette chaîne.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `autogrow` | Un groupe d'entrées dynamique qui accepte des valeurs flottantes. Le groupe peut contenir entre 1 et 10 entrées flottantes, et le nœud traite toutes les valeurs fournies. | FLOAT | Oui | 1 à 10 entrées |

**Remarque :** L'entrée `autogrow` est une entrée dynamique spéciale qui peut être développée pour ajouter davantage d'entrées flottantes jusqu'à un maximum de 10. Le minimum est de 1 entrée. Les valeurs `min` et `max` dans ce nœud définissent le nombre autorisé d'entrées dans le groupe, et non la plage de valeurs de chaque flottant individuel.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Une chaîne unique contenant toutes les valeurs flottantes d'entrée, séparées par des virgules. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/fr.md)

---
**Source fingerprint (SHA-256):** `9b815f59961a4c661815f44b9c78e15e9084db1e4be89d502b9d92438f18e70b`
