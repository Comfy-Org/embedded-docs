Le nœud ThresholdMask convertit un masque en un masque binaire en appliquant une valeur de seuil. Il compare chaque pixel du masque d'entrée à la valeur de seuil spécifiée et crée un nouveau masque où les pixels au-dessus du seuil deviennent 1 (blanc) et les pixels inférieurs ou égaux au seuil deviennent 0 (noir).

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `masque` | Le masque d'entrée à traiter | MASK | Oui | - |
| `valeur` | La valeur de seuil pour la binarisation (par défaut : 0,5) | FLOAT | Oui | 0,0 - 1,0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `masque` | Le masque binaire résultant après application du seuil | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ThresholdMask/fr.md)

---
**Source fingerprint (SHA-256):** `5c61433c05ef8106d928306b64035078e7598605512f20aaf992255f7b166456`
