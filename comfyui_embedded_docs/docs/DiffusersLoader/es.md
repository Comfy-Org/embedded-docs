> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/es.md)

El nodo DiffusersLoader carga modelos preentrenados desde el formato diffusers. Busca directorios de modelos diffusers válidos que contengan un archivo `model_index.json` y los carga como componentes MODEL, CLIP y VAE para su uso en el pipeline. Este nodo pertenece a la categoría de cargadores obsoletos y proporciona compatibilidad con modelos diffusers de Hugging Face.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `ruta_del_modelo` | STRING | Sí | Múltiples opciones disponibles<br>(auto-rellenadas desde las carpetas diffusers) | La ruta al directorio del modelo diffusers a cargar. El nodo escanea automáticamente los modelos diffusers válidos en las carpetas configuradas y lista las opciones disponibles. |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `MODEL` | MODEL | El componente del modelo cargado desde el formato diffusers |
| `CLIP` | CLIP | El componente del modelo CLIP cargado desde el formato diffusers |
| `VAE` | VAE | El componente VAE (Autoencoder Variacional) cargado desde el formato diffusers |

---
**Source fingerprint (SHA-256):** `59be9923ed76d4859d5f7217a802c43297cb5af3d895eb6713edea97a32c3db2`
