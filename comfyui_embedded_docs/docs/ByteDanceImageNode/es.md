> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageNode/es.md)

El nodo ByteDance Image genera imágenes utilizando modelos de ByteDance a través de una API basada en indicaciones de texto. Permite seleccionar diferentes modelos, especificar dimensiones de imagen y controlar varios parámetros de generación como semilla y escala de guía. El nodo se conecta al servicio de generación de imágenes de ByteDance y devuelve la imagen creada.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seedream_3 | Opciones de Text2ImageModelName | Nombre del modelo |
| `prompt` | STRING | STRING | - | - | La indicación de texto utilizada para generar la imagen |
| `size_preset` | STRING | COMBO | - | Etiquetas de RECOMMENDED_PRESETS | Selecciona un tamaño recomendado. Elige Personalizado para usar el ancho y alto a continuación |
| `width` | INT | INT | 1024 | 512-2048 (paso 64) | Ancho personalizado para la imagen. El valor solo funciona si `size_preset` está establecido en `Custom` |
| `height` | INT | INT | 1024 | 512-2048 (paso 64) | Alto personalizado para la imagen. El valor solo funciona si `size_preset` está establecido en `Custom` |
| `seed` | INT | INT | 0 | 0-2147483647 (paso 1) | Semilla a utilizar para la generación (opcional) |
| `guidance_scale` | FLOAT | FLOAT | 2.5 | 1.0-10.0 (paso 0.01) | Un valor más alto hace que la imagen siga la indicación más estrechamente (opcional) |
| `watermark` | BOOLEAN | BOOLEAN | True | - | Si añadir una marca de agua de "Generado por IA" a la imagen (opcional) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | La imagen generada desde la API de ByteDance |
