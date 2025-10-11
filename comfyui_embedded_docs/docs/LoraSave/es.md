> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraSave/es.md)

El nodo LoraSave extrae y guarda archivos LoRA (Low-Rank Adaptation) a partir de diferencias de modelos. Puede procesar diferencias de modelos de difusión, diferencias de codificadores de texto, o ambos, convirtiéndolos al formato LoRA con un rango y tipo específicos. El archivo LoRA resultante se guarda en el directorio de salida para su uso posterior.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `filename_prefix` | STRING | Sí | - | El prefijo para el nombre del archivo de salida (por defecto: "loras/ComfyUI_extracted_lora") |
| `rank` | INT | Sí | 1-4096 | El valor de rango para el LoRA, que controla el tamaño y la complejidad (por defecto: 8) |
| `lora_type` | COMBO | Sí | Múltiples opciones disponibles | El tipo de LoRA a crear, con varias opciones disponibles |
| `bias_diff` | BOOLEAN | Sí | - | Si se deben incluir diferencias de sesgo en el cálculo del LoRA (por defecto: True) |
| `model_diff` | MODEL | No | - | La salida de ModelSubtract que se convertirá en un lora |
| `text_encoder_diff` | CLIP | No | - | La salida de CLIPSubtract que se convertirá en un lora |

**Nota:** Se debe proporcionar al menos uno de los parámetros `model_diff` o `text_encoder_diff` para que el nodo funcione. Si se omiten ambos, el nodo no producirá ninguna salida.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| - | - | Este nodo guarda un archivo LoRA en el directorio de salida pero no devuelve ningún dato a través del flujo de trabajo |