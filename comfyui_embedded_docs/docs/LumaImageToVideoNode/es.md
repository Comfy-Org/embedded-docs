> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageToVideoNode/es.md)

Genera videos de forma síncrona basándose en prompts, imágenes de entrada y tamaño de salida. Este nodo crea videos utilizando la API de Luma proporcionando prompts de texto e imágenes opcionales de inicio/fin para definir el contenido y estructura del video.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Prompt para la generación del video (por defecto: "") |
| `model` | COMBO | Sí | Múltiples opciones disponibles | Selecciona el modelo de generación de video entre los modelos Luma disponibles |
| `resolución` | COMBO | Sí | Múltiples opciones disponibles | Resolución de salida para el video generado (por defecto: 540p) |
| `duración` | COMBO | Sí | Múltiples opciones disponibles | Duración del video generado |
| `bucle` | BOOLEAN | Sí | - | Si el video generado debe reproducirse en bucle (por defecto: False) |
| `semilla` | INT | Sí | 0 a 18446744073709551615 | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no determinísticos independientemente de la semilla. (por defecto: 0) |
| `primera_imagen` | IMAGE | No | - | Primer fotograma del video generado. (opcional) |
| `última_imagen` | IMAGE | No | - | Último fotograma del video generado. (opcional) |
| `luma_concepts` | CUSTOM | No | - | Conceptos de Cámara opcionales para dictar el movimiento de cámara a través del nodo Luma Concepts. (opcional) |

**Nota:** Se debe proporcionar al menos uno de los parámetros `first_image` o `last_image`. El nodo generará una excepción si faltan ambos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado |