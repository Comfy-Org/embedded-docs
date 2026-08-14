# QwenImageEditApi

Este nodo utiliza los modelos Qwen-Image 3.0 para editar o combinar hasta 3 imágenes de referencia guiadas por un prompt de texto. Usted proporciona el prompt de texto y las imágenes de referencia, y el nodo devuelve el resultado generado como una o más imágenes.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | Modelo a utilizar. Esta selección también incluye el prompt de texto, hasta 3 entradas de imágenes de referencia y un prompt negativo opcional. | COMBO | Sí | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `size` | Resolución de salida. "match input" reutiliza el tamaño de la primera imagen de referencia, "auto" permite que el modelo elija un tamaño con la misma relación de aspecto, "custom" establece un ancho y una altura explícitos. | COMBO | Sí | "match input"<br>"auto"<br>"custom" |
| `n` | Número de imágenes a generar, devueltas como un lote. (por defecto: 1) | INT | No | 1 a 6 |
| `seed` | Semilla a utilizar para la generación. (por defecto: 42) | INT | No | 0 a 2147483647 |
| `prompt_extend` | Si se debe mejorar el prompt con asistencia de IA. (por defecto: True) | BOOLEAN | No | True<br>False |
| `watermark` | Si se debe añadir una marca de agua generada por IA al resultado. (por defecto: False) | BOOLEAN | No | True<br>False |

### Restricciones

- El prompt de texto es obligatorio y debe contener al menos un carácter.
- Se admite un máximo de 3 imágenes de referencia; se produce un error si se proporcionan más (una entrada por lotes cuenta una vez por imagen).
- Cuando `size` se establece en "custom", se deben proporcionar y validar valores explícitos de ancho y altura.
- Cuando `size` se establece en "match input", se requiere al menos una imagen de referencia porque se utilizan las dimensiones de la primera imagen de referencia.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| IMAGE | La imagen o imágenes generadas devueltas como un lote. Se devuelven hasta `n` imágenes. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageEditApi/es.md)

---
**Source fingerprint (SHA-256):** `efa8d2b1a039a7b91789c0332b751a5f90ab8dad755ef0e25124d7d1c44d9abb`
