Le nœud RegexMatch vérifie si une chaîne de texte contient une correspondance avec un motif d'expression régulière donné. Il recherche dans la chaîne d'entrée et renvoie un résultat simple oui/non indiquant si le motif a été trouvé dans le texte. Vous pouvez ajuster le fonctionnement de la recherche en activant des options comme la correspondance insensible à la casse ou le mode multiligne.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `chaîne` | La chaîne de texte dans laquelle rechercher des correspondances | STRING | Oui | - |
| `motif_regex` | Le motif d'expression régulière à comparer avec la chaîne | STRING | Oui | - |
| `insensible_à_la_casse` | Indique s'il faut ignorer la casse lors de la correspondance (par défaut : True) | BOOLEAN | Non | - |
| `multiligne` | Indique s'il faut activer le mode multiligne pour la correspondance regex (par défaut : False) | BOOLEAN | Non | - |
| `dotall` | Indique s'il faut activer le mode dotall pour la correspondance regex (par défaut : False) | BOOLEAN | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `correspondances` | Renvoie True si le motif regex correspond à une partie de la chaîne d'entrée, False sinon | BOOLEAN |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexMatch/fr.md)

---
**Source fingerprint (SHA-256):** `b0ee05277edd8600d880051aa33a940c01abc170553515ab02960f25b1aec2be`
