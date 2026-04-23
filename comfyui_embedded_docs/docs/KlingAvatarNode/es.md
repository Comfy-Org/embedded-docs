> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingAvatarNode/es.md)

El nodo Kling Avatar 2.0 genera videos de humanos digitales con estilo de transmisión. Utiliza una única foto de referencia y un archivo de audio para crear un video de un avatar parlante. Se puede utilizar un texto de instrucción opcional para definir las acciones, emociones y movimientos de cámara del avatar.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | Imagen de referencia para el avatar. El ancho y la altura deben ser de al menos 300px. La relación de aspecto debe estar entre 1:2.5 y 2.5:1. |
| `sound_file` | AUDIO | Sí | - | Entrada de audio. Debe tener una duración entre 2 y 300 segundos. |
| `mode` | COMBO | Sí | `"std"`<br>`"pro"` | El modo de generación a utilizar. |
| `prompt` | STRING | No | - | Instrucción opcional para definir las acciones, emociones y movimientos de cámara del avatar. (valor por defecto: cadena vacía) |
| `seed` | INT | Sí | 0 a 2147483647 | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. (valor por defecto: 0) |

**Nota:** Las entradas `image` y `sound_file` tienen requisitos de validación específicos. La imagen debe tener al menos 300x300 píxeles con una relación de aspecto entre 1:2.5 y 2.5:1. El archivo de audio debe tener una duración entre 2 y 300 segundos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video del humano digital generado. |