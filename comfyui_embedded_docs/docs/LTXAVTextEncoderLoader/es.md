# Cargador de codificador de texto LTXV Audio

Este nodo carga un codificador de texto especializado para el modelo de audio LTXV. Combina un archivo de codificador de texto con un archivo de checkpoint para crear un modelo CLIP que puede utilizarse para tareas de condicionamiento de texto relacionadas con audio. Según la descripción de la receta del nodo, el codificador de texto de audio LTXV debe ser un modelo Gemma 3 12B o un modelo Gemma 4 compatible.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `text_encoder` | El nombre del archivo del modelo de codificador de texto LTXV a cargar. Las opciones disponibles se cargan desde la carpeta `text_encoders`. | COMBO | Sí | Múltiples opciones disponibles |
| `ckpt_name` | El nombre del archivo del checkpoint a cargar. Las opciones disponibles se cargan desde la carpeta `checkpoints`. | COMBO | Sí | Múltiples opciones disponibles |
| `device` | Especifica el dispositivo en el que se cargará el modelo. Usa `"cpu"` para forzar la carga en la CPU. El comportamiento predeterminado (`"default"`) utiliza la asignación automática de dispositivo del sistema (predeterminado: `"default"`). | COMBO | No | `"default"`<br>`"cpu"` |

**Nota:** Los parámetros `text_encoder` y `ckpt_name` funcionan juntos. El nodo carga ambos archivos especificados para crear un único modelo CLIP funcional. Los archivos deben ser compatibles con la arquitectura LTXV.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `clip` | El modelo CLIP LTXV cargado, listo para usarse para codificar indicaciones de texto para la generación de audio. | CLIP |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXAVTextEncoderLoader/es.md)

---
**Source fingerprint (SHA-256):** `1f3df2c1791203ba849a87897de14052e0cb8370100dbca19df4cf30169a0a2a`
