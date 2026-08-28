# Posprocesar salida de SeedVR2

Este nodo alinea la imagen generada con la imagen redimensionada original y aplica una corrección de color opcional. Toma la salida de un proceso de ampliación SeedVR2 y la ajusta para que coincida con los colores y las dimensiones de la imagen de referencia original.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `imágenes` | La imagen generada a procesar. | IMAGE | Sí | - |
| `imágenes_redimensionadas_originales` | La imagen redimensionada original antes del preprocesamiento, utilizada como referencia. | IMAGE | Sí | - |
| `método_de_corrección_de_color` | Método para ajustar los colores de la imagen generada a los de la imagen original. lab: transfiere el color en el espacio CIELAB, preservando el detalle (el más fiel). wavelet: transfiere el color de baja frecuencia, conservando el detalle de alta frecuencia ampliado. adain: iguala la media/desviación estándar por canal (el más rápido, tinte global). none: omite la transferencia de color (solo alineación geométrica). (predeterminado: "lab") | COMBO | Sí | `"lab"`<br>`"wavelet"`<br>`"adain"`<br>`"none"` |

**Nota:** Ambas entradas pueden ser tensores 4-D (lote, altura, ancho, canales) o 5-D (lote, fotogramas, altura, ancho, canales). El nodo recorta ambas al lote, número de fotogramas, altura y ancho más pequeños, por lo que no es necesario que coincidan exactamente. La altura y el ancho de salida se redondean hacia abajo a números pares. Si la imagen de referencia tiene un canal alfa (4 canales), ese canal alfa se preserva y se aplica a la salida.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `imágenes` | La imagen alineada y con corrección de color. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2PostProcessing/es.md)

---
**Source fingerprint (SHA-256):** `00a3a3ef06edc7e0eca8f67a96095920a3e0e885dac3fb676d081e4c4c30bec5`
