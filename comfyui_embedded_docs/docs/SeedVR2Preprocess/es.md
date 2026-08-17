# Preprocesar entrada de SeedVR2

Este nodo rellena una imagen redimensionada para prepararla para el modelo SeedVR2. Elimina el canal alfa durante el procesamiento, que luego es restaurado por el nodo complementario Post-Process SeedVR2 Output utilizando la imagen redimensionada original.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `resized_images` | La imagen redimensionada a procesar. | IMAGE | Sí | - |

Nota: La entrada puede ser una sola imagen o una secuencia de fotogramas (por ejemplo, fotogramas de un video). Su borde más corto debe tener al menos 2 píxeles. Durante el procesamiento, el canal alfa (si está presente) se elimina, los valores de píxeles se limitan al intervalo [0, 1], y el ancho y la altura se rellenan a múltiplos de 16. Las secuencias de fotogramas se rellenan para que su longitud siga el patrón 1, 5, 9, 13, ... fotogramas.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `images` | La imagen rellenada para la codificación VAE. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Preprocess/es.md)

---
**Source fingerprint (SHA-256):** `f4fa433d299feba40696f27ff365c59988e5102112f09536724b5db5b09416bb`
