> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaReferenceNode/es.md)

Este nodo contiene una imagen y un valor de peso para usarse con el nodo Luma Generate Image. Crea una cadena de referencia que puede pasarse a otros nodos Luma para influir en la generación de imágenes. El nodo puede iniciar una nueva cadena de referencia o agregarse a una existente.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | - | Imagen a utilizar como referencia. |
| `weight` | FLOAT | Sí | 0.0 - 1.0 | Peso de la referencia de imagen (predeterminado: 1.0). |
| `luma_ref` | LUMA_REF | No | - | Cadena de referencia Luma existente opcional a la que agregarse. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `luma_ref` | LUMA_REF | La cadena de referencia Luma que contiene la imagen y el peso. |

---
**Source fingerprint (SHA-256):** `1ad653f0ad7c56702f607ebc3c3d117196295e4e3b044a2c6f1aa3db18869a40`
