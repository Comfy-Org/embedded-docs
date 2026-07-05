# Fusionner les listes de textes

Voici la traduction en français de la documentation du nœud ComfyUI :

Ce nœud fusionne plusieurs listes de textes en une seule liste combinée. Il est conçu pour recevoir des entrées textuelles sous forme de listes et les concatène ensemble. Le nœud enregistre le nombre total de textes dans la liste fusionnée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `textes` | Les listes de textes à fusionner. Plusieurs listes peuvent être connectées à l'entrée, et elles seront concaténées en une seule. | STRING | Oui | N/D |

**Remarque :** Ce nœud est configuré comme un processus de groupe (`is_group_process = True`), ce qui signifie qu'il gère automatiquement plusieurs entrées de listes en les concaténant avant l'exécution de la fonction de traitement principale.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `textes` | La liste unique et fusionnée contenant tous les textes d'entrée. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeTextLists/fr.md)

---
**Source fingerprint (SHA-256):** `043a39a373d03f1ff79dd0746070171bab4d5d915c985e4e64fd35f802b09f69`
