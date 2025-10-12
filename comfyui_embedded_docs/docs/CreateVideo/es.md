> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/es.md)

El nodo Create Video genera un archivo de video a partir de una secuencia de imágenes. Puedes especificar la velocidad de reproducción usando fotogramas por segundo y opcionalmente añadir audio al video. El nodo combina tus imágenes en un formato de video que puede reproducirse con la velocidad de fotogramas especificada.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imágenes` | IMAGE | Sí | - | Las imágenes a partir de las cuales crear un video. |
| `fps` | FLOAT | Sí | 1.0 - 120.0 | Los fotogramas por segundo para la velocidad de reproducción del video (valor por defecto: 30.0). |
| `audio` | AUDIO | No | - | El audio para añadir al video. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado que contiene las imágenes de entrada y el audio opcional. |
