# ModelMergeAuraflow

El nodo ModelMergeAuraflow te permite fusionar dos modelos diferentes ajustando pesos de fusión específicos para varios componentes del modelo. Proporciona un control detallado sobre cómo se fusionan las diferentes partes de los modelos, desde las capas iniciales hasta las salidas finales. Este nodo es especialmente útil para crear combinaciones de modelos personalizadas con un control preciso sobre el proceso de fusión.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo1` | El primer modelo a fusionar | MODEL | Sí | - |
| `modelo2` | El segundo modelo a fusionar | MODEL | Sí | - |
| `init_x_linear.` | Peso de fusión para la transformación lineal inicial (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `codificación_posicional` | Peso de fusión para los componentes de codificación posicional (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `cond_seq_linear.` | Peso de fusión para las capas lineales de secuencia condicional (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `registrar_tokens` | Peso de fusión para los componentes de registro de tokens (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `t_embedder.` | Peso de fusión para los componentes de incrustación de tiempo (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `double_layers.0.` | Peso de fusión para el grupo de capas dobles 0 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `double_layers.1.` | Peso de fusión para el grupo de capas dobles 1 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `double_layers.2.` | Peso de fusión para el grupo de capas dobles 2 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `double_layers.3.` | Peso de fusión para el grupo de capas dobles 3 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.0.` | Peso de fusión para la capa individual 0 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.1.` | Peso de fusión para la capa individual 1 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.2.` | Peso de fusión para la capa individual 2 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.3.` | Peso de fusión para la capa individual 3 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.4.` | Peso de fusión para la capa individual 4 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.5.` | Peso de fusión para la capa individual 5 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.6.` | Peso de fusión para la capa individual 6 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.7.` | Peso de fusión para la capa individual 7 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.8.` | Peso de fusión para la capa individual 8 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.9.` | Peso de fusión para la capa individual 9 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.10.` | Peso de fusión para la capa individual 10 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.11.` | Peso de fusión para la capa individual 11 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.12.` | Peso de fusión para la capa individual 12 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.13.` | Peso de fusión para la capa individual 13 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.14.` | Peso de fusión para la capa individual 14 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.15.` | Peso de fusión para la capa individual 15 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.16.` | Peso de fusión para la capa individual 16 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.17.` | Peso de fusión para la capa individual 17 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.18.` | Peso de fusión para la capa individual 18 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.19.` | Peso de fusión para la capa individual 19 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.20.` | Peso de fusión para la capa individual 20 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.21.` | Peso de fusión para la capa individual 21 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.22.` | Peso de fusión para la capa individual 22 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.23.` | Peso de fusión para la capa individual 23 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.24.` | Peso de fusión para la capa individual 24 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.25.` | Peso de fusión para la capa individual 25 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.26.` | Peso de fusión para la capa individual 26 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.27.` | Peso de fusión para la capa individual 27 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.28.` | Peso de fusión para la capa individual 28 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.29.` | Peso de fusión para la capa individual 29 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.30.` | Peso de fusión para la capa individual 30 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.31.` | Peso de fusión para la capa individual 31 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `modF.` | Peso de fusión para los componentes modF (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `final_linear.` | Peso de fusión para la transformación lineal final (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo fusionado que combina características de ambos modelos de entrada según los pesos de fusión especificados | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAuraflow/es.md)

---
**Source fingerprint (SHA-256):** `e9d3d81b2a3f81b082f9dc9f662f4e51df66f1f077e2899a1fea9a7061c4a97b`
