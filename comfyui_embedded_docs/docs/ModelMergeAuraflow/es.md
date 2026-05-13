> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAuraflow/es.md)

El nodo `ModelMergeAuraflow` permite combinar dos modelos diferentes ajustando pesos de mezcla específicos para varios componentes del modelo. Proporciona un control detallado sobre cómo se fusionan las diferentes partes de los modelos, desde las capas iniciales hasta las salidas finales. Este nodo es particularmente útil para crear combinaciones de modelos personalizadas con un control preciso sobre el proceso de fusión.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sí | - | El primer modelo a fusionar |
| `model2` | MODEL | Sí | - | El segundo modelo a fusionar |
| `init_x_linear.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la transformación lineal inicial (predeterminado: 1.0) |
| `positional_encoding` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para los componentes de codificación posicional (predeterminado: 1.0) |
| `cond_seq_linear.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para las capas lineales de secuencia condicional (predeterminado: 1.0) |
| `register_tokens` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para los componentes de registro de tokens (predeterminado: 1.0) |
| `t_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para los componentes de incrustación temporal (predeterminado: 1.0) |
| `double_layers.0.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para el grupo de capas dobles 0 (predeterminado: 1.0) |
| `double_layers.1.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para el grupo de capas dobles 1 (predeterminado: 1.0) |
| `double_layers.2.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para el grupo de capas dobles 2 (predeterminado: 1.0) |
| `double_layers.3.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para el grupo de capas dobles 3 (predeterminado: 1.0) |
| `single_layers.0.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 0 (predeterminado: 1.0) |
| `single_layers.1.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 1 (predeterminado: 1.0) |
| `single_layers.2.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 2 (predeterminado: 1.0) |
| `single_layers.3.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 3 (predeterminado: 1.0) |
| `single_layers.4.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 4 (predeterminado: 1.0) |
| `single_layers.5.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 5 (predeterminado: 1.0) |
| `single_layers.6.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 6 (predeterminado: 1.0) |
| `single_layers.7.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 7 (predeterminado: 1.0) |
| `single_layers.8.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 8 (predeterminado: 1.0) |
| `single_layers.9.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 9 (predeterminado: 1.0) |
| `single_layers.10.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 10 (predeterminado: 1.0) |
| `single_layers.11.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 11 (predeterminado: 1.0) |
| `single_layers.12.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 12 (predeterminado: 1.0) |
| `single_layers.13.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 13 (predeterminado: 1.0) |
| `single_layers.14.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 14 (predeterminado: 1.0) |
| `single_layers.15.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 15 (predeterminado: 1.0) |
| `single_layers.16.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 16 (predeterminado: 1.0) |
| `single_layers.17.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 17 (predeterminado: 1.0) |
| `single_layers.18.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 18 (predeterminado: 1.0) |
| `single_layers.19.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 19 (predeterminado: 1.0) |
| `single_layers.20.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 20 (predeterminado: 1.0) |
| `single_layers.21.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 21 (predeterminado: 1.0) |
| `single_layers.22.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 22 (predeterminado: 1.0) |
| `single_layers.23.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 23 (predeterminado: 1.0) |
| `single_layers.24.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 24 (predeterminado: 1.0) |
| `single_layers.25.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 25 (predeterminado: 1.0) |
| `single_layers.26.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 26 (predeterminado: 1.0) |
| `single_layers.27.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 27 (predeterminado: 1.0) |
| `single_layers.28.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 28 (predeterminado: 1.0) |
| `single_layers.29.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 29 (predeterminado: 1.0) |
| `single_layers.30.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 30 (predeterminado: 1.0) |
| `single_layers.31.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la capa simple 31 (predeterminado: 1.0) |
| `modF.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para los componentes modF (predeterminado: 1.0) |
| `final_linear.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la transformación lineal final (predeterminado: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo fusionado que combina características de ambos modelos de entrada según los pesos de mezcla especificados |

---
**Source fingerprint (SHA-256):** `c4959321bba252eb24c945343198d72f50d6021d4dac9945f94e3eb28f1bc3c9`
