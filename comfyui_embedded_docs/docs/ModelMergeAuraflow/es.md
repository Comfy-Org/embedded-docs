> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAuraflow/es.md)

El nodo ModelMergeAuraflow permite combinar dos modelos diferentes ajustando pesos de mezcla específicos para varios componentes del modelo. Proporciona control detallado sobre cómo se fusionan las diferentes partes de los modelos, desde las capas iniciales hasta las salidas finales. Este nodo es particularmente útil para crear combinaciones personalizadas de modelos con control preciso sobre el proceso de fusión.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sí | - | El primer modelo a fusionar |
| `model2` | MODEL | Sí | - | El segundo modelo a fusionar |
| `init_x_linear.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para la transformación lineal inicial (valor por defecto: 1.0) |
| `positional_encoding` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para componentes de codificación posicional (valor por defecto: 1.0) |
| `cond_seq_linear.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capas lineales de secuencia condicional (valor por defecto: 1.0) |
| `register_tokens` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para componentes de registro de tokens (valor por defecto: 1.0) |
| `t_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para componentes de incrustación temporal (valor por defecto: 1.0) |
| `double_layers.0.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para grupo de capas dobles 0 (valor por defecto: 1.0) |
| `double_layers.1.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para grupo de capas dobles 1 (valor por defecto: 1.0) |
| `double_layers.2.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para grupo de capas dobles 2 (valor por defecto: 1.0) |
| `double_layers.3.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para grupo de capas dobles 3 (valor por defecto: 1.0) |
| `single_layers.0.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 0 (valor por defecto: 1.0) |
| `single_layers.1.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 1 (valor por defecto: 1.0) |
| `single_layers.2.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 2 (valor por defecto: 1.0) |
| `single_layers.3.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 3 (valor por defecto: 1.0) |
| `single_layers.4.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 4 (valor por defecto: 1.0) |
| `single_layers.5.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 5 (valor por defecto: 1.0) |
| `single_layers.6.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 6 (valor por defecto: 1.0) |
| `single_layers.7.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 7 (valor por defecto: 1.0) |
| `single_layers.8.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 8 (valor por defecto: 1.0) |
| `single_layers.9.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 9 (valor por defecto: 1.0) |
| `single_layers.10.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 10 (valor por defecto: 1.0) |
| `single_layers.11.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 11 (valor por defecto: 1.0) |
| `single_layers.12.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 12 (valor por defecto: 1.0) |
| `single_layers.13.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 13 (valor por defecto: 1.0) |
| `single_layers.14.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 14 (valor por defecto: 1.0) |
| `single_layers.15.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 15 (valor por defecto: 1.0) |
| `single_layers.16.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 16 (valor por defecto: 1.0) |
| `single_layers.17.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 17 (valor por defecto: 1.0) |
| `single_layers.18.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 18 (valor por defecto: 1.0) |
| `single_layers.19.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 19 (valor por defecto: 1.0) |
| `single_layers.20.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 20 (valor por defecto: 1.0) |
| `single_layers.21.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 21 (valor por defecto: 1.0) |
| `single_layers.22.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 22 (valor por defecto: 1.0) |
| `single_layers.23.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 23 (valor por defecto: 1.0) |
| `single_layers.24.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 24 (valor por defecto: 1.0) |
| `single_layers.25.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 25 (valor por defecto: 1.0) |
| `single_layers.26.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 26 (valor por defecto: 1.0) |
| `single_layers.27.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 27 (valor por defecto: 1.0) |
| `single_layers.28.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 28 (valor por defecto: 1.0) |
| `single_layers.29.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 29 (valor por defecto: 1.0) |
| `single_layers.30.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 30 (valor por defecto: 1.0) |
| `single_layers.31.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para capa simple 31 (valor por defecto: 1.0) |
| `modF.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para componentes modF (valor por defecto: 1.0) |
| `final_linear.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla para transformación lineal final (valor por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo fusionado que combina características de ambos modelos de entrada según los pesos de mezcla especificados |