> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleImageTextDataset/es.md)

Este nodo mezcla una lista de imágenes y una lista de textos de forma conjunta, manteniendo intactos sus emparejamientos. Utiliza una semilla aleatoria para determinar el orden de la mezcla, lo que garantiza que las mismas listas de entrada se mezclarán de la misma manera cada vez que se reutilice la semilla.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `images` | IMAGE | Sí | - | Lista de imágenes a mezclar. |
| `texts` | STRING | Sí | - | Lista de textos a mezclar. |
| `seed` | INT | No | 0 a 18446744073709551615 | Semilla aleatoria. El orden de la mezcla está determinado por este valor (predeterminado: 0). |

**Nota:** Las entradas `images` y `texts` deben ser listas de la misma longitud. El nodo emparejará la primera imagen con el primer texto, la segunda imagen con el segundo texto, y así sucesivamente, antes de mezclar estos pares de forma conjunta.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `images` | IMAGE | La lista mezclada de imágenes. |
| `texts` | STRING | La lista mezclada de textos, manteniendo sus emparejamientos originales con las imágenes. |

---
**Source fingerprint (SHA-256):** `c87cef780c98b1cf2a58a7d5faf4399c85edd647a9fdba693d008152e43d9c99`
