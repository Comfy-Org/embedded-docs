> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduImageToVideoNode/es.md)

El nodo Generación de Video a partir de Imagen Vidu crea videos a partir de una imagen inicial y una descripción de texto opcional. Utiliza modelos de IA para generar contenido de video que se extiende desde el fotograma de imagen proporcionado. El nodo envía la imagen y los parámetros a un servicio externo y devuelve el video generado.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | `vidu_q1`<br>*Otras opciones de VideoModelName* | Nombre del modelo (por defecto: vidu_q1) |
| `image` | IMAGE | Sí | - | Una imagen que se utilizará como fotograma inicial del video generado |
| `prompt` | STRING | No | - | Una descripción textual para la generación de video (por defecto: vacío) |
| `duration` | INT | No | 5-5 | Duración del video de salida en segundos (por defecto: 5, fijado en 5 segundos) |
| `seed` | INT | No | 0-2147483647 | Semilla para la generación de video (0 para aleatorio) (por defecto: 0) |
| `resolution` | COMBO | No | `r_1080p`<br>*Otras opciones de Resolution* | Los valores admitidos pueden variar según el modelo y la duración (por defecto: r_1080p) |
| `movement_amplitude` | COMBO | No | `auto`<br>*Otras opciones de MovementAmplitude* | La amplitud de movimiento de los objetos en el fotograma (por defecto: auto) |

**Restricciones:**

- Solo se permite una imagen de entrada (no puede procesar múltiples imágenes)
- La imagen de entrada debe tener una relación de aspecto entre 1:4 y 4:1

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | La salida de video generada |
