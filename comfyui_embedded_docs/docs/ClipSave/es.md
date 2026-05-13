> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSave/es.md)

El nodo `CLIPSave` guarda un modelo de codificador de texto CLIP en disco en formato SafeTensors. Está diseñado para flujos de trabajo avanzados de fusión de modelos y separa automáticamente el modelo CLIP en sus partes componentes (como CLIP-L, CLIP-G o T5XXL) según la estructura interna del modelo, guardando cada componente como un archivo separado.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Valor por Defecto | Rango | Descripción |
|-----------|--------------|-----------------|-------------------|-------|-------------|
| `clip` | CLIP | Requerido | - | - | El modelo CLIP que se va a guardar. |
| `filename_prefix` | STRING | Requerido | `clip/ComfyUI` | - | La ruta de prefijo y nombre de archivo para los archivos guardados. El nodo añadirá un sufijo de componente (ej., `_clip_l`, `_clip_g`) y un contador para crear nombres de archivo únicos. |
| `prompt` | PROMPT | Oculto | - | - | La información del prompt del flujo de trabajo, guardada como metadatos en el archivo de salida. |
| `extra_pnginfo` | EXTRA_PNGINFO | Oculto | - | - | Metadatos adicionales, guardados como pares clave-valor en el archivo de salida. |

## Salidas

Este nodo no tiene conexiones de salida. Guarda los archivos procesados directamente en el directorio `ComfyUI/output/`.

### Detalles del Archivo Guardado

El nodo analiza el diccionario de estado del modelo CLIP y guarda archivos SafeTensors separados para cada componente detectado. El componente se identifica por el prefijo de sus claves de parámetros. Se verifican los siguientes prefijos:

- `clip_l.` (codificador de texto CLIP-L)
- `clip_g.` (codificador de texto CLIP-G)
- `clip_h.` (codificador de texto CLIP-H)
- `t5xxl.` (codificador de texto T5-XXL)
- `pile_t5xl.` (codificador de texto Pile-T5-XL)
- `mt5xl.` (codificador de texto mT5-XL)
- `umt5xxl.` (codificador de texto UMT5-XXL)
- `t5base.` (codificador de texto T5-Base)
- `gemma2_2b.` (codificador de texto Gemma 2 2B)
- `llama.` (codificador de texto LLaMA)
- `hydit_clip.` (codificador de texto Hydit CLIP)
- Prefijo vacío (otros componentes CLIP)

Para cada componente detectado, el nodo crea un archivo con el nombre `{filename_prefix}_{contador:05}_.safetensors`, donde el prefijo del componente se añade al prefijo del nombre de archivo (ej., `clip/ComfyUI_clip_l_00001_.safetensors`). El prefijo `transformer.` se elimina de las claves de parámetros durante el guardado.

---
**Source fingerprint (SHA-256):** `039b39cbfb9b04ccebc5fc885ebe75dfde14838530d38133d0a3a6311e392059`
