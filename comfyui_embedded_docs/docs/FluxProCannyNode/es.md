> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProCannyNode/es.md)

Genera una imagen utilizando una imagen de control (canny). Este nodo toma una imagen de control y genera una nueva imagen basada en el aviso proporcionado, siguiendo la estructura de bordes detectada en la imagen de control.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `control_image` | IMAGE | Sí | - | La imagen de entrada utilizada para el control de detección de bordes canny |
| `prompt` | STRING | No | - | Aviso para la generación de la imagen (por defecto: cadena vacía) |
| `prompt_upsampling` | BOOLEAN | No | - | Si se debe realizar un sobremuestreo en el aviso. Si está activo, modifica automáticamente el aviso para una generación más creativa, pero los resultados no son deterministas (la misma semilla no producirá exactamente el mismo resultado). (por defecto: False) |
| `canny_low_threshold` | FLOAT | No | 0.01 - 0.99 | Umbral bajo para la detección de bordes Canny; se ignora si `skip_preprocessing` es True (por defecto: 0.1) |
| `canny_high_threshold` | FLOAT | No | 0.01 - 0.99 | Umbral alto para la detección de bordes Canny; se ignora si `skip_preprocessing` es True (por defecto: 0.4) |
| `skip_preprocessing` | BOOLEAN | No | - | Si se debe omitir el preprocesamiento; configúrelo como True si `control_image` ya está procesada con canny, False si es una imagen en bruto. (por defecto: False) |
| `guidance` | FLOAT | No | 1 - 100 | Intensidad de guía para el proceso de generación de la imagen (por defecto: 30) |
| `steps` | INT | No | 15 - 50 | Número de pasos para el proceso de generación de la imagen (por defecto: 50) |
| `seed` | INT | No | 0 - 18446744073709551615 | La semilla aleatoria utilizada para crear el ruido. (por defecto: 0) |

**Nota:** Cuando `skip_preprocessing` está configurado como True, los parámetros `canny_low_threshold` y `canny_high_threshold` se ignoran, ya que se asume que la imagen de control ya está procesada como una imagen de bordes canny. La `control_image` se utiliza directamente como la imagen preprocesada.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `output_image` | IMAGE | La imagen generada basada en la imagen de control y el aviso |

---
**Source fingerprint (SHA-256):** `dedf55a2b2c183519d7f5be0d9a96abbe40716a247f574fc0d50f10f715949a7`
