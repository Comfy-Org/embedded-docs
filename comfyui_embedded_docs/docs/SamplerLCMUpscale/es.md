# SamplerLCMUpscale

El nodo SamplerLCMUpscale proporciona un método de muestreo especializado que combina el muestreo del Modelo Consistente Latente (LCM) con capacidades de ampliación de imagen. Permite ampliar imágenes durante el proceso de muestreo utilizando varios métodos de interpolación, lo que resulta útil para generar salidas de mayor resolución manteniendo la calidad de la imagen.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `relación_escala` | El factor de escala a aplicar durante la ampliación (predeterminado: 1.0) | FLOAT | No | 0.1 - 20.0 |
| `pasos_escala` | El número de pasos a utilizar para el proceso de ampliación. Use -1 para cálculo automático (predeterminado: -1) | INT | No | -1 - 1000 |
| `método_aumento_escala` | El método de interpolación utilizado para ampliar la imagen | COMBO | Sí | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `sampler` | Devuelve un objeto muestreador configurado que puede utilizarse en el proceso de muestreo | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/es.md)

---
**Source fingerprint (SHA-256):** `fe0d4c8676454a9e8ecf4bb4e149c9b5e22083322447749116d624984d75e73c`
