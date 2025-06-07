Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/clip_vision`, y también leerá los modelos de las rutas adicionales que hayas configurado en el archivo extra_model_paths.yaml. A veces, es posible que necesites **refrescar la interfaz de ComfyUI** para que pueda leer los archivos de modelo en la carpeta correspondiente.

El nodo CLIPVisionLoader está diseñado para cargar modelos de Visión CLIP desde rutas especificadas. Abstrae las complejidades de localizar e inicializar modelos de Visión CLIP, haciéndolos fácilmente disponibles para tareas de procesamiento o inferencia adicionales.

## Entradas

| Campo       | Comfy dtype | Descripción                                                                       |
|-------------|-------------|-----------------------------------------------------------------------------------|
| `clip_name` | `COMBO[STRING]` | Especifica el nombre del modelo de Visión CLIP a cargar, utilizado para localizar el archivo del modelo dentro de una estructura de directorios predefinida. |

## Salidas

| Campo          | Comfy dtype     | Descripción                                                              |
|----------------|-----------------|--------------------------------------------------------------------------|
| `clip_vision`  | `CLIP_VISION`   | El modelo de Visión CLIP cargado, listo para su uso en la codificación de imágenes o en la realización de otras tareas relacionadas con la visión. |
