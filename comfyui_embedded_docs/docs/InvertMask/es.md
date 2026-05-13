> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InvertMask/es.md)

El nodo InvertMask está diseñado para invertir los valores de una máscara dada, intercambiando efectivamente las áreas enmascaradas y no enmascaradas. Esta operación es fundamental en tareas de procesamiento de imágenes donde es necesario cambiar el foco de interés entre el primer plano y el fondo.

## Entradas

| Parámetro | Tipo de dato | Descripción |
|-----------|--------------|-------------|
| `mask`    | MASK         | El parámetro `mask` representa la máscara de entrada que se va a invertir. Es crucial para determinar las áreas que se intercambiarán en el proceso de inversión. |

## Salidas

| Parámetro | Tipo de dato | Descripción |
|-----------|--------------|-------------|
| `mask`    | MASK         | La salida es una versión invertida de la máscara de entrada, donde las áreas previamente enmascaradas pasan a ser no enmascaradas y viceversa. |