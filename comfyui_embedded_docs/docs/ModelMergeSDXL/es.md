# ModelMergeSDXL

El nodo ModelMergeSDXL permite combinar dos modelos SDXL ajustando la influencia de cada modelo en diferentes partes de la arquitectura. Puedes controlar cuánto contribuye cada modelo a las incrustaciones de tiempo, las incrustaciones de etiquetas y varios bloques dentro de la estructura del modelo. Esto crea un modelo híbrido que combina características de ambos modelos de entrada.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model1` | El primer modelo SDXL a fusionar | MODEL | Sí | - |
| `model2` | El segundo modelo SDXL a fusionar | MODEL | Sí | - |
| `time_embed.` | Peso de fusión para las capas de incrustaciones de tiempo (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `label_emb.` | Peso de fusión para las capas de incrustaciones de etiquetas (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.0` | Peso de fusión para el bloque de entrada 0 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.1` | Peso de fusión para el bloque de entrada 1 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.2` | Peso de fusión para el bloque de entrada 2 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.3` | Peso de fusión para el bloque de entrada 3 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.4` | Peso de fusión para el bloque de entrada 4 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.5` | Peso de fusión para el bloque de entrada 5 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.6` | Peso de fusión para el bloque de entrada 6 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.7` | Peso de fusión para el bloque de entrada 7 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.8` | Peso de fusión para el bloque de entrada 8 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `middle_block.0` | Peso de fusión para el bloque intermedio 0 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `middle_block.1` | Peso de fusión para el bloque intermedio 1 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `middle_block.2` | Peso de fusión para el bloque intermedio 2 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.0` | Peso de fusión para el bloque de salida 0 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.1` | Peso de fusión para el bloque de salida 1 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.2` | Peso de fusión para el bloque de salida 2 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.3` | Peso de fusión para el bloque de salida 3 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.4` | Peso de fusión para el bloque de salida 4 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.5` | Peso de fusión para el bloque de salida 5 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.6` | Peso de fusión para el bloque de salida 6 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.7` | Peso de fusión para el bloque de salida 7 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.8` | Peso de fusión para el bloque de salida 8 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `out.` | Peso de fusión para las capas de salida (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

Todos los parámetros de peso de fusión son valores FLOAT obligatorios entre 0.0 y 1.0, con valor predeterminado 1.0, y pueden ajustarse en pasos de 0.01.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `model` | El modelo SDXL fusionado que combina características de ambos modelos de entrada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSDXL/es.md)

---
**Source fingerprint (SHA-256):** `9a1b0645ee19c2eddb274dd6ea3f9a05997115119cc654a7f055d58475745bb2`
