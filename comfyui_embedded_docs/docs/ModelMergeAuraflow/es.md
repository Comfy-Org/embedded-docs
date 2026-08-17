# ModelMergeAuraflow

ModelMergeAuraflow permite combinar dos modelos diferentes ajustando pesos de fusión específicos para diversos componentes del modelo. Proporciona un control detallado sobre cómo se fusionan las distintas partes de los modelos, desde las capas iniciales hasta las salidas finales, y está diseñado para usarse con arquitecturas de modelo estilo Auraflow. Este nodo es especialmente útil para crear combinaciones de modelos personalizadas con un control preciso sobre el proceso de fusión.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model1` | El primer modelo que se va a fusionar | MODEL | Sí | - |
| `model2` | El segundo modelo que se va a fusionar | MODEL | Sí | - |
| `init_x_linear.` | Peso de fusión para la transformación lineal inicial (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `positional_encoding` | Peso de fusión para los componentes de codificación posicional (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `cond_seq_linear.` | Peso de fusión para las capas lineales de secuencia condicional (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `register_tokens` | Peso de fusión para los componentes de registro de tokens (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `t_embedder.` | Peso de fusión para los componentes de incrustación temporal (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `double_layers.0.` | Peso de fusión para el grupo 0 de capas dobles (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `double_layers.1.` | Peso de fusión para el grupo 1 de capas dobles (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `double_layers.2.` | Peso de fusión para el grupo 2 de capas dobles (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `double_layers.3.` | Peso de fusión para el grupo 3 de capas dobles (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.0.` | Peso de fusión para la capa individual 0 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.1.` | Peso de fusión para la capa individual 1 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.2.` | Peso de fusión para la capa individual 2 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.3.` | Peso de fusión para la capa individual 3 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.4.` | Peso de fusión para la capa individual 4 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.5.` | Peso de fusión para la capa individual 5 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.6.` | Peso de fusión para la capa individual 6 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.7.` | Peso de fusión para la capa individual 7 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.8.` | Peso de fusión para la capa individual 8 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.9.` | Peso de fusión para la capa individual 9 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.10.` | Peso de fusión para la capa individual 10 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.11.` | Peso de fusión para la capa individual 11 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.12.` | Peso de fusión para la capa individual 12 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.13.` | Peso de fusión para la capa individual 13 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.14.` | Peso de fusión para la capa individual 14 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.15.` | Peso de fusión para la capa individual 15 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.16.` | Peso de fusión para la capa individual 16 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.17.` | Peso de fusión para la capa individual 17 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.18.` | Peso de fusión para la capa individual 18 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.19.` | Peso de fusión para la capa individual 19 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.20.` | Peso de fusión para la capa individual 20 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.21.` | Peso de fusión para la capa individual 21 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.22.` | Peso de fusión para la capa individual 22 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.23.` | Peso de fusión para la capa individual 23 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.24.` | Peso de fusión para la capa individual 24 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.25.` | Peso de fusión para la capa individual 25 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.26.` | Peso de fusión para la capa individual 26 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.27.` | Peso de fusión para la capa individual 27 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.28.` | Peso de fusión para la capa individual 28 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.29.` | Peso de fusión para la capa individual 29 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.30.` | Peso de fusión para la capa individual 30 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.31.` | Peso de fusión para la capa individual 31 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `modF.` | Peso de fusión para los componentes modF (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `final_linear.` | Peso de fusión para la transformación lineal final (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo fusionado que combina características de ambos modelos de entrada según los pesos de fusión especificados | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAuraflow/es.md)

---
**Source fingerprint (SHA-256):** `e9d3d81b2a3f81b082f9dc9f662f4e51df66f1f077e2899a1fea9a7061c4a97b`
