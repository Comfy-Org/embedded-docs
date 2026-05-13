> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlur/fr.md)

Le nœud `ImageBlur` applique un flou gaussien à une image, permettant d'adoucir les contours et de réduire les détails et le bruit. Il offre un contrôle sur l'intensité et l'étendue du flou via ses paramètres.

## Entrées

| Champ          | Type de données | Description                                                                   |
|----------------|-----------------|-------------------------------------------------------------------------------|
| `image`        | `IMAGE`         | L'image d'entrée à flouter. C'est la cible principale de l'effet de flou.     |
| `rayon_flou`  | `INT`           | Détermine le rayon de l'effet de flou. Un rayon plus important produit un flou plus prononcé. |
| `sigma`        | `FLOAT`         | Contrôle l'étendue du flou. Une valeur sigma plus élevée signifie que le flou affectera une zone plus large autour de chaque pixel. |

## Sorties

| Champ | Type de données | Description                                                              |
|-------|-----------------|--------------------------------------------------------------------------|
| `image`| `IMAGE`         | La sortie est la version floutée de l'image d'entrée, dont le degré de flou est déterminé par les paramètres d'entrée. |