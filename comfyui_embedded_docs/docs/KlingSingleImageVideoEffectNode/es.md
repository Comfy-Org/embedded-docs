> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingSingleImageVideoEffectNode/es.md)

El nodo Kling Single Image Video Effect crea videos con diferentes efectos especiales basados en una única imagen de referencia. Aplica varios efectos visuales y escenas para transformar imágenes estáticas en contenido de video dinámico. El nodo admite diferentes escenas de efectos, opciones de modelos y duraciones de video para lograr el resultado visual deseado.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen` | IMAGE | Sí | - | Imagen de referencia. URL o cadena codificada en Base64 (sin el prefijo data:image). El tamaño del archivo no puede exceder 10MB, la resolución no debe ser inferior a 300*300px, relación de aspecto entre 1:2.5 ~ 2.5:1 |
| `effect_scene` | COMBO | Sí | Opciones de KlingSingleImageEffectsScene | El tipo de escena de efecto especial a aplicar en la generación del video |
| `model_name` | COMBO | Sí | Opciones de KlingSingleImageEffectModelName | El modelo específico a utilizar para generar el efecto de video |
| `duración` | COMBO | Sí | Opciones de KlingVideoGenDuration | La duración del video generado |

**Nota:** Las opciones específicas para `effect_scene`, `model_name` y `duration` están determinadas por los valores disponibles en sus respectivas clases de enumeración (KlingSingleImageEffectsScene, KlingSingleImageEffectModelName y KlingVideoGenDuration).

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `video_id` | VIDEO | El video generado con los efectos aplicados |
| `duración` | STRING | El identificador único para el video generado |
| `duración` | STRING | La duración del video generado |