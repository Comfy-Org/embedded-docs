> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncode/es.md)

`CLIP Text Encode (CLIPTextEncode)` actúa como un traductor, convirtiendo tus descripciones de texto en un formato que la IA puede entender. Esto ayuda a la IA a interpretar tu entrada y generar la imagen deseada.

Piénsalo como comunicarte con un artista que habla un idioma diferente. El modelo CLIP, entrenado con vastos pares de imagen-texto, tiende un puente entre ambos al convertir tus descripciones en "instrucciones" que el modelo de IA puede seguir.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `texto` | STRING | Sí | Cualquier texto | El texto a codificar. Admite entrada de varias líneas y prompts dinámicos. |
| `clip` | CLIP | Sí | Modelos CLIP cargados | El modelo CLIP utilizado para codificar el texto. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Un condicionamiento que contiene el texto incrustado utilizado para guiar el modelo de difusión. |

## Características del Prompt

### Modelos de Incrustación (Embedding)

Los modelos de incrustación te permiten aplicar efectos artísticos o estilos específicos. Los formatos compatibles incluyen `.safetensors`, `.pt` y `.bin`. Para usar un modelo de incrustación:

1. Coloca el archivo en la carpeta `ComfyUI/models/embeddings`.
2. Haz referencia a él en tu texto usando `embedding:nombre_del_modelo`.

Ejemplo: Si tienes un modelo llamado `EasyNegative.pt` en tu carpeta `ComfyUI/models/embeddings`, puedes usarlo así:

```
worst quality, embedding:EasyNegative, bad quality
```

**IMPORTANTE**: Al usar modelos de incrustación, verifica que el nombre del archivo coincida y sea compatible con la arquitectura de tu modelo. Por ejemplo, una incrustación diseñada para SD1.5 no funcionará correctamente con un modelo SDXL.

### Ajuste de Peso del Prompt

Puedes ajustar la importancia de ciertas partes de tu descripción usando paréntesis. Por ejemplo:

- `(beautiful:1.2)` aumenta el peso de "beautiful".
- `(beautiful:0.8)` disminuye el peso de "beautiful".
- Los paréntesis simples `(beautiful)` aplicarán un peso predeterminado de 1.1.

Puedes usar los atajos de teclado `ctrl + flecha arriba/abajo` para ajustar rápidamente los pesos. El tamaño del paso de ajuste de peso se puede modificar en la configuración.

Si deseas incluir paréntesis literales en tu prompt sin cambiar el peso, puedes escaparlos usando una barra invertida, ej. `\(palabra\)`.

### Prompts Dinámicos/Comodín (Wildcard)

Usa `{}` para crear prompts dinámicos. Por ejemplo, `{día|noche|mañana}` seleccionará aleatoriamente una opción cada vez que se procese el prompt.

Si deseas incluir llaves literales en tu prompt sin activar el comportamiento dinámico, puedes escaparlas usando una barra invertida, ej. `\{palabra\}`.

**Source fingerprint (SHA-256):** `e8f286cdec879c529270e110ccf5959ed6df77737cfb5a8019379afac9266118`
