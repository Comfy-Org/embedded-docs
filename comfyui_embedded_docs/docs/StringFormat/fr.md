Voici la traduction en français de la documentation du nœud ComfyUI, en respectant vos règles :

## Aperçu

Ce nœud formate du texte en utilisant la méthode de formatage de chaîne de Python. Il fonctionne comme un modèle où vous définissez un motif de texte avec des espaces réservés, puis fournissez des valeurs pour remplir ces espaces réservés. Il prend en charge toutes les options et fonctionnalités de formatage de Python.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `f_string` | Le modèle de chaîne de format avec des espaces réservés (par défaut : `{a}`). Prend en charge la saisie multiligne. | STRING | Oui | N/A |
| `values` | Entrée dynamique pour fournir des valeurs afin de remplir les espaces réservés dans la chaîne de format. Plusieurs entrées de valeurs peuvent être ajoutées selon les besoins. | STRING | Oui | N/A |

**Remarque sur l'entrée `values` :** Cette entrée est dynamique et peut être développée pour inclure plusieurs valeurs nommées. Chaque entrée de valeur est étiquetée avec une lettre (a, b, c, etc.) et correspond à un espace réservé dans la chaîne de format (par exemple, `{a}`, `{b}`, `{c}`). Vous pouvez ajouter ou supprimer des entrées de valeur selon vos besoins.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `STRING` | La chaîne de texte formatée avec tous les espaces réservés remplacés par leurs valeurs correspondantes. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringFormat/fr.md)

---
**Source fingerprint (SHA-256):** `72625287533829a8087687bb47f39bc265aced3d5f43066f615326d729725122`
