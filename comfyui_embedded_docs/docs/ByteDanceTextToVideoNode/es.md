> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/es.md)

El nodo ByteDance Text to Video genera videos utilizando modelos de ByteDance a través de una API basada en indicaciones de texto. Toma una descripción textual y varias configuraciones de video como entrada, y luego crea un video que coincide con las especificaciones proporcionadas. El nodo maneja la comunicación con la API y devuelve el video generado como salida.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | STRING | Combo | seedance_1_pro | Opciones de Text2VideoModelName | Nombre del modelo |
| `prompt` | STRING | String | - | - | La indicación de texto utilizada para generar el video. |
| `resolution` | STRING | Combo | - | ["480p", "720p", "1080p"] | La resolución del video de salida. |
| `aspect_ratio` | STRING | Combo | - | ["16:9", "4:3", "1:1", "3:4", "9:16", "21:9"] | La relación de aspecto del video de salida. |
| `duration` | INT | Int | 5 | 3-12 | La duración del video de salida en segundos. |
| `seed` | INT | Int | 0 | 0-2147483647 | Semilla a utilizar para la generación. (Opcional) |
| `camera_fixed` | BOOLEAN | Boolean | False | - | Especifica si se debe fijar la cámara. La plataforma añade una instrucción para fijar la cámara a su indicación, pero no garantiza el efecto real. (Opcional) |
| `watermark` | BOOLEAN | Boolean | True | - | Si se debe agregar una marca de agua de "Generado por IA" al video. (Opcional) |

**Restricciones de Parámetros:**

- El parámetro `prompt` debe contener al menos 1 carácter después de la eliminación de espacios en blanco
- El parámetro `prompt` no puede contener los siguientes parámetros de texto: "resolution", "ratio", "duration", "seed", "camerafixed", "watermark"
- El parámetro `duration` está limitado a valores entre 3 y 12 segundos
- El parámetro `seed` acepta valores de 0 a 2,147,483,647

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado |
