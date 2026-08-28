# GuardarModelo

El nodo ModelSave guarda un modelo en el almacenamiento de tu computadora como un archivo de checkpoint `.safetensors`. Toma un modelo como entrada y lo escribe en el directorio de salida utilizando el prefijo de nombre de archivo que especifiques. Cuando está disponible, también incrusta información del prompt del flujo de trabajo y metadatos adicionales en el archivo guardado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo que se guardará en el disco | MODEL | Sí | - |
| `prefijo_nombre_archivo` | El prefijo de nombre de archivo y ruta para el archivo de modelo guardado (predeterminado: "diffusion_models/ComfyUI") | STRING | Sí | - |
| `prompt` | Información del prompt del flujo de trabajo (proporcionada automáticamente) | PROMPT | No | - |
| `extra_pnginfo` | Metadatos adicionales del flujo de trabajo (proporcionados automáticamente) | EXTRA_PNGINFO | No | - |

Nota: El nombre de archivo guardado se construye a partir del valor de `filename_prefix` seguido de un contador de cinco dígitos (por ejemplo, `diffusion_models/ComfyUI_00001_.safetensors`). Si ya existe un archivo con el mismo prefijo, el contador se incrementa para que el nuevo archivo tenga un nombre único. Cuando están disponibles, el prompt del flujo de trabajo, los metadatos adicionales y la información de la arquitectura del modelo se incrustan en el archivo guardado.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| *None* | Este nodo no devuelve ningún valor de salida | - |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/es.md)

---
**Source fingerprint (SHA-256):** `943e60f2c596d9cbcaabe95029fd9d443df5b61c6137736a8b1b81ab78f200ea`
