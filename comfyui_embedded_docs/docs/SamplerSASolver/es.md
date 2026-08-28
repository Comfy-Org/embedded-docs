# SamplerSASolver

El nodo SamplerSASolver implementa un algoritmo de muestreo personalizado para modelos de difusión. Utiliza un enfoque predictor-corrector con ajustes de orden configurables y parámetros de ecuación diferencial estocástica (SDE) para generar muestras a partir del modelo de entrada.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de difusión que se utilizará para el muestreo | MODEL | Sí | - |
| `eta` | Controla el factor de escala del tamaño de paso (por defecto: 1.0) | FLOAT | No | 0.0 - 10.0 |
| `porcentaje_inicio_sde` | El porcentaje inicial para el muestreo SDE (por defecto: 0.2) | FLOAT | No | 0.0 - 1.0 |
| `porcentaje_fin_sde` | El porcentaje final para el muestreo SDE (por defecto: 0.8) | FLOAT | No | 0.0 - 1.0 |
| `s_ruido` | Controla la cantidad de ruido añadido durante el muestreo (por defecto: 1.0) | FLOAT | No | 0.0 - 100.0 |
| `orden_predictor` | El orden del componente predictor en el solver (por defecto: 3) | INT | No | 1 - 6 |
| `orden_corrector` | El orden del componente corrector en el solver (por defecto: 4) | INT | No | 0 - 6 |
| `usar_pece` | Activa o desactiva el método PECE (Predict-Evaluate-Correct-Evaluate) | BOOLEAN | No | - |
| `orden_simple_2` | Activa o desactiva los cálculos simplificados de segundo orden | BOOLEAN | No | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `sampler` | Un objeto sampler configurado que se puede utilizar con modelos de difusión | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/es.md)

---
**Source fingerprint (SHA-256):** `31da2d436665bf533c28b32248f632edab8f6d92372402904702ae954230f98d`
