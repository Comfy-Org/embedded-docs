El nodo `ModelMergeAuraflow` permite combinar dos modelos diferentes ajustando pesos de mezcla específicos para varios componentes del modelo. Proporciona un control detallado sobre cómo se fusionan las diferentes partes de los modelos, desde las capas iniciales hasta las salidas finales. Este nodo es particularmente útil para crear combinaciones de modelos personalizadas con un control preciso sobre el proceso de fusión.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo1` | El primer modelo a fusionar | MODEL | Sí | - |
| `modelo2` | El segundo modelo a fusionar | MODEL | Sí | - |
| `init_x_linear.` | Peso de mezcla para la transformación lineal inicial (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `codificación_posicional` | Peso de mezcla para los componentes de codificación posicional (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `cond_seq_linear.` | Peso de mezcla para las capas lineales de secuencia condicional (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `registrar_tokens` | Peso de mezcla para los componentes de registro de tokens (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `t_embedder.` | Peso de mezcla para los componentes de incrustación temporal (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `double_layers.0.` | Peso de mezcla para el grupo de capas dobles 0 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `double_layers.1.` | Peso de mezcla para el grupo de capas dobles 1 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `double_layers.2.` | Peso de mezcla para el grupo de capas dobles 2 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `double_layers.3.` | Peso de mezcla para el grupo de capas dobles 3 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.0.` | Peso de mezcla para la capa simple 0 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.1.` | Peso de mezcla para la capa simple 1 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.2.` | Peso de mezcla para la capa simple 2 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.3.` | Peso de mezcla para la capa simple 3 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.4.` | Peso de mezcla para la capa simple 4 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.5.` | Peso de mezcla para la capa simple 5 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.6.` | Peso de mezcla para la capa simple 6 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.7.` | Peso de mezcla para la capa simple 7 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.8.` | Peso de mezcla para la capa simple 8 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.9.` | Peso de mezcla para la capa simple 9 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.10.` | Peso de mezcla para la capa simple 10 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.11.` | Peso de mezcla para la capa simple 11 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.12.` | Peso de mezcla para la capa simple 12 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.13.` | Peso de mezcla para la capa simple 13 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.14.` | Peso de mezcla para la capa simple 14 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.15.` | Peso de mezcla para la capa simple 15 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.16.` | Peso de mezcla para la capa simple 16 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.17.` | Peso de mezcla para la capa simple 17 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.18.` | Peso de mezcla para la capa simple 18 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.19.` | Peso de mezcla para la capa simple 19 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.20.` | Peso de mezcla para la capa simple 20 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.21.` | Peso de mezcla para la capa simple 21 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.22.` | Peso de mezcla para la capa simple 22 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.23.` | Peso de mezcla para la capa simple 23 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.24.` | Peso de mezcla para la capa simple 24 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.25.` | Peso de mezcla para la capa simple 25 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.26.` | Peso de mezcla para la capa simple 26 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.27.` | Peso de mezcla para la capa simple 27 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.28.` | Peso de mezcla para la capa simple 28 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.29.` | Peso de mezcla para la capa simple 29 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.30.` | Peso de mezcla para la capa simple 30 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `single_layers.31.` | Peso de mezcla para la capa simple 31 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `modF.` | Peso de mezcla para los componentes modF (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `final_linear.` | Peso de mezcla para la transformación lineal final (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model` | El modelo fusionado que combina características de ambos modelos de entrada según los pesos de mezcla especificados | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAuraflow/es.md)

---
**Source fingerprint (SHA-256):** `c4959321bba252eb24c945343198d72f50d6021d4dac9945f94e3eb28f1bc3c9`
