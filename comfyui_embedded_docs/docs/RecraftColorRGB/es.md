> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftColorRGB/es.md)

Crea un color Recraft especificando valores individuales de rojo, verde y azul. Este nodo toma valores enteros RGB (0-255) y los convierte en un formato de color Recraft que puede utilizarse en otras operaciones Recraft. También puedes proporcionar opcionalmente una cadena de color Recraft existente para extenderla con el nuevo color.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `r` | INT | Sí | 0-255 | Valor rojo del color (predeterminado: 0) |
| `g` | INT | Sí | 0-255 | Valor verde del color (predeterminado: 0) |
| `b` | INT | Sí | 0-255 | Valor azul del color (predeterminado: 0) |
| `recraft_color` | COLOR | No | - | Cadena de color Recraft existente opcional para extender con el nuevo color RGB |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `recraft_color` | COLOR | El objeto de color Recraft creado que contiene los valores RGB especificados, o la cadena de color extendida si se proporcionó una existente |

---
**Source fingerprint (SHA-256):** `8c3503632d085fa4c1771f92f17008b7b051e9604d9e7d1e7d352cbbbd22dddc`
