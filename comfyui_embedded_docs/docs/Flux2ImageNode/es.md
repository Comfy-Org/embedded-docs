# Flux.2 Image

Flux.2 Image

Genere imágenes usando el modelo Flux.2 [pro] o Flux.2 [max] a partir de un prompt de texto e imágenes de referencia opcionales. Este nodo envía su solicitud a la API de BFL, consulta el resultado y devuelve la imagen generada como un tensor.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `modelo` | La versión del modelo Flux.2 a utilizar. Seleccionar un modelo desbloquea parámetros adicionales para ancho, alto e imágenes de referencia opcionales. | DYNAMIC_COMBO | Sí | "Flux.2 [pro]"<br>"Flux.2 [max]" |
| `prompt` | Prompt para la generación o edición de la imagen (por defecto: cadena vacía). | STRING | Sí | N/A |
| `semilla` | La semilla aleatoria utilizada para crear el ruido. Se puede configurar para aleatorizar después de cada generación (por defecto: 0). | INT | Sí | 0 a 18446744073709551615 |

### Entradas de Flux.2 [pro] y Flux.2 [max]

Compartidas por ambos modelos — los conjuntos de parámetros son idénticos.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `ancho` | El ancho de la imagen generada en píxeles (por defecto: 1024). | INT | Sí | 256 a 2048 (step 32) |
| `altura` | El alto de la imagen generada en píxeles (por defecto: 768). | INT | Sí | 256 a 2048 (step 32) |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `model.images` | Imagen(es) de referencia opcional(es) para la generación de imagen a imagen. Hasta 8 imágenes. Ranura ampliable: conecte de 1 a 8 elementos (`image_1`...`image_8`). | IMAGE | No | 0 a 8 images |

**Nota:**
- El número máximo de imágenes de referencia es 8. Si se proporcionan más de 8 imágenes, se produce un error.
- Los valores de `model.width` y `model.height` afectan el costo de generación. El costo también depende del modelo seleccionado y de si se proporcionan imágenes de referencia.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `image` | La imagen generada como un tensor, descargada desde el resultado de la API de BFL. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2ImageNode/es.md)

---
**Source fingerprint (SHA-256):** `2994564757e1c66ac6da7b45d227b27ceb0020ac6fc9e8cbe2b53fe9f70bc195`
