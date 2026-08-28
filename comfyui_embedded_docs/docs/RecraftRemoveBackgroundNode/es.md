# Recraft Remove Background

Este nodo elimina el fondo de las imágenes mediante el servicio de la API de Recraft. Procesa cada imagen del lote de entrada y devuelve tanto las imágenes procesadas con fondos transparentes como las máscaras alfa correspondientes que indican las áreas de fondo eliminadas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `imagen` | Las imágenes de entrada que se procesarán para eliminar el fondo. Cada imagen del lote se procesa individualmente. | IMAGE | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | Imágenes procesadas con fondos transparentes (formato RGBA) | IMAGE |
| `mask` | Máscaras de canal alfa que indican las áreas de fondo eliminadas, en formato B,H,W | MASK |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/es.md)

---
**Source fingerprint (SHA-256):** `702dfdf2751d5ca33f23e10c0968496887514a21da7a0c42e3636a0ed4e82311`
