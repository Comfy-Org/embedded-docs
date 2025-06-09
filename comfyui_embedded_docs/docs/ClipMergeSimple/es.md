Este nodo se especializa en fusionar dos modelos CLIP basándose en una proporción especificada, combinando efectivamente sus características. Aplica selectivamente parches de un modelo a otro, excluyendo componentes específicos como los IDs de posición y la escala de logit, para crear un modelo híbrido que combina características de ambos modelos fuente.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `clip1`   | `CLIP`      | El primer modelo CLIP que se va a fusionar. Sirve como el modelo base para el proceso de fusión. |
| `clip2`   | `CLIP`      | El segundo modelo CLIP que se va a fusionar. Sus parches clave, excepto los IDs de posición y la escala de logit, se aplican al primer modelo según la proporción especificada. |
| `ratio`   | `FLOAT`     | Determina la proporción de características del segundo modelo que se fusionarán en el primer modelo. Una proporción de 1.0 significa adoptar completamente las características del segundo modelo, mientras que 0.0 retiene solo las características del primer modelo. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `clip`    | CLIP      | El modelo CLIP resultante de la fusión, que incorpora características de ambos modelos de entrada según la proporción especificada. |
