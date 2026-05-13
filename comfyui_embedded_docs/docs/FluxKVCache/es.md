> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKVCache/es.md)

El nodo Caché KV de Flux permite una optimización de Caché Clave-Valor (KV) para modelos de la familia Flux. Esta optimización mejora el rendimiento al utilizar imágenes de referencia mediante el almacenamiento en caché de ciertos cálculos, lo que puede acelerar el proceso de generación.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `modelo` | MODEL | Sí | | El modelo al que se aplicará la optimización de Caché KV. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `modelo` | MODEL | El modelo modificado con la optimización de Caché KV habilitada. |

---
**Source fingerprint (SHA-256):** `530c660ae23607d4035815826ae73cdcbebe7693ba47a3b0fe98e69f329b9e86`
