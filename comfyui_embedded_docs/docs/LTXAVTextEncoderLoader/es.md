> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXAVTextEncoderLoader/es.md)

Este nodo carga un codificador de texto especializado para el modelo de audio LTXV. Combina un archivo específico de codificador de texto con un archivo de punto de control para crear un modelo CLIP que puede utilizarse en tareas de condicionamiento de texto relacionadas con audio.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `text_encoder` | STRING | Sí | Múltiples opciones disponibles | El nombre de archivo del modelo codificador de texto LTXV a cargar. Las opciones disponibles se cargan desde la carpeta `text_encoders`. |
| `ckpt_name` | STRING | Sí | Múltiples opciones disponibles | El nombre de archivo del punto de control a cargar. Las opciones disponibles se cargan desde la carpeta `checkpoints`. |
| `device` | STRING | No | `"default"`<br>`"cpu"` | Especifica el dispositivo en el que cargar el modelo. Usa `"cpu"` para forzar la carga en la CPU. El comportamiento por defecto (`"default"`) utiliza la colocación automática de dispositivos del sistema. |

**Nota:** Los parámetros `text_encoder` y `ckpt_name` funcionan en conjunto. El nodo carga ambos archivos especificados para crear un único modelo CLIP funcional. Los archivos deben ser compatibles con la arquitectura LTXV.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `clip` | CLIP | El modelo CLIP LTXV cargado, listo para ser utilizado para codificar prompts de texto para la generación de audio. |
