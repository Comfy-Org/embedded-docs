> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRANode/es.md)

El nodo SaveLoRA guarda modelos LoRA (Low-Rank Adaptation) en su directorio de salida. Toma un modelo LoRA como entrada y crea un archivo safetensors con un nombre de archivo generado automáticamente. Puede personalizar el prefijo del nombre de archivo y opcionalmente incluir el recuento de pasos de entrenamiento en el nombre del archivo para una mejor organización.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `lora` | LORA_MODEL | Sí | - | El modelo LoRA a guardar. No utilice el modelo con capas LoRA. |
| `prefix` | STRING | Sí | - | El prefijo a utilizar para el archivo LoRA guardado (por defecto: "loras/ComfyUI_trained_lora"). |
| `steps` | INT | No | - | Opcional: El número de pasos para los que el LoRA ha sido entrenado, utilizado para nombrar el archivo guardado. |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| *Ninguno* | - | Este nodo no devuelve ninguna salida, pero guarda el modelo LoRA en el directorio de salida. |
