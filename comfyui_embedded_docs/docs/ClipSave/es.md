# Guardar CLIP

El nodo `CLIPSave` guarda un modelo de codificador de texto CLIP en disco en formato SafeTensors. Está diseñado para flujos de trabajo avanzados de fusión de modelos y separa automáticamente el modelo CLIP en sus partes componentes (como CLIP-L, CLIP-G o T5XXL) según la estructura interna del modelo, guardando cada componente como un archivo separado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `clip` | El modelo CLIP que se va a guardar. | CLIP | Sí | - |
| `filename_prefix` | La ruta del prefijo y el nombre de archivo para los archivos guardados. El nodo añade un sufijo de componente (p. ej., `_clip_l`, `_clip_g`) y un contador para crear nombres de archivo únicos (valor predeterminado: `clip/ComfyUI`). | STRING | Sí | - |
| `prompt` | La información del prompt del flujo de trabajo, guardada como metadatos en el archivo de salida. Este parámetro está oculto en la interfaz de usuario. | PROMPT | No | - |
| `extra_pnginfo` | Metadatos adicionales, guardados como pares clave-valor en el archivo de salida. Este parámetro está oculto en la interfaz de usuario. | EXTRA_PNGINFO | No | - |

## Salidas

Este nodo no tiene conexiones de salida. Guarda los archivos procesados directamente en el directorio `ComfyUI/output/`.

### Detalles de los archivos guardados

El nodo analiza el diccionario de estado del modelo CLIP y guarda archivos SafeTensors separados para cada componente detectado. El componente se identifica por el prefijo de sus claves de parámetros. El nodo verifica los siguientes prefijos, en orden:

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

Para cada componente detectado, el nodo crea un archivo con el nombre `{filename}_{counter:05}_.safetensors` (por ejemplo, `ComfyUI_clip_l_00001_.safetensors`), donde el nombre del componente se añade al prefijo del nombre de archivo y el contador garantiza nombres de archivo únicos. Cuando se guarda un componente, el prefijo `transformer.` se elimina de sus claves de parámetros.

Los metadatos escritos en cada archivo incluyen el prompt del flujo de trabajo y cualquier información PNG extra, a menos que el guardado de metadatos esté deshabilitado con el argumento de línea de comandos `--disable-metadata`.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSave/es.md)

---
**Source fingerprint (SHA-256):** `4ab9171e4245b10f738f78bac8a5b564c0957dde352e207ec3f9865e4fac0cab`
