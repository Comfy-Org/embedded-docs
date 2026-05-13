> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNETLoader/es.md)

El nodo UNETLoader está diseñado para cargar modelos U-Net por nombre, facilitando el uso de arquitecturas U-Net preentrenadas dentro del sistema.

Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/diffusion_models`.

## Entradas

| Parámetro   | Tipo de Dato | Descripción |
|-------------|--------------|-------------|
| `unet_name` | COMBO[STRING] | Especifica el nombre del modelo U-Net a cargar. Este nombre se utiliza para localizar el modelo dentro de una estructura de directorios predefinida, permitiendo la carga dinámica de diferentes modelos U-Net. |
| `weight_dtype` | ... | 🚧  fp8_e4m3fn fp9_e5m2  |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `model`   | MODEL     | Devuelve el modelo U-Net cargado, permitiendo su uso para procesamiento adicional o inferencia dentro del sistema. |