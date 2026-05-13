> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DeprecatedDiffusersLoader/es.md)

El nodo DiffusersLoader está diseñado para cargar modelos de la biblioteca diffusers, manejando específicamente la carga de modelos UNet, CLIP y VAE basándose en las rutas de modelo proporcionadas. Facilita la integración de estos modelos en el marco de ComfyUI, permitiendo funcionalidades avanzadas como generación de texto a imagen, manipulación de imágenes y más.

## Entradas

| Parámetro     | Tipo de Dato | Descripción |
|--------------|--------------|-------------|
| `model_path` | COMBO[STRING] | Especifica la ruta al modelo que se cargará. Esta ruta es crucial, ya que determina qué modelo se utilizará para operaciones posteriores, afectando la salida y las capacidades del nodo. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `model`   | MODEL     | El modelo UNet cargado, que forma parte de la tupla de salida. Este modelo es esencial para tareas de síntesis y manipulación de imágenes dentro del marco de ComfyUI. |
| `clip`    | CLIP      | El modelo CLIP cargado, incluido en la tupla de salida si se solicita. Este modelo permite capacidades avanzadas de comprensión y manipulación de texto e imágenes. |
| `vae`     | VAE       | El modelo VAE cargado, incluido en la tupla de salida si se solicita. Este modelo es crucial para tareas que implican manipulación del espacio latente y generación de imágenes. |