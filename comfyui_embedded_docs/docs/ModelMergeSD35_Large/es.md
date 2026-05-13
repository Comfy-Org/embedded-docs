> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD35_Large/es.md)

El nodo `ModelMergeSD35_Large` permite fusionar dos modelos Stable Diffusion 3.5 Large combinando la influencia de diferentes componentes del modelo. Proporciona un control preciso sobre cuánto contribuye cada parte del segundo modelo al modelo fusionado final, desde las capas de incrustación hasta los bloques conjuntos y las capas finales.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|---------------|-----------|-------|-------------|
| `model1` | MODEL | Sí | - | El modelo base que sirve como base para la fusión |
| `model2` | MODEL | Sí | - | El modelo secundario cuyos componentes se fusionarán en el modelo base |
| `pos_embed.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto de la incrustación de posición de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `x_embedder.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del incrustador x de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `context_embedder.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del incrustador de contexto de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `y_embedder.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del incrustador y de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `t_embedder.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del incrustador t de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.0.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 0 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.1.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 1 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.2.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 2 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.3.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 3 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.4.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 4 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.5.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 5 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.6.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 6 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.7.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 7 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.8.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 8 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.9.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 9 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.10.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 10 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.11.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 11 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.12.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 12 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.13.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 13 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.14.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 14 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.15.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 15 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.16.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 16 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.17.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 17 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.18.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 18 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.19.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 19 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.20.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 20 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.21.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 21 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.22.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 22 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.23.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 23 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.24.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 24 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.25.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 25 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.26.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 26 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.27.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 27 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.28.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 28 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.29.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 29 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.30.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 30 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.31.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 31 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.32.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 32 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.33.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 33 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.34.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 34 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.35.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 35 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.36.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 36 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `joint_blocks.37.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del bloque conjunto 37 de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |
| `final_layer.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto de la capa final de `model2` se fusiona en el modelo combinado (predeterminado: 1.0) |

**Nota:** Todos los parámetros de fusión aceptan valores de 0.0 a 1.0, donde 0.0 significa ninguna contribución de `model2` y 1.0 significa contribución completa de `model2` para ese componente específico.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `model` | MODEL | El modelo fusionado resultante que combina características de ambos modelos de entrada según los parámetros de fusión especificados |

---
**Source fingerprint (SHA-256):** `1b491bd96cc40c6098fd8194f66753bc0f7aa485ea5f97b67b4d864cc9615c9a`
