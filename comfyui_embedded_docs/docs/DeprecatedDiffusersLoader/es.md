El nodo Cargador de Difusores está diseñado para cargar modelos de la biblioteca de difusores, manejando específicamente la carga de modelos UNet, CLIP y VAE según las rutas de modelo proporcionadas. Facilita la integración de estos modelos en el marco de ComfyUI, habilitando funcionalidades avanzadas como la generación de imágenes a partir de texto, manipulación de imágenes y más.

## Entradas

| Parámetro    | Tipo de Dato | Descripción |
|--------------|--------------|-------------|
| `model_path` | COMBO[STRING] | Especifica la ruta al modelo que se va a cargar. Esta ruta es crucial ya que determina qué modelo se utilizará para las operaciones posteriores, afectando la salida y las capacidades del nodo. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `model`   | MODEL     | El modelo UNet cargado, que es parte de la tupla de salida. Este modelo es esencial para tareas de síntesis y manipulación de imágenes dentro del marco de ComfyUI. |
| `clip`    | CLIP      | El modelo CLIP cargado, incluido en la tupla de salida si se solicita. Este modelo permite capacidades avanzadas de comprensión y manipulación de texto e imágenes. |
| `vae`     | VAE       | El modelo VAE cargado, incluido en la tupla de salida si se solicita. Este modelo es crucial para tareas que implican manipulación del espacio latente y generación de imágenes.
