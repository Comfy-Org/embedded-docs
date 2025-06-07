Le nœud `ImageBlur` applique un flou gaussien à une image, permettant d'adoucir les bords et de réduire les détails et le bruit. Il offre un contrôle sur l'intensité et l'étendue du flou via des paramètres.

## Entrées

| Champ          | Data Type | Description                                                                   |
|----------------|-------------|-------------------------------------------------------------------------------|
| `image`        | `IMAGE`     | L'image d'entrée à flouter. C'est la cible principale de l'effet de flou. |
| `blur_radius`  | `INT`       | Détermine le rayon de l'effet de flou. Un rayon plus grand entraîne un flou plus prononcé. |
| `sigma`        | `FLOAT`     | Contrôle l'étendue du flou. Une valeur de sigma plus élevée signifie que le flou affectera une zone plus large autour de chaque pixel. |

## Sorties

| Champ | Data Type | Description                                                              |
|-------|-------------|--------------------------------------------------------------------------|
| `image`| `IMAGE`     | La sortie est la version floutée de l'image d'entrée, avec le degré de flou déterminé par les paramètres d'entrée. |
