# SeedVR2PostProcessing

Este nodo alinea la imagen generada con la imagen redimensionada original y aplica corrección de color opcional. Toma la salida de un proceso de ampliación SeedVR2 y la ajusta para que coincida con los colores y dimensiones de la imagen de referencia original.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `images` | La imagen generada a procesar. | IMAGE | Sí | - |
| `original_resized_images` | La imagen redimensionada original antes del preprocesamiento, utilizada como referencia. | IMAGE | Sí | - |
| `color_correction_method` | Método para hacer coincidir los colores de la imagen generada con la imagen original. lab: transfiere color en espacio CIELAB, preservando detalles (más fiel). wavelet: transfiere color de baja frecuencia, manteniendo detalles de alta frecuencia ampliados. adain: iguala media/desviación estándar por canal (más rápido, tono global). none: omite transferencia de color (solo alineación geométrica). (predeterminado: "lab") | COMBO | Sí | `"lab"`<br>`"wavelet"`<br>`"adain"`<br>`"none"` |

**Nota:** Las entradas `images` y `original_resized_images` deben tener dimensiones coincidentes. Si la imagen original tiene un canal alfa (4 canales), este se preservará y aplicará a la salida.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|-------------|-------------|-----------|
| `images` | La imagen procesada con corrección de color aplicada y dimensiones alineadas con la imagen de referencia. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2PostProcessing/es.md)

---
**Source fingerprint (SHA-256):** `befbe8ccd591c8064a07ae4bb8df853c7ce10f3de83ebfa9214755c22faf28b0`
