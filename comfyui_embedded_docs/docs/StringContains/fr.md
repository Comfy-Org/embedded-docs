Le nœud StringContains vérifie si une chaîne de caractères donnée contient une sous-chaîne spécifiée. Il peut effectuer cette vérification avec une correspondance sensible à la casse ou insensible à la casse, renvoyant un résultat booléen indiquant si la sous-chaîne a été trouvée dans la chaîne principale.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `chaîne` | La chaîne de texte principale dans laquelle effectuer la recherche | STRING | Oui | - |
| `sous-chaîne` | Le texte à rechercher dans la chaîne principale | STRING | Oui | - |
| `sensible_à_la_casse` | Détermine si la recherche doit être sensible à la casse (par défaut : true) | BOOLEAN | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `contains` | Renvoie true si la sous-chaîne est trouvée dans la chaîne, false sinon | BOOLEAN |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringContains/fr.md)

---
**Source fingerprint (SHA-256):** `ef7329ca8586e0f894306d93835490edb948a346db1e0cb011e4da5a6fe44202`
