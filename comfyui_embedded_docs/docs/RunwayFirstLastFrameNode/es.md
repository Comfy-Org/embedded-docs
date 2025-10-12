> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/es.md)

El nodo Runway First-Last-Frame to Video genera videos cargando fotogramas clave iniciales y finales junto con un texto descriptivo. Crea transiciones suaves entre los fotogramas de inicio y fin proporcionados utilizando el modelo Gen-3 de Runway. Esto es particularmente útil para transiciones complejas donde el fotograma final difiere significativamente del fotograma inicial.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | N/A | Texto descriptivo para la generación (valor por defecto: cadena vacía) |
| `start_frame` | IMAGE | Sí | N/A | Fotograma inicial que se utilizará para el video |
| `end_frame` | IMAGE | Sí | N/A | Fotograma final que se utilizará para el video. Solo compatible con gen3a_turbo. |
| `duration` | COMBO | Sí | Múltiples opciones disponibles | Selección de duración del video entre las opciones de Duration disponibles |
| `ratio` | COMBO | Sí | Múltiples opciones disponibles | Selección de relación de aspecto entre las opciones RunwayGen3aAspectRatio disponibles |
| `seed` | INT | No | 0-4294967295 | Semilla aleatoria para la generación (valor por defecto: 0) |

**Restricciones de Parámetros:**

- El `prompt` debe contener al menos 1 carácter
- Tanto `start_frame` como `end_frame` deben tener dimensiones máximas de 7999x7999 píxeles
- Tanto `start_frame` como `end_frame` deben tener relaciones de aspecto entre 0.5 y 2.0
- El parámetro `end_frame` solo es compatible cuando se utiliza el modelo gen3a_turbo

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video generado que realiza la transición entre los fotogramas inicial y final |
