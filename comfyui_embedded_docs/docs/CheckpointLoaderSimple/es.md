> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoaderSimple/es.md)

## Descripción general

Carga un archivo de modelo de difusión (checkpoint) y lo descompone en tres componentes principales: el modelo principal utilizado para eliminar el ruido de los latentes, el codificador de texto CLIP y el codificador/decodificador de imágenes VAE. Este nodo detecta automáticamente todos los archivos de modelo en la carpeta `ComfyUI/models/checkpoints` y cualquier ruta adicional configurada en tu archivo `extra_model_paths.yaml`.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `nombre_ckpt` | STRING | Sí | Todos los archivos de modelo en la carpeta de checkpoints | El nombre del checkpoint (modelo) a cargar. Selecciona el nombre del archivo del checkpoint, que determina el modelo de IA utilizado para la generación de imágenes posterior. |

**Nota:** Si se agregan nuevos archivos de modelo mientras ComfyUI está en ejecución, es necesario actualizar el navegador (Ctrl+R) para ver los nuevos archivos en la lista desplegable.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `MODEL` | MODEL | El modelo utilizado para eliminar el ruido de los latentes. Este es el modelo de difusión principal utilizado para la generación de imágenes. |
| `CLIP` | CLIP | El modelo CLIP utilizado para codificar indicaciones de texto, convirtiendo descripciones textuales en información que la IA puede entender. |
| `VAE` | VAE | El modelo VAE utilizado para codificar y decodificar imágenes hacia y desde el espacio latente. |

---
**Source fingerprint (SHA-256):** `2fd8866ae659f8080f46c16d3a9864fa563d2090815d897ea2f42ba8d66d9b39`
