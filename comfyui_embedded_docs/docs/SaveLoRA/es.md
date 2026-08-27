# Guardar pesos de LoRA

El nodo SaveLoRA guarda un modelo LoRA (Adaptación de Bajo Rango) en un archivo. Toma un modelo LoRA como entrada y lo escribe en un archivo `.safetensors` en el directorio de salida. Puede especificar un prefijo para el nombre de archivo y un número de pasos opcional que se incluirá en el nombre final del archivo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `lora` | El modelo LoRA a guardar. No utilice el modelo con capas LoRA. | LORA_MODEL | Sí | N/A |
| `prefix` | El prefijo que se usará para el archivo LoRA guardado (por defecto: "loras/ComfyUI_trained_lora"). | STRING | Sí | N/A |
| `steps` | Opcional: El número de pasos con los que se ha entrenado el LoRA, utilizado para nombrar el archivo guardado. | INT | No | N/A |

**Nota:** La entrada `lora` debe ser un modelo LoRA puro. No proporcione un modelo base que tenga capas LoRA aplicadas.

**Nota:** El archivo se guarda en el directorio de salida de ComfyUI con una extensión `.safetensors`. El nombre del archivo se construye a partir del `prefix` y un contador con relleno de ceros (5 dígitos) para evitar sobrescribir archivos existentes. Cuando se proporciona `steps`, el número de pasos también se incluye en el nombre del archivo (por ejemplo, `1000_steps` para 1000 pasos).

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| *None* | Este nodo no envía ningún dato al flujo de trabajo. Es un nodo de salida que guarda un archivo en el disco. | N/A |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/es.md)

---
**Source fingerprint (SHA-256):** `02f1d15dd7a5181666f2dbf06c45c07b12c4a178985464e07b5f613bd628f906`
