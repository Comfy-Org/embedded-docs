> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/es.md)

El nodo SaveLoRA guarda un modelo LoRA (Adaptación de Bajo Rango) en un archivo. Toma un modelo LoRA como entrada y lo escribe en un archivo `.safetensors` en el directorio de salida. Puedes especificar un prefijo para el nombre de archivo y un recuento de pasos opcional para que se incluya en el nombre final del archivo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `lora` | MODEL | Sí | N/A | El modelo LoRA que se va a guardar. No usar el modelo con capas LoRA. |
| `prefix` | STRING | Sí | N/A | El prefijo que se usará para el archivo LoRA guardado (por defecto: "loras/ComfyUI_trained_lora"). |
| `steps` | INT | No | N/A | Opcional: El número de pasos para los que se ha entrenado el LoRA, utilizado para nombrar el archivo guardado. |

**Nota:** La entrada `lora` debe ser un modelo LoRA puro. No proporciones un modelo base que tenga capas LoRA aplicadas.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| *Ninguna* | N/A | Este nodo no envía ningún dato al flujo de trabajo. Es un nodo de salida que guarda un archivo en el disco. |
