> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraSave/es.md)

El nodo LoraSave extrae y guarda archivos LoRA (Adaptación de Bajo Rango) a partir de diferencias de modelos. Puede procesar diferencias de modelos de difusión, diferencias de codificadores de texto, o ambas, convirtiéndolas en formato LoRA con rango y tipo especificados. El archivo LoRA resultante se guarda en el directorio de salida para su uso posterior.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `prefijo_nombre_archivo` | STRING | Sí | - | El prefijo para el nombre del archivo de salida (predeterminado: "loras/ComfyUI_extracted_lora") |
| `rango` | INT | Sí | 1-4096 | El valor de rango para el LoRA, que controla el tamaño y la complejidad (predeterminado: 8) |
| `tipo_lora` | COMBO | Sí | `"standard"`<br>`"locon"`<br>`"loha"`<br>`"lokr"`<br>`"dylora"` | El tipo de LoRA a crear (predeterminado: "standard") |
| `diferencia_sesgo` | BOOLEAN | Sí | - | Si se deben incluir las diferencias de sesgo en el cálculo del LoRA (predeterminado: True) |
| `diferencia_modelo` | MODEL | No | - | La salida de ModelSubtract que se convertirá en un lora |
| `diferencia_codificador_texto` | CLIP | No | - | La salida de CLIPSubtract que se convertirá en un lora |

**Nota:** Se debe proporcionar al menos uno de los parámetros `model_diff` o `text_encoder_diff` para que el nodo funcione. Si ambos se omiten, el nodo no generará ninguna salida.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| - | - | Este nodo guarda un archivo LoRA en el directorio de salida, pero no devuelve ningún dato a través del flujo de trabajo |

---
**Source fingerprint (SHA-256):** `fdf020915ee233cf68250dcdcf87e7862d13ccc4fa73d8da8245727fdac46015`
