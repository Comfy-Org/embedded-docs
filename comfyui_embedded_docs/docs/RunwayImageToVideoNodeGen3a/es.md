> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/es.md)

El nodo Runway Image to Video (Gen3a Turbo) genera un video a partir de una única imagen inicial utilizando el modelo Gen3a Turbo de Runway. Toma un texto descriptivo y una imagen de inicio, luego crea una secuencia de video basada en la duración y relación de aspecto especificadas. Este nodo se conecta a la API de Runway para procesar la generación de forma remota.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | N/A | Texto descriptivo para la generación (valor por defecto: "") |
| `start_frame` | IMAGE | Sí | N/A | Imagen de inicio que se utilizará para el video |
| `duration` | COMBO | Sí | Múltiples opciones disponibles | Selección de duración del video entre las opciones disponibles |
| `ratio` | COMBO | Sí | Múltiples opciones disponibles | Selección de relación de aspecto entre las opciones disponibles |
| `seed` | INT | No | 0-4294967295 | Semilla aleatoria para la generación (valor por defecto: 0) |

**Restricciones de Parámetros:**
- El `start_frame` debe tener dimensiones que no excedan 7999x7999 píxeles
- El `start_frame` debe tener una relación de aspecto entre 0.5 y 2.0
- El `prompt` debe contener al menos un carácter (no puede estar vacío)

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | La secuencia de video generada |