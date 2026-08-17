# ModelMergeSD35_Large

El nodo ModelMergeSD35_Large le permite fusionar dos modelos Stable Diffusion 3.5 Large combinando la influencia de diferentes componentes del modelo. Proporciona un control preciso sobre cuánto contribuye cada parte del segundo modelo al modelo fusionado final, desde las capas de incrustación hasta los bloques conjuntos y la capa final.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model1` | El modelo base que sirve de base para la fusión | MODEL | Sí | - |
| `model2` | El modelo secundario cuyos componentes se fusionarán en el modelo base | MODEL | Sí | - |
| `pos_embed.` | Controla cuánto de la incrustación de posición del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `x_embedder.` | Controla cuánto del módulo de incrustación x del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `context_embedder.` | Controla cuánto del módulo de incrustación de contexto del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `y_embedder.` | Controla cuánto del módulo de incrustación y del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `t_embedder.` | Controla cuánto del módulo de incrustación t del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.0.` | Controla cuánto del bloque conjunto 0 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.1.` | Controla cuánto del bloque conjunto 1 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.2.` | Controla cuánto del bloque conjunto 2 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.3.` | Controla cuánto del bloque conjunto 3 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.4.` | Controla cuánto del bloque conjunto 4 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.5.` | Controla cuánto del bloque conjunto 5 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.6.` | Controla cuánto del bloque conjunto 6 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.7.` | Controla cuánto del bloque conjunto 7 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.8.` | Controla cuánto del bloque conjunto 8 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.9.` | Controla cuánto del bloque conjunto 9 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.10.` | Controla cuánto del bloque conjunto 10 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.11.` | Controla cuánto del bloque conjunto 11 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.12.` | Controla cuánto del bloque conjunto 12 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.13.` | Controla cuánto del bloque conjunto 13 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.14.` | Controla cuánto del bloque conjunto 14 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.15.` | Controla cuánto del bloque conjunto 15 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.16.` | Controla cuánto del bloque conjunto 16 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.17.` | Controla cuánto del bloque conjunto 17 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.18.` | Controla cuánto del bloque conjunto 18 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.19.` | Controla cuánto del bloque conjunto 19 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.20.` | Controla cuánto del bloque conjunto 20 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.21.` | Controla cuánto del bloque conjunto 21 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.22.` | Controla cuánto del bloque conjunto 22 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.23.` | Controla cuánto del bloque conjunto 23 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.24.` | Controla cuánto del bloque conjunto 24 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.25.` | Controla cuánto del bloque conjunto 25 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.26.` | Controla cuánto del bloque conjunto 26 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.27.` | Controla cuánto del bloque conjunto 27 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.28.` | Controla cuánto del bloque conjunto 28 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.29.` | Controla cuánto del bloque conjunto 29 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.30.` | Controla cuánto del bloque conjunto 30 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.31.` | Controla cuánto del bloque conjunto 31 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.32.` | Controla cuánto del bloque conjunto 32 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.33.` | Controla cuánto del bloque conjunto 33 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.34.` | Controla cuánto del bloque conjunto 34 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.35.` | Controla cuánto del bloque conjunto 35 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.36.` | Controla cuánto del bloque conjunto 36 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `joint_blocks.37.` | Controla cuánto del bloque conjunto 37 del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |
| `final_layer.` | Controla cuánto de la capa final del modelo2 se fusiona en el modelo fusionado (por defecto: 1.0) | FLOAT | Sí | 0.0 to 1.0 |

**Nota:** Todos los parámetros de fusión aceptan valores de 0.0 a 1.0, donde 0.0 significa ninguna contribución del modelo2 y 1.0 significa contribución completa del modelo2 para ese componente específico. Se incrementan en pasos de 0.01.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo fusionado resultante que combina características de ambos modelos de entrada según los parámetros de fusión especificados | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD35_Large/es.md)

---
**Source fingerprint (SHA-256):** `c489c710e18d01adcf4320d9c010ed587ca5e12babb468448f56d79acdc40f6c`
