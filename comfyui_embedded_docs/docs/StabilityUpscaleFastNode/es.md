> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleFastNode/es.md)

# Nodo de Escalado Rápido de Estabilidad

Escala rápidamente una imagen mediante una llamada a la API de Stability, aumentando su tamaño 4 veces respecto al original. Este nodo está diseñado específicamente para escalar imágenes de baja calidad o comprimidas, enviándolas al servicio de escalado rápido de Stability AI.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se va a escalar |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `output` | IMAGE | La imagen escalada devuelta por la API de Stability AI |

---
**Source fingerprint (SHA-256):** `0f349c6834807d43173e628abbee91a3a26f587f4bd5453443a9f5754ea8aeeb`
