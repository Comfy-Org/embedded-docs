> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/fr.md)

Le nœud Adjust Brightness modifie la luminosité d'une image d'entrée. Il fonctionne en multipliant la valeur de chaque pixel par un facteur spécifié, puis en s'assurant que les valeurs résultantes restent dans une plage valide. Un facteur de 1.0 laisse l'image inchangée, les valeurs inférieures à 1.0 l'assombrissent et les valeurs supérieures à 1.0 l'éclaircissent.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à ajuster. |
| `factor` | FLOAT | Non | 0.0 - 2.0 | Facteur de luminosité. 1.0 = pas de changement, <1.0 = plus sombre, >1.0 = plus clair. (par défaut : 1.0) |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image de sortie avec la luminosité ajustée. |
