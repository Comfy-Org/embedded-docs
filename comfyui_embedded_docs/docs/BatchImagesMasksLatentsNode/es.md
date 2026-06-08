El nodo Combinar Lotes de Imágenes/Máscaras/Latentes combina múltiples entradas del mismo tipo en un solo lote. Detecta automáticamente si las entradas son imágenes, máscaras o representaciones latentes y utiliza el método de agrupación adecuado. Esto es útil para preparar múltiples elementos para su procesamiento por nodos que aceptan entradas por lotes.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `inputs` | Una lista dinámica de entradas que se combinarán en un lote. Puedes agregar entre 1 y 50 elementos. Todos los elementos deben ser del mismo tipo (todas imágenes, todas máscaras o todos latentes). | IMAGE, MASK o LATENT | Sí | 1 a 50 entradas |

**Nota:** El nodo determina automáticamente el tipo de dato (IMAGE, MASK o LATENT) basándose en el primer elemento de la lista `inputs`. Todos los elementos posteriores deben coincidir con este tipo. El nodo fallará si intentas mezclar diferentes tipos de datos.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | Una única salida agrupada en lote. El tipo de dato coincide con el tipo de entrada (IMAGE agrupada, MASK agrupada o LATENT agrupado). | IMAGE, MASK o LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesMasksLatentsNode/es.md)

---
**Source fingerprint (SHA-256):** `6f3037bc00fd8526f42ad2d79a0f27434f58bd6dd0338a585cc707a771ac0989`
