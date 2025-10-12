> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/es.md)

El nodo DiffusersLoader carga modelos preentrenados desde el formato diffusers. Busca directorios válidos de modelos diffusers que contengan un archivo model_index.json y los carga como componentes MODEL, CLIP y VAE para su uso en el pipeline. Este nodo forma parte de la categoría obsoleta de cargadores y proporciona compatibilidad con modelos de Hugging Face diffusers.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `ruta_del_modelo` | STRING | Sí | Múltiples opciones disponibles<br>(autocompletado desde carpetas diffusers) | La ruta al directorio del modelo diffusers a cargar. El nodo escanea automáticamente en busca de modelos diffusers válidos en las carpetas diffusers configuradas y lista las opciones disponibles. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `MODEL` | MODEL | El componente del modelo cargado desde el formato diffusers |
| `CLIP` | CLIP | El componente del modelo CLIP cargado desde el formato diffusers |
| `VAE` | VAE | El componente VAE (Autoencoder Variacional) cargado desde el formato diffusers |