Voici la traduction en français de la documentation technique du nœud ComfyUI :

Ce nœud est un test pour la fonctionnalité d'entrée Autogrow. Il accepte un nombre dynamique d'entrées flottantes, chacune étiquetée avec un nom spécifique, et combine leurs valeurs en une seule chaîne de caractères séparée par des virgules.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `autogrow` | Un groupe d'entrées dynamique. Vous pouvez ajouter plusieurs entrées flottantes, chacune avec un nom prédéfini parmi la liste : "a", "b" ou "c". Le nœud accepte toute combinaison de ces entrées nommées. | FLOAT | Oui | N/A |

**Remarque :** L'entrée `autogrow` est dynamique. Vous pouvez ajouter ou supprimer des entrées flottantes individuelles (nommées "a", "b" ou "c") selon les besoins de votre flux de travail. Le nœud traite toutes les valeurs fournies.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Une chaîne unique contenant les valeurs de toutes les entrées flottantes fournies, concaténées avec des virgules. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/fr.md)

---
**Source fingerprint (SHA-256):** `33e8b2e2c369d06979415c31ef2623cff55d98ecf49137c5cafbeba7cc3b0451`
