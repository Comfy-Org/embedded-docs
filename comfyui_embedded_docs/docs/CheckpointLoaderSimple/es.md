# Cargar Punto de Control

Carga un archivo de checkpoint de modelo de difusión y lo descompone en tres componentes principales: el modelo principal utilizado para eliminar el ruido de los latentes, el codificador de texto CLIP y el codificador/decodificador de imágenes VAE. Este nodo detecta automáticamente todos los archivos de modelo en la carpeta `ComfyUI/models/checkpoints` y cualquier ruta adicional configurada en su archivo `extra_model_paths.yaml`.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `nombre_ckpt` | El nombre del checkpoint (modelo) a cargar. Seleccione el nombre del archivo de checkpoint, que determina el modelo de IA utilizado para la generación posterior de imágenes. | COMBO | Sí | Todos los archivos de modelo en la carpeta de checkpoints |

**Nota:** Si se añaden nuevos archivos de modelo mientras ComfyUI está en ejecución, debe actualizar el navegador (Ctrl+R) para ver los nuevos archivos en la lista desplegable.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `MODEL` | El modelo utilizado para eliminar el ruido de los latentes. Este es el modelo de difusión principal utilizado para la generación de imágenes. | MODEL |
| `CLIP` | El modelo CLIP utilizado para codificar las indicaciones de texto, convirtiendo las descripciones de texto en información que la IA puede entender. | CLIP |
| `VAE` | El modelo VAE utilizado para codificar y decodificar imágenes hacia y desde el espacio latente. | VAE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoaderSimple/es.md)

---
**Source fingerprint (SHA-256):** `db99a8ba83a586491463df0d4e99ba5f77d4511c6d8337a721d76edd3450f310`
