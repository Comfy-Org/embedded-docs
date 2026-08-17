# ModeloCalcularDtype

El nodo ModelComputeDtype cambia el tipo de datos computacionales (precisión) utilizado por un modelo durante el procesamiento. Crea una copia del modelo de entrada y aplica la configuración de precisión seleccionada, lo que puede ayudar a optimizar el uso de memoria y el rendimiento según tu hardware. Esto es útil para depurar y probar diferentes configuraciones de precisión.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de entrada a modificar con un nuevo tipo de datos computacionales | MODEL | Sí | - |
| `dtype` | El tipo de datos computacionales que se aplicará al modelo (por defecto: "default"). Este parámetro está marcado como configuración avanzada en la interfaz de usuario. | COMBO | Sí | "default"<br>"fp32"<br>"fp16"<br>"bf16" |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo modificado con el nuevo tipo de datos computacionales aplicado | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelComputeDtype/es.md)

---
**Source fingerprint (SHA-256):** `ad9c39e1217fd2e343ad4f49df9d1acabbc4708966dadec5340bb975adb59854`
