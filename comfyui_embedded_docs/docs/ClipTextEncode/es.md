> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncode/es.md)

`CLIP Text Encode (CLIPTextEncode)` actúa como un traductor, convirtiendo tus descripciones de texto en un formato que la IA puede entender. Esto ayuda a la IA a interpretar tu entrada y generar la imagen deseada.

Piensa en ello como comunicarte con un artista que habla un idioma diferente. El modelo CLIP, entrenado con vastos pares de imagen-texto, salva esta brecha convirtiendo tus descripciones en "instrucciones" que el modelo de IA puede seguir.

## Entradas

| Parámetro | Tipo de Dato | Método de Entrada | Valor por Defecto | Rango | Descripción |
|-----------|-----------|--------------|---------|--------|-------------|
| text | STRING | Entrada de Texto | Vacío | Cualquier texto | Introduce la descripción (*prompt*) para la imagen que quieres crear. Admite entrada de múltiples líneas para descripciones detalladas. |
| clip | CLIP | Selección de Modelo | Ninguno | Modelos CLIP cargados | Selecciona el modelo CLIP a utilizar para traducir tu descripción en instrucciones para el modelo de IA. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| CONDITIONING | CONDITIONING | Las "instrucciones" procesadas de tu descripción que guían al modelo de IA al generar una imagen. |

## Características del *Prompt*

### Modelos de *Embedding*

Los modelos de *embedding* te permiten aplicar efectos o estilos artísticos específicos. Los formatos soportados incluyen `.safetensors`, `.pt` y `.bin`. Para usar un modelo de *embedding*:

1. Coloca el archivo en la carpeta `ComfyUI/models/embeddings`.
2. Referéncialo en tu texto usando `embedding:nombre_del_modelo`.

Ejemplo: Si tienes un modelo llamado `EasyNegative.pt` en tu carpeta `ComfyUI/models/embeddings`, entonces puedes usarlo así:

```
worst quality, embedding:EasyNegative, bad quality
```

**IMPORTANTE**: Al usar modelos de *embedding*, verifica que el nombre del archivo coincida y sea compatible con la arquitectura de tu modelo. Por ejemplo, un *embedding* diseñado para SD1.5 no funcionará correctamente para un modelo SDXL.

### Ajuste de Peso del *Prompt*

Puedes ajustar la importancia de ciertas partes de tu descripción usando paréntesis. Por ejemplo:

- `(beautiful:1.2)` aumenta el peso de "beautiful".
- `(beautiful:0.8)` disminuye el peso de "beautiful".
- Los paréntesis simples `(beautiful)` aplicarán un peso por defecto de 1.1.

Puedes usar los atajos de teclado `ctrl + flecha arriba/abajo` para ajustar rápidamente los pesos. El tamaño del paso de ajuste de peso se puede modificar en la configuración.

Si deseas incluir paréntesis literales en tu *prompt* sin cambiar el peso, puedes escaparlos usando una barra invertida, por ejemplo: `\(palabra\)`.

### *Prompts* Dinámicos / Comodín

Usa `{}` para crear *prompts* dinámicos. Por ejemplo, `{day|night|morning}` seleccionará aleatoriamente una opción cada vez que se procese el *prompt*.

Si deseas incluir llaves literales en tu *prompt* sin activar el comportamiento dinámico, puedes escaparlas usando una barra invertida, por ejemplo: `\{palabra\}`.

### Comentarios en los *Prompts*

Puedes agregar comentarios que se excluyan del *prompt* usando:

- `//` para comentar una sola línea.
- `/* */` para comentar una sección o múltiples líneas.

Ejemplo:

```
// esta línea se excluye del prompt.
un paisaje hermoso, /* esta parte se ignora */ alta calidad
```
