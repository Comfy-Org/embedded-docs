Le nœud StringSubstring extrait une portion de texte d'une chaîne de caractères plus longue. Il utilise une position de début et une position de fin pour définir la section à extraire, puis retourne le texte situé entre ces deux positions.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `chaîne` | La chaîne de texte d'entrée à partir de laquelle extraire. Prend en charge le texte multi-lignes. | STRING | Oui | - |
| `début` | L'indice de position de début pour la sous-chaîne. Le premier caractère se trouve à l'indice 0. | INT | Oui | - |
| `fin` | L'indice de position de fin pour la sous-chaîne. Le caractère à cet indice n'est pas inclus dans le résultat. | INT | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La sous-chaîne extraite du texte d'entrée, contenant tous les caractères de la position `début` jusqu'à (mais sans inclure) la position `fin`. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringSubstring/fr.md)

---
**Source fingerprint (SHA-256):** `962d0b19af88b6c95b5c9d374081ecd55ee8cffbfb638de7ed38e6e378b220c5`
