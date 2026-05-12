> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemoveBackground/es.md)

## Descripción general

El nodo Remove Background utiliza un modelo de eliminación de fondo para generar una máscara que separa el sujeto en primer plano del fondo de una imagen de entrada. Toma una imagen y un modelo de eliminación de fondo, y produce una máscara que resalta el sujeto principal.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | N/A | Imagen de entrada a la que se le eliminará el fondo |
| `bg_removal_model` | BACKGROUND_REMOVAL_MODEL | Sí | N/A | Modelo de eliminación de fondo utilizado para generar la máscara |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `mask` | MASK | Máscara de primer plano generada que resalta el sujeto principal de la imagen de entrada |