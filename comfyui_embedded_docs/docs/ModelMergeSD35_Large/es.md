El nodo `ModelMergeSD35_Large` permite fusionar dos modelos Stable Diffusion 3.5 Large combinando la influencia de diferentes componentes del modelo. Proporciona un control preciso sobre cuánto contribuye cada parte del segundo modelo al modelo fusionado final, desde las capas de incrustación hasta los bloques conjuntos y las capas finales.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model1` | El modelo base que sirve como base para la fusión | MODEL | Sí | - |
| `model2` | El modelo secundario cuyos componentes se fusionarán en el modelo base | MODEL | Sí | - |
| `pos_embed.` | Controla cuánto de la incrustación de posición de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `x_embedder.` | Controla cuánto del incrustador x de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `context_embedder.` | Controla cuánto del incrustador de contexto de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `y_embedder.` | Controla cuánto del incrustador y de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `t_embedder.` | Controla cuánto del incrustador t de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.0.` | Controla cuánto del bloque conjunto 0 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.1.` | Controla cuánto del bloque conjunto 1 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.2.` | Controla cuánto del bloque conjunto 2 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.3.` | Controla cuánto del bloque conjunto 3 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.4.` | Controla cuánto del bloque conjunto 4 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.5.` | Controla cuánto del bloque conjunto 5 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.6.` | Controla cuánto del bloque conjunto 6 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.7.` | Controla cuánto del bloque conjunto 7 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.8.` | Controla cuánto del bloque conjunto 8 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.9.` | Controla cuánto del bloque conjunto 9 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.10.` | Controla cuánto del bloque conjunto 10 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.11.` | Controla cuánto del bloque conjunto 11 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.12.` | Controla cuánto del bloque conjunto 12 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.13.` | Controla cuánto del bloque conjunto 13 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.14.` | Controla cuánto del bloque conjunto 14 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.15.` | Controla cuánto del bloque conjunto 15 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.16.` | Controla cuánto del bloque conjunto 16 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.17.` | Controla cuánto del bloque conjunto 17 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.18.` | Controla cuánto del bloque conjunto 18 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.19.` | Controla cuánto del bloque conjunto 19 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.20.` | Controla cuánto del bloque conjunto 20 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.21.` | Controla cuánto del bloque conjunto 21 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.22.` | Controla cuánto del bloque conjunto 22 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.23.` | Controla cuánto del bloque conjunto 23 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.24.` | Controla cuánto del bloque conjunto 24 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.25.` | Controla cuánto del bloque conjunto 25 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.26.` | Controla cuánto del bloque conjunto 26 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.27.` | Controla cuánto del bloque conjunto 27 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.28.` | Controla cuánto del bloque conjunto 28 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.29.` | Controla cuánto del bloque conjunto 29 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.30.` | Controla cuánto del bloque conjunto 30 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.31.` | Controla cuánto del bloque conjunto 31 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.32.` | Controla cuánto del bloque conjunto 32 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.33.` | Controla cuánto del bloque conjunto 33 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.34.` | Controla cuánto del bloque conjunto 34 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.35.` | Controla cuánto del bloque conjunto 35 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.36.` | Controla cuánto del bloque conjunto 36 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `joint_blocks.37.` | Controla cuánto del bloque conjunto 37 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `final_layer.` | Controla cuánto de la capa final de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |

**Nota:** Todos los parámetros de fusión aceptan valores de 0.0 a 1.0, donde 0.0 significa ninguna contribución de `model2` y 1.0 significa contribución completa de `model2` para ese componente específico.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model` | El modelo fusionado resultante que combina características de ambos modelos de entrada según los parámetros de fusión especificados | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD35_Large/es.md)

---
**Source fingerprint (SHA-256):** `1b491bd96cc40c6098fd8194f66753bc0f7aa485ea5f97b67b4d864cc9615c9a`
