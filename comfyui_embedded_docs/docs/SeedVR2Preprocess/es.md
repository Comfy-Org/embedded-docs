# Preprocesar entrada de SeedVR2

Este nodo prepara una imagen o video redimensionado para el modelo SeedVR2 aplicando un relleno (padding) a la forma que el modelo espera. Durante el procesamiento, elimina el canal alfa; el nodo complementario Post-Process SeedVR2 Output lo restaura más tarde desde la imagen redimensionada original. Los valores de píxeles se limitan al rango 0-1, la altura y el ancho se rellenan a múltiplos de 16, y el número de fotogramas se rellena repitiendo el último fotograma cuando sea necesario.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `imágenes_redimensionadas` | La imagen redimensionada a procesar. | IMAGE | Sí | - |

Nota: La entrada puede ser un solo fotograma, una secuencia de fotogramas o un lote de videos. Si tiene más de 3 canales, el canal alfa se elimina y solo se conserva RGB. El borde más corto de la entrada debe tener al menos 2 píxeles. El relleno espacial se rellena con negro (valor 0), y los recuentos de fotogramas válidos siguen un patrón 4n+1 (1, 5, 9, 13, ...).

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `imágenes` | La imagen rellenada para la codificación VAE. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Preprocess/es.md)

---
**Source fingerprint (SHA-256):** `f4fa433d299feba40696f27ff365c59988e5102112f09536724b5db5b09416bb`
