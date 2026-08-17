# Codificar Texto CLIP (Prompt)

`CLIP Text Encode (CLIPTextEncode)` actúa como un traductor, convirtiendo sus descripciones de texto en un formato que la IA pueda entender. Esto ayuda a la IA a interpretar su entrada y generar la imagen deseada.

Piense en ello como comunicarse con un artista que habla un idioma diferente. El modelo CLIP, entrenado con vastos pares de imagen y texto, tiende un puente sobre esta brecha al convertir sus descripciones en "instrucciones" que el modelo de IA puede seguir.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `text` | El texto a codificar. Admite entradas de varias líneas y prompts dinámicos. | STRING | Sí | Cualquier texto |
| `clip` | El modelo CLIP utilizado para codificar el texto. | CLIP | Sí | Modelos CLIP cargados |

**Nota**: La entrada `clip` debe ser un modelo CLIP válido. Si es `None`, el nodo genera un error. Esto suele ocurrir cuando el checkpoint cargado por un nodo cargador de checkpoint no contiene un modelo CLIP o codificador de texto válido.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `CONDITIONING` | Un condicionamiento que contiene el texto incrustado utilizado para guiar el modelo de difusión. | CONDITIONING |

## Características del Prompt

### Modelos de incrustación

Los modelos de incrustación (embeddings) le permiten aplicar efectos o estilos artísticos específicos. Los formatos admitidos incluyen `.safetensors`, `.pt` y `.bin`. Para usar un modelo de incrustación:

1. Coloque el archivo en la carpeta `ComfyUI/models/embeddings`.
2. Refiérase a él en su texto usando `embedding:model_name`.

Ejemplo: Si tiene un modelo llamado `EasyNegative.pt` en su carpeta `ComfyUI/models/embeddings`, puede usarlo así:

```
worst quality, embedding:EasyNegative, bad quality
```

**IMPORTANTE**: Al usar modelos de incrustación, verifique que el nombre del archivo coincida y sea compatible con la arquitectura de su modelo. Por ejemplo, una incrustación diseñada para SD1.5 no funcionará correctamente con un modelo SDXL.

### Ajuste de peso del prompt

Puede ajustar la importancia de ciertas partes de su descripción usando paréntesis. Por ejemplo:

- `(beautiful:1.2)` aumenta el peso de "beautiful".
- `(beautiful:0.8)` disminuye el peso de "beautiful".
- Los paréntesis simples `(beautiful)` aplicarán un peso predeterminado de 1.1.

Puede usar los atajos de teclado `ctrl + flecha arriba/abajo` para ajustar rápidamente los pesos. El tamaño del paso de ajuste de peso se puede modificar en la configuración.

Si desea incluir paréntesis literales en su prompt sin cambiar el peso, puede escaparlos usando una barra invertida, p. ej. `\(word\)`.

### Prompts comodín/dinámicos

Use `{}` para crear prompts dinámicos. Por ejemplo, `{day|night|morning}` seleccionará aleatoriamente una opción cada vez que se procese el prompt.

Si desea incluir llaves literales en su prompt sin activar el comportamiento dinámico, puede escaparlas usando una barra invertida, p. ej. `\{word\}`.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncode/es.md)

---
**Source fingerprint (SHA-256):** `ace7988df7aaa3ac26419b16a9bd8908a327da6e82c21c2b2704af091d2e76e7`
