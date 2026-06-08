El nodo `ModelComputeDtype` cambia el tipo de datos computacional (precisión) utilizado por un modelo durante el procesamiento. Crea una copia del modelo de entrada y aplica la configuración de precisión seleccionada, lo que puede ayudar a optimizar el uso de memoria y el rendimiento según tu hardware. Esto es útil para depurar y probar diferentes configuraciones de precisión.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de entrada al que se le aplicará un nuevo tipo de datos computacional | MODEL | Sí | - |
| `dtype` | El tipo de datos computacional que se aplicará al modelo (predeterminado: "default") | STRING | Sí | "default"<br>"fp32"<br>"fp16"<br>"bf16" |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `modelo` | El modelo modificado con el nuevo tipo de datos computacional aplicado | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelComputeDtype/es.md)

---
**Source fingerprint (SHA-256):** `bc65f1e452d0122ad175a8b95f38a36503253c9908157037c516496e65c828e6`
