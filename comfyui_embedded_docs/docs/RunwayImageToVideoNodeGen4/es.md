> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen4/es.md)

El nodo Runway Image to Video (Gen4 Turbo) genera un video a partir de una única imagen inicial utilizando el modelo Gen4 Turbo de Runway. Toma un texto descriptivo y una imagen de inicio, luego crea una secuencia de video basada en la duración y relación de aspecto proporcionadas. El nodo maneja la carga de la imagen inicial a la API de Runway y devuelve el video generado.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Texto descriptivo para la generación (valor por defecto: cadena vacía) |
| `start_frame` | IMAGE | Sí | - | Imagen de inicio que se utilizará para el video |
| `duration` | COMBO | Sí | Múltiples opciones disponibles | Selección de duración del video entre las opciones de duración disponibles |
| `ratio` | COMBO | Sí | Múltiples opciones disponibles | Selección de relación de aspecto entre las opciones disponibles para Gen4 Turbo |
| `seed` | INT | No | 0 a 4294967295 | Semilla aleatoria para la generación (valor por defecto: 0) |

**Restricciones de Parámetros:**
- La imagen `start_frame` debe tener dimensiones que no excedan 7999x7999 píxeles
- La imagen `start_frame` debe tener una relación de aspecto entre 0.5 y 2.0
- El `prompt` debe contener al menos un carácter

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video generado basado en la imagen de entrada y el texto descriptivo |