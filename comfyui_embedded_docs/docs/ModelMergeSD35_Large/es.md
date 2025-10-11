> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD35_Large/es.md)

El nodo ModelMergeSD35_Large permite combinar dos modelos Stable Diffusion 3.5 Large ajustando la influencia de los diferentes componentes del modelo. Proporciona control preciso sobre cuánto contribuye cada parte del segundo modelo al modelo fusionado final, desde las capas de embedding hasta los bloques conjuntos y las capas finales.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sí | - | El modelo base que sirve como fundamento para la fusión |
| `model2` | MODEL | Sí | - | El modelo secundario cuyos componentes se mezclarán en el modelo base |
| `pos_embed.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del embedding de posición del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `x_embedder.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del x embedder del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `context_embedder.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del context embedder del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `y_embedder.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del y embedder del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `t_embedder.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del t embedder del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.0.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 0 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.1.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 1 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.2.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 2 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.3.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 3 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.4.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 4 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.5.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 5 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.6.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 6 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.7.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 7 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.8.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 8 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.9.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 9 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.10.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 10 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.11.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 11 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.12.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 12 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.13.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 13 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.14.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 14 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.15.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 15 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.16.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 16 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.17.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 17 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.18.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 18 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.19.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 19 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.20.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 20 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.21.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 21 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.22.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 22 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.23.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 23 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.24.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 24 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.25.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 25 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.26.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 26 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.27.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 27 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.28.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 28 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.29.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 29 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.30.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 30 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.31.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 31 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.32.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 32 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.33.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 33 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.34.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 34 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.35.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 35 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.36.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 36 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `joint_blocks.37.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto del joint block 37 del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |
| `final_layer.` | FLOAT | Sí | 0.0 a 1.0 | Controla cuánto de la capa final del model2 se mezcla en el modelo fusionado (valor por defecto: 1.0) |

**Nota:** Todos los parámetros de mezcla aceptan valores de 0.0 a 1.0, donde 0.0 significa ninguna contribución del model2 y 1.0 significa contribución completa del model2 para ese componente específico.

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo fusionado resultante que combina características de ambos modelos de entrada según los parámetros de mezcla especificados |