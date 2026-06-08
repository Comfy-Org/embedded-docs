# Pre-Procesar Entrada SeedVR2

Este nodo rellena una imagen redimensionada para prepararla para el modelo SeedVR2. Elimina el canal alfa durante el procesamiento, el cual es restaurado posteriormente por el nodo complementario Post-Procesar Salida SeedVR2 utilizando la imagen redimensionada original.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `resized_images` | La imagen redimensionada a procesar. | IMAGE | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `images` | La imagen rellenada lista para el procesamiento SeedVR2. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Preprocess/es.md)

---
**Source fingerprint (SHA-256):** `b8135d0e27f75a673f52d080c6704de8cc86d15b5d16eca055d55e2d20837dc7`
