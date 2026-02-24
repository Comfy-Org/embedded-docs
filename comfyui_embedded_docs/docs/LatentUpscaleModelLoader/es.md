> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/es.md)

El nodo LatentUpscaleModelLoader carga un modelo especializado diseñado para aumentar la escala de representaciones latentes. Lee un archivo de modelo desde la carpeta designada del sistema y detecta automáticamente su tipo (720p, 1080p u otro) para instanciar y configurar la arquitectura de modelo interna correcta. El modelo cargado queda listo para ser utilizado por otros nodos en tareas de super-resolución en el espacio latente.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model_name` | STRING | Sí | *Todos los archivos en la carpeta `latent_upscale_models`* | El nombre del archivo del modelo de aumento de escala latente a cargar. Las opciones disponibles se completan dinámicamente a partir de los archivos presentes en el directorio `latent_upscale_models` de tu ComfyUI. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | LATENT_UPSCALE_MODEL | El modelo de aumento de escala latente cargado, configurado y listo para usar. |
