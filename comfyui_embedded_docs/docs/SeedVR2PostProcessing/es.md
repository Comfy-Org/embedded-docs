# Posprocesar salida de SeedVR2

Este nodo alinea la imagen generada con la imagen original redimensionada y aplica corrección de color opcional. Toma la salida de un proceso de ampliación SeedVR2 y la ajusta para que coincida con los colores y dimensiones de la imagen de referencia original.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `images` | La imagen generada a procesar. | IMAGE | Sí | - |
| `original_resized_images` | La imagen original redimensionada antes del preprocesamiento, utilizada como referencia. | IMAGE | Sí | - |
| `color_correction_method` | Método para hacer coincidir los colores de la imagen generada con los de la imagen original. lab: transfiere el color en el espacio CIELAB, preservando el detalle (el más fiel). wavelet: transfiere el color de baja frecuencia, manteniendo el detalle de alta frecuencia ampliado. adain: iguala la media/desviación estándar por canal (el más rápido, tinte global). none: omite la transferencia de color (solo alineación geométrica). (predeterminado: "lab") | COMBO | Sí | `"lab"`<br>`"wavelet"`<br>`"adain"`<br>`"none"` |

**Nota:** La salida se recorta a la altura y anchura más pequeñas entre la imagen generada y la de referencia, y las dimensiones finales se redondean hacia abajo a números pares. Si la imagen de referencia tiene un canal alfa (4 canales), este se conserva y se aplica a la salida. Ambas entradas pueden ser tensores de imagen 4D o 5D, y la salida utiliza la misma dimensionalidad que la entrada de imagen generada.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `images` | La imagen alineada y corregida en color. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2PostProcessing/es.md)

---
**Source fingerprint (SHA-256):** `00a3a3ef06edc7e0eca8f67a96095920a3e0e885dac3fb676d081e4c4c30bec5`
