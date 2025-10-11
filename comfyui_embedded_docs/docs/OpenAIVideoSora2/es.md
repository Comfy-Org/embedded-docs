> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIVideoSora2/es.md)

El nodo OpenAIVideoSora2 genera videos utilizando los modelos Sora de OpenAI. Crea contenido de video basado en indicaciones de texto e imágenes de entrada opcionales, y luego devuelve el video generado. El nodo admite diferentes duraciones y resoluciones de video según el modelo seleccionado.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | "sora-2"<br>"sora-2-pro" | El modelo OpenAI Sora a utilizar para la generación de video (predeterminado: "sora-2") |
| `prompt` | STRING | Sí | - | Texto guía; puede estar vacío si hay una imagen de entrada presente (predeterminado: vacío) |
| `size` | COMBO | Sí | "720x1280"<br>"1280x720"<br>"1024x1792"<br>"1792x1024" | La resolución para el video generado (predeterminado: "1280x720") |
| `duration` | COMBO | Sí | 4<br>8<br>12 | La duración del video generado en segundos (predeterminado: 8) |
| `image` | IMAGE | No | - | Imagen de entrada opcional para la generación de video |
| `seed` | INT | No | 0 a 2147483647 | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (predeterminado: 0) |

**Restricciones y Limitaciones:**
- El modelo "sora-2" solo admite resoluciones "720x1280" y "1280x720"
- Solo se admite una imagen de entrada cuando se utiliza el parámetro image
- Los resultados son no deterministas independientemente del valor de la semilla

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | La salida de video generada |