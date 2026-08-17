# Guardar pesos de LoRA

El nodo SaveLoRA guarda un modelo LoRA (Adaptación de Bajo Rango) en un archivo. Escribe el modelo LoRA como un archivo `.safetensors` en el directorio de salida. Puede especificar un prefijo para el nombre del archivo y un número opcional de pasos; cuando se proporciona, el número de pasos se incluye en el nombre del archivo guardado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `lora` | El modelo LoRA a guardar. No utilice el modelo con capas LoRA aplicadas. | LORA_MODEL | Sí | N/A |
| `prefix` | El prefijo a utilizar para el archivo LoRA guardado (predeterminado: "loras/ComfyUI_trained_lora"). | STRING | Sí | N/A |
| `steps` | Opcional: El número de pasos para los que se ha entrenado el LoRA, utilizado para nombrar el archivo guardado. | INT | No | N/A |

**Nota:** La entrada `lora` debe ser un modelo LoRA puro. No proporcione un modelo base con capas LoRA aplicadas.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| *None* | Este nodo no genera ningún dato para el flujo de trabajo. Es un nodo de salida que guarda un archivo en disco. | N/A |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/es.md)

---
**Source fingerprint (SHA-256):** `02f1d15dd7a5181666f2dbf06c45c07b12c4a178985464e07b5f613bd628f906`
