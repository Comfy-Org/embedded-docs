# Recraft Remove Background

Este nodo elimina el fondo de las imágenes utilizando el servicio API de Recraft. Procesa cada imagen del lote de entrada y devuelve tanto las imágenes procesadas con fondos transparentes como las máscaras alfa correspondientes que indican las áreas de fondo eliminadas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `image` | La(s) imagen(es) de entrada para procesar la eliminación de fondo | IMAGE | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | Imágenes procesadas con fondos transparentes | IMAGE |
| `mask` | Máscaras de canal alfa que indican las áreas de fondo eliminadas | MASK |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/es.md)

---
**Source fingerprint (SHA-256):** `702dfdf2751d5ca33f23e10c0968496887514a21da7a0c42e3636a0ed4e82311`
