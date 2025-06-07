Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/upscale_models`,
y también leerá los modelos de las rutas adicionales que hayas configurado en el archivo extra_model_paths.yaml.
A veces, es posible que necesites **refrescar la interfaz de ComfyUI** para que pueda leer los archivos de modelo en la carpeta correspondiente.

El nodo VAELoader está diseñado para cargar modelos de Autoencoder Variacional (VAE), específicamente adaptados para manejar tanto VAEs estándar como aproximados. Soporta la carga de VAEs por nombre, incluyendo un manejo especializado para los modelos 'taesd' y 'taesdxl', y se ajusta dinámicamente según la configuración específica del VAE.

## Entradas

| Campo   | Comfy dtype       | Descripción                                                                                   |
|---------|-------------------|-----------------------------------------------------------------------------------------------|
| `vae_name` | `COMBO[STRING]`    | Especifica el nombre del VAE a cargar, determinando qué modelo VAE se obtiene y carga, con soporte para una gama de nombres de VAE predefinidos, incluyendo 'taesd' y 'taesdxl'. |

## Salidas

| Campo | Data Type | Descripción                                                              |
|-------|-------------|--------------------------------------------------------------------------|
| `vae`  | `VAE`       | Devuelve el modelo VAE cargado, listo para operaciones adicionales como codificación o decodificación. La salida es un objeto modelo que encapsula el estado del modelo cargado. |
