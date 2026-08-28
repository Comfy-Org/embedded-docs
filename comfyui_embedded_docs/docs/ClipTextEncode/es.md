# ClipTextEncode

`CLIP Text Encode (CLIPTextEncode)` actúa como un traductor, convirtiendo tus descripciones de texto en un formato que la IA puede entender. Esto ayuda a la IA a interpretar tu entrada y generar la imagen deseada.

Piénsalo como comunicarte con un artista que habla otro idioma. El modelo CLIP, entrenado con vastos pares de imagen-texto, supera esta brecha convirtiendo tus descripciones en «instrucciones» que el modelo de IA puede seguir.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `texto` | El texto a codificar. Admite entrada de varias líneas y prompts dinámicos. | STRING | Sí | Cualquier texto |
| `clip` | El modelo CLIP utilizado para codificar el texto. | CLIP | Sí | Modelos CLIP cargados |

Nota: Si la entrada `clip` es None (por ejemplo, cuando proviene de un cargador de checkpoint cuyo checkpoint no contiene un modelo CLIP o un codificador de texto válido), el nodo genera un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `CONDITIONING` | Un condicionamiento que contiene el texto incrustado utilizado para guiar el modelo de difusión. | CONDITIONING |

## Características del Prompt

### Modelos de Embedding

Los modelos de embedding te permiten aplicar efectos artísticos o estilos específicos. Los formatos compatibles incluyen `.safetensors`, `.pt` y `.bin`. Para usar un modelo de embedding:

1. Coloca el archivo en la carpeta `ComfyUI/models/embeddings`.
2. Haz referencia a él en tu texto usando `embedding:model_name`.

Ejemplo: Si tienes un modelo llamado `EasyNegative.pt` en tu carpeta `ComfyUI/models/embeddings`, puedes usarlo de la siguiente manera:

```
worst quality, embedding:EasyNegative, bad quality
```

**IMPORTANTE**: Al usar modelos de embedding, verifica que el nombre del archivo coincida y sea compatible con la arquitectura de tu modelo. Por ejemplo, un embedding diseñado para SD1.5 no funcionará correctamente con un modelo SDXL.

### Ajuste de peso del prompt

Puedes ajustar la importancia de ciertas partes de tu descripción usando paréntesis. Por ejemplo:

- `(beautiful:1.2)` aumenta el peso de "beautiful".
- `(beautiful:0.8)` disminuye el peso de "beautiful".
- Los paréntesis simples `(beautiful)` aplicarán un peso predeterminado de 1.1.

Puedes usar los atajos de teclado `ctrl + flecha arriba/abajo` para ajustar los pesos rápidamente. El tamaño del paso del ajuste de peso se puede modificar en la configuración.

Si deseas incluir paréntesis literales en tu prompt sin cambiar el peso, puedes escaparlos usando una barra invertida, p. ej. `\(word\)`.

### Comodines/Prompts dinámicos

Usa `{}` para crear prompts dinámicos. Por ejemplo, `{day|night|morning}` seleccionará aleatoriamente una opción cada vez que se procese el prompt.

Si deseas incluir llaves literales en tu prompt sin activar el comportamiento dinámico, puedes escaparlas usando una barra invertida, p. ej. `\{word\}`.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipTextEncode/es.md)

---
**Source fingerprint (SHA-256):** `ace7988df7aaa3ac26419b16a9bd8908a327da6e82c21c2b2704af091d2e76e7`
