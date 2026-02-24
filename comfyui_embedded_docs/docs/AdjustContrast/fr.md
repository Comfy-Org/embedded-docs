> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustContrast/fr.md)

Le nœud Adjust Contrast modifie le niveau de contraste d'une image d'entrée. Il fonctionne en ajustant la différence entre les zones claires et sombres de l'image. Un facteur de 1.0 laisse l'image inchangée, les valeurs inférieures à 1.0 réduisent le contraste et les valeurs supérieures à 1.0 l'augmentent.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée dont le contraste doit être ajusté. |
| `factor` | FLOAT | Non | 0.0 - 2.0 | Facteur de contraste. 1.0 = aucun changement, <1.0 = moins de contraste, >1.0 = plus de contraste. (par défaut : 1.0) |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image résultante avec le contraste ajusté. |
