> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringCompare/fr.md)

Voici la traduction de la documentation du nœud StringCompare :

Le nœud StringCompare compare deux chaînes de texte à l'aide de différentes méthodes de comparaison. Il peut vérifier si une chaîne commence par une autre, se termine par une autre, ou si les deux chaînes sont exactement égales. La comparaison peut être effectuée en tenant compte ou non des différences de casse.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `string_a` | STRING | Oui | - | La première chaîne à comparer |
| `string_b` | STRING | Oui | - | La deuxième chaîne à comparer |
| `mode` | COMBO | Oui | "Commence par"<br>"Se termine par"<br>"Égal" | La méthode de comparaison à utiliser (par défaut : "Commence par") |
| `case_sensitive` | BOOLEAN | Non | - | Indique s'il faut tenir compte de la casse lors de la comparaison (par défaut : true) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | BOOLEAN | Renvoie true si la condition de comparaison est remplie, false sinon |

---
**Source fingerprint (SHA-256):** `4491e4acd2c1881e9c924c6ae51d764dec5f46279094d173fe551e9ee9256597`
