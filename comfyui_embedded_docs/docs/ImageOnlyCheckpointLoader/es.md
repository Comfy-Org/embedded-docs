Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/checkpoints`, y también leerá los modelos de las rutas adicionales configuradas en el archivo extra_model_paths.yaml. A veces, es posible que necesites **refrescar la interfaz de ComfyUI** para permitir que lea los archivos de modelo de la carpeta correspondiente.

Este nodo se especializa en cargar checkpoints específicamente para modelos basados en imágenes dentro de flujos de trabajo de generación de video. Recupera y configura eficientemente los componentes necesarios de un checkpoint dado, centrándose en los aspectos relacionados con la imagen del modelo.

## Entradas

| Campo      | Data Type | Descripción                                                                       |
|------------|-------------|-----------------------------------------------------------------------------------|
| `ckpt_name`| COMBO[STRING] | Especifica el nombre del checkpoint a cargar, crucial para identificar y recuperar el archivo de checkpoint correcto de una lista predefinida. |

## Salidas

| Campo     | Data Type | Descripción                                                                                   |
|-----------|-------------|-----------------------------------------------------------------------------------------------|
| `model`   | MODEL     | Devuelve el modelo principal cargado desde el checkpoint, configurado para el procesamiento de imágenes dentro de contextos de generación de video. |
| `clip_vision` | `CLIP_VISION` | Proporciona el componente de visión CLIP del checkpoint, adaptado para la comprensión de imágenes y la extracción de características. |
| `vae`     | VAE       | Entrega el componente Autoencoder Variacional (VAE), esencial para tareas de manipulación y generación de imágenes. |
