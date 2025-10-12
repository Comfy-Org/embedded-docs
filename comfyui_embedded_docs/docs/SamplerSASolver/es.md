> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/es.md)

El nodo SamplerSASolver implementa un algoritmo de muestreo personalizado para modelos de difusión. Utiliza un enfoque predictor-corrector con configuraciones de orden ajustables y parámetros de ecuaciones diferenciales estocásticas (SDE) para generar muestras a partir del modelo de entrada.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo de difusión a utilizar para el muestreo |
| `eta` | FLOAT | Sí | 0.0 - 10.0 | Controla el factor de escala del tamaño del paso (por defecto: 1.0) |
| `sde_start_percent` | FLOAT | Sí | 0.0 - 1.0 | El porcentaje inicial para el muestreo SDE (por defecto: 0.2) |
| `sde_end_percent` | FLOAT | Sí | 0.0 - 1.0 | El porcentaje final para el muestreo SDE (por defecto: 0.8) |
| `s_noise` | FLOAT | Sí | 0.0 - 100.0 | Controla la cantidad de ruido añadido durante el muestreo (por defecto: 1.0) |
| `predictor_order` | INT | Sí | 1 - 6 | El orden del componente predictor en el solucionador (por defecto: 3) |
| `corrector_order` | INT | Sí | 0 - 6 | El orden del componente corrector en el solucionador (por defecto: 4) |
| `use_pece` | BOOLEAN | Sí | - | Habilita o deshabilita el método PECE (Predecir-Evaluar-Corregir-Evaluar) |
| `simple_order_2` | BOOLEAN | Sí | - | Habilita o deshabilita los cálculos simplificados de segundo orden |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Un objeto sampler configurado que puede utilizarse con modelos de difusión |
