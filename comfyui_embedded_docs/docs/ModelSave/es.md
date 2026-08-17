# GuardarModelo

El nodo ModelSave guarda modelos entrenados o modificados en el almacenamiento de tu computadora. Toma un modelo como entrada y lo escribe en un archivo de checkpoint en formato safetensors dentro de la carpeta de salida, utilizando el prefijo de nombre de archivo que especifiques. La información del prompt del flujo de trabajo y los metadatos se incrustan en el archivo guardado cuando están disponibles.

## Entradas

| Parámetro | Descripción | Tipo de datos | ¿Requerido? | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo que se guardará en el disco | MODEL | Sí | - |
| `filename_prefix` | El prefijo de nombre de archivo y ruta para el archivo de modelo guardado (predeterminado: "diffusion_models/ComfyUI"). Se agrega un contador al nombre al guardar (por ejemplo, `ComfyUI_00000_.safetensors`). | STRING | Sí | - |
| `prompt` | Información del prompt del flujo de trabajo (proporcionada automáticamente) | PROMPT | No | - |
| `extra_pnginfo` | Metadatos adicionales del flujo de trabajo (proporcionados automáticamente) | EXTRA_PNGINFO | No | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| *None* | Este nodo no devuelve ningún valor de salida | - |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/es.md)

---
**Source fingerprint (SHA-256):** `943e60f2c596d9cbcaabe95029fd9d443df5b61c6137736a8b1b81ab78f200ea`
