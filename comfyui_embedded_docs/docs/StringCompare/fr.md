Voici la traduction de la documentation du nœud StringCompare :

Le nœud StringCompare compare deux chaînes de texte à l'aide de différentes méthodes de comparaison. Il peut vérifier si une chaîne commence par une autre, se termine par une autre, ou si les deux chaînes sont exactement égales. La comparaison peut être effectuée en tenant compte ou non des différences de casse.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `chaîne_a` | La première chaîne à comparer | STRING | Oui | - |
| `chaîne_b` | La deuxième chaîne à comparer | STRING | Oui | - |
| `mode` | La méthode de comparaison à utiliser (par défaut : "Commence par") | COMBO | Oui | "Commence par"<br>"Se termine par"<br>"Égal" |
| `sensible_casse` | Indique s'il faut tenir compte de la casse lors de la comparaison (par défaut : true) | BOOLEAN | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Renvoie true si la condition de comparaison est remplie, false sinon | BOOLEAN |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringCompare/fr.md)

---
**Source fingerprint (SHA-256):** `4491e4acd2c1881e9c924c6ae51d764dec5f46279094d173fe551e9ee9256597`
