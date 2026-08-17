# Qwen Image 3 Edit

Este nodo utiliza los modelos Qwen-Image 3.0 para editar o combinar hasta 3 imágenes de referencia guiadas por un prompt de texto. Seleccione un modelo, proporcione el prompt y las imágenes de referencia, y el nodo devolverá una o más imágenes generadas.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a utilizar. Esta selección también incluye el prompt de texto, hasta 3 entradas de imágenes de referencia y un prompt negativo opcional. | DYNAMIC_COMBO | Sí | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `size` | Resolución de salida. "match input" reutiliza el tamaño de la primera imagen de referencia, "auto" permite que el modelo elija un tamaño con la misma relación de aspecto, "custom" establece un ancho y un alto explícitos. | DYNAMIC_COMBO | Sí | "match input"<br>"auto"<br>"custom" |
| `n` | Número de imágenes a generar, devueltas como un lote. (por defecto: 1) | INT | No | 1 a 6 |
| `seed` | Semilla a utilizar para la generación. (por defecto: 42) | INT | No | 0 a 2147483647 |
| `prompt_extend` | Si se debe mejorar el prompt con asistencia de IA. (por defecto: True) | BOOLEAN | No | True<br>False |
| `watermark` | Si se debe añadir una marca de agua generada por IA al resultado. (por defecto: False) | BOOLEAN | No | True<br>False |

### Entradas de qwen-image-3.0-pro y qwen-image-3.0

Ambos modelos comparten los mismos subparámetros.

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Instrucciones de edición. Admite inglés y chino, y referencias al estilo @Image1 a las imágenes de entrada. (por defecto: "") | STRING | Sí | - |
| `negative_prompt` | Prompt negativo que describe lo que se debe evitar. (por defecto: "") | STRING | No | - |

### Entradas de referencia

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `images` | Ranura ampliable: conecte de 1 a 3 imágenes de referencia (`image_1`, `image_2`, `image_3`). Refiérase a ellas en el prompt como @Image1, @Image2, @Image3, numeradas en el orden de entrada; una entrada por lotes cuenta una vez por imagen. | IMAGE | Sí | 1 a 3 |

### Entradas de tamaño personalizado

Se muestran cuando `size` está establecido en "custom".

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `width` | Ancho de salida. El área total de píxeles debe estar entre 512x512 y 2560x2560; la relación de aspecto debe estar entre 1:8 y 8:1. (por defecto: 1024) | INT | Sí (cuando `size` es "custom") | 256 a 2560, paso 16 |
| `height` | Alto de salida. El área total de píxeles debe estar entre 512x512 y 2560x2560; la relación de aspecto debe estar entre 1:8 y 8:1. (por defecto: 1024) | INT | Sí (cuando `size` es "custom") | 256 a 2560, paso 16 |

### Restricciones

- El prompt de texto es obligatorio y debe contener al menos un carácter.
- Se admiten un máximo de 3 imágenes de referencia; se produce un error si se proporcionan más (una entrada por lotes cuenta una vez por imagen).
- Cuando `size` se establece en "custom", se deben proporcionar valores explícitos de ancho y alto, y se validan: el área total de píxeles debe estar entre 262.144 (512x512) y 6.553.600 (2560x2560) píxeles, y la relación de aspecto debe estar entre 1:8 y 8:1.
- Cuando `size` se establece en "match input", se requiere al menos una imagen de referencia porque se utilizan las dimensiones de la primera imagen de referencia; las dimensiones se escalan para ajustarse al área admitida y al rango de relación de aspecto.
- Cuando `size` se establece en "auto", el modelo elige el tamaño de salida preservando la relación de aspecto de entrada.
- Las referencias en el prompt utilizan @Image1, @Image2, @Image3, numeradas en el orden de entrada; una referencia a un índice mayor que el número de imágenes conectadas genera un error. Las etiquetas solo se reconocen en los límites de palabra, por lo que direcciones como user@image1.com se dejan sin cambios.
- Las imágenes de referencia de entrada se reducen a un máximo de 2048x2048 píxeles antes de enviarse a la API. Si la codificación PNG supera el límite de tamaño de la API, se utiliza una codificación JPEG en su lugar.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|-------------|-------------|-----------|
| `IMAGE` | La imagen o imágenes generadas devueltas como un lote. Se devuelven hasta `n` imágenes. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageEditApi/es.md)

---
**Source fingerprint (SHA-256):** `efa8d2b1a039a7b91789c0332b751a5f90ab8dad755ef0e25124d7d1c44d9abb`
