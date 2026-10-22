# Text Encode MOSS-Image Edit

Codifica una instrucción de edición junto con imágenes de referencia en el condicionamiento para un LoRA de edición MOSS-Image. Conecta la salida como el condicionamiento positivo y ejecuta una segunda instancia con las mismas referencias para el negativo. Las referencias se utilizan con el tamaño con el que llegan, así que escálalas antes de conectarlas. Este nodo está marcado como experimental en ComfyUI.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `clip` | El modelo CLIP que tokeniza la instrucción y la codifica. | CLIP | Sí | - |
| `prompt` | La instrucción que describe la edición. Admite texto multilínea y prompts dinámicos. | STRING | Sí | Cualquier texto |
| `vae` | El VAE utilizado para codificar las imágenes de referencia en latentes de referencia. | VAE | Sí | - |
| `edit_format` | El formato con el que se entrenó el LoRA de edición. Selecciona el método de latentes de referencia y si el codificador de texto también ve las referencias. | COMBO | Sí | `"ai-toolkit"`<br>`"ai-toolkit (kv_cache off)"`<br>`"Moss-Image-Edit"` |
| `images` | Ranura ampliable: conecta una o más imágenes de referencia (`image_1`, `image_2`, ...). Cada imagen se utiliza con el tamaño con el que llega, se le quita el canal alfa y se codifica con VAE en un latente de referencia. | IMAGE | Sí | 1 o más imágenes |

**Nota:** Con `"ai-toolkit"` y `"ai-toolkit (kv_cache off)"` el codificador de texto también ve cada referencia, reducida a un máximo de 384x384 píxeles y precedida por un marcador `Picture N:` en el prompt, de modo que la instrucción puede referirse a ellas por número. Con `"Moss-Image-Edit"` las referencias llegan al modelo solo como latentes de referencia y el codificador de texto ve únicamente la instrucción. `"ai-toolkit (kv_cache off)"` además mantiene las referencias atendiendo a la imagen que se está generando, por lo que se recalculan en cada paso de muestreo.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `conditioning` | La instrucción codificada con los latentes de referencia y el método de latentes de referencia correspondiente adjuntos. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMOSSImageEdit/es.md)

---
**Source fingerprint (SHA-256):** `30e4edbb129f647cdce4ec95f78c002ecdc9a4f8fc5a45f1477fdc555b541dae`
