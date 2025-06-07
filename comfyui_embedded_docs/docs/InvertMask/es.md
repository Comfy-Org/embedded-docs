El nodo InvertMask está diseñado para invertir los valores de una máscara dada, invirtiendo efectivamente las áreas enmascaradas y no enmascaradas. Esta operación es fundamental en tareas de procesamiento de imágenes donde el foco de interés necesita cambiarse entre el primer plano y el fondo.

## Entradas

| Parameter | Data Type | Description |
|-----------|--------------|-------------|
| `mask`    | MASK         | El parámetro 'mask' representa la máscara de entrada que se va a invertir. Es crucial para determinar las áreas que se invertirán en el proceso de inversión. |

## Salidas

| Parameter | Data Type | Description |
|-----------|--------------|-------------|
| `mask`    | MASK         | La salida es una versión invertida de la máscara de entrada, con áreas previamente enmascaradas que se vuelven no enmascaradas y viceversa. |
