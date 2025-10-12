> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaVideoNode/es.md)

Genera videos de forma síncrona basándose en el prompt y la configuración de salida. Este nodo crea contenido de video utilizando descripciones de texto y varios parámetros de generación, produciendo el video final una vez que el proceso de generación se completa.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Prompt para la generación del video (valor por defecto: cadena vacía) |
| `modelo` | COMBO | Sí | Múltiples opciones disponibles | El modelo de generación de video a utilizar |
| `relación de aspecto` | COMBO | Sí | Múltiples opciones disponibles | La relación de aspecto para el video generado (valor por defecto: 16:9) |
| `resolución` | COMBO | Sí | Múltiples opciones disponibles | La resolución de salida para el video (valor por defecto: 540p) |
| `duración` | COMBO | Sí | Múltiples opciones disponibles | La duración del video generado |
| `bucle` | BOOLEAN | Sí | - | Si el video debe reproducirse en bucle (valor por defecto: False) |
| `semilla` | INT | Sí | 0 a 18446744073709551615 | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (valor por defecto: 0) |
| `luma_concepts` | CUSTOM | No | - | Conceptos de Cámara opcionales para dictar el movimiento de cámara a través del nodo Luma Concepts |

**Nota:** Cuando se utiliza el modelo `ray_1_6`, los parámetros `duration` y `resolution` se establecen automáticamente en None y no afectan la generación.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado |
