# Guardar pesos de LoRA

El nodo SaveLoRA guarda un modelo LoRA (Adaptación de Bajo Rango) en un archivo. Toma un modelo LoRA como entrada y lo escribe en un archivo `.safetensors` en el directorio de salida. Puedes especificar un prefijo para el nombre del archivo y un número opcional de pasos que se incluirá en el nombre final.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `lora` | El modelo LoRA a guardar. No uses el modelo con capas LoRA aplicadas. | LORA_MODEL | Sí | N/A |
| `prefix` | El prefijo a usar para el archivo LoRA guardado (predeterminado: "loras/ComfyUI_trained_lora"). | STRING | Sí | N/A |
| `steps` | Opcional: El número de pasos con los que se ha entrenado el LoRA, usado para nombrar el archivo guardado. | INT | No | N/A |

**Nota:** La entrada `lora` debe ser un modelo LoRA puro. No proporciones un modelo base que tenga capas LoRA aplicadas.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| *Ninguno* | Este nodo no envía ningún dato al flujo de trabajo. Es un nodo de salida que guarda un archivo en el disco. | N/A |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/es.md)

---
**Source fingerprint (SHA-256):** `e68a449d741c908f23fc1585d848254d78c310ad19efbd139c33c9ddef3145c7`
