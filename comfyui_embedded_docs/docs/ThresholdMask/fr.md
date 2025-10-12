> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ThresholdMask/fr.md)

Le nœud ThresholdMask convertit un masque en masque binaire en appliquant une valeur de seuil. Il compare chaque pixel du masque d'entrée avec la valeur de seuil spécifiée et crée un nouveau masque où les pixels au-dessus du seuil deviennent 1 (blanc) et les pixels en dessous ou égaux au seuil deviennent 0 (noir).

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `masque` | MASK | Oui | - | Le masque d'entrée à traiter |
| `valeur` | FLOAT | Oui | 0.0 - 1.0 | La valeur de seuil pour la binarisation (par défaut : 0.5) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `masque` | MASK | Le masque binaire résultant après application du seuil |
