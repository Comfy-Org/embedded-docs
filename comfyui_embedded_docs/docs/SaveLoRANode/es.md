> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRANode/es.md)

El nodo SaveLoRA guarda modelos LoRA (Adaptación de Bajo Rango) en tu directorio de salida. Toma un modelo LoRA como entrada y crea un archivo safetensors con un nombre de archivo generado automáticamente. Puedes personalizar el prefijo del nombre de archivo y, opcionalmente, incluir el número de pasos de entrenamiento en el nombre para una mejor organización.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `lora` | LORA_MODEL | Sí | - | El modelo LoRA a guardar. No uses el modelo con capas LoRA. |
| `prefix` | STRING | Sí | - | El prefijo a utilizar para el archivo LoRA guardado (predeterminado: "loras/ComfyUI_trained_lora"). |
| `steps` | INT | No | - | Opcional: El número de pasos con los que se ha entrenado el LoRA, utilizado para nombrar el archivo guardado. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| *Ninguno* | - | Este nodo no devuelve ninguna salida, pero guarda el modelo LoRA en el directorio de salida. |

---
**Source fingerprint (SHA-256):** `06a1067433aa4b720b51050b09fbad4870caf12c5e92f788d44ea022a39efef4`
