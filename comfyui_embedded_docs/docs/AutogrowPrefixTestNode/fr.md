# AutogrowPrefixTestNode

Le nœud AutogrowPrefixTestNode est un nœud logique conçu pour tester la fonctionnalité d'entrée à croissance automatique. Il accepte un nombre dynamique d'entrées flottantes, combine leurs valeurs en une chaîne séparée par des virgules, et produit cette chaîne en sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `autogrow` | Un groupe d'entrées dynamique pouvant accepter entre 1 et 10 valeurs flottantes. Chaque entrée du groupe est de type FLOAT avec une valeur minimale de 1 et une valeur maximale de 10. | AUTOGROW | Oui | 1 à 10 entrées |

**Remarque :** L'entrée `autogrow` est une entrée dynamique spéciale. Vous pouvez ajouter plusieurs entrées flottantes à ce groupe, jusqu'à un maximum de 10. Le nœud traitera toutes les valeurs fournies. Chaque entrée flottante individuelle est limitée à une plage de 1 à 10.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Une chaîne unique contenant toutes les valeurs d'entrée flottantes, séparées par des virgules. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/fr.md)

---
**Source fingerprint (SHA-256):** `7ae65365f77399a2ad8358b5a1eab3f2caa39331e53dec474cdd7f2751bfff4b`
