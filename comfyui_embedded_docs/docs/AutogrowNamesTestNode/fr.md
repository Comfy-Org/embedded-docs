> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/fr.md)

Voici la traduction en français de la documentation technique du nœud ComfyUI :

Ce nœud est un test pour la fonctionnalité d'entrée Autogrow. Il accepte un nombre dynamique d'entrées flottantes, chacune étiquetée avec un nom spécifique, et combine leurs valeurs en une seule chaîne de caractères séparée par des virgules.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `autogrow` | FLOAT | Oui | N/A | Un groupe d'entrées dynamique. Vous pouvez ajouter plusieurs entrées flottantes, chacune avec un nom prédéfini parmi la liste : "a", "b" ou "c". Le nœud accepte toute combinaison de ces entrées nommées. |

**Remarque :** L'entrée `autogrow` est dynamique. Vous pouvez ajouter ou supprimer des entrées flottantes individuelles (nommées "a", "b" ou "c") selon les besoins de votre flux de travail. Le nœud traite toutes les valeurs fournies.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | STRING | Une chaîne unique contenant les valeurs de toutes les entrées flottantes fournies, concaténées avec des virgules. |

---
**Source fingerprint (SHA-256):** `33e8b2e2c369d06979415c31ef2623cff55d98ecf49137c5cafbeba7cc3b0451`
