> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXAVTextEncoderLoader/es.md)

Este nodo carga un codificador de texto especializado para el modelo de audio LTXV. Combina un archivo de codificador de texto específico con un archivo de checkpoint para crear un modelo CLIP que puede utilizarse en tareas de condicionamiento de texto relacionadas con audio.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `text_encoder` | STRING | Sí | Múltiples opciones disponibles | El nombre del archivo del modelo de codificador de texto LTXV a cargar. Las opciones disponibles se cargan desde la carpeta `text_encoders`. |
| `ckpt_name` | STRING | Sí | Múltiples opciones disponibles | El nombre del archivo del checkpoint a cargar. Las opciones disponibles se cargan desde la carpeta `checkpoints`. |
| `device` | STRING | No | `"default"`<br>`"cpu"` | Especifica el dispositivo en el que cargar el modelo. Use `"cpu"` para forzar la carga en la CPU. El comportamiento predeterminado (`"default"`) utiliza la asignación automática de dispositivos del sistema. |

**Nota:** Los parámetros `text_encoder` y `ckpt_name` funcionan en conjunto. El nodo carga ambos archivos especificados para crear un único modelo CLIP funcional. Los archivos deben ser compatibles con la arquitectura LTXV.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `clip` | CLIP | El modelo CLIP LTXV cargado, listo para usarse en la codificación de indicaciones de texto para generación de audio. |

---
**Source fingerprint (SHA-256):** `c072a0b3393aa44333bb15ae42179c50868a4e9d7ca706d6c7da5922625373e6`
