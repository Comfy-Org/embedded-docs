# SamplerSASolver

El nodo SamplerSASolver implementa un algoritmo de muestreo personalizado para modelos de difusión. Utiliza un enfoque predictor-corrector con ajustes de orden configurables y parámetros de ecuaciones diferenciales estocásticas (SDE) para generar muestras a partir del modelo de entrada.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | El modelo de difusión a utilizar para el muestreo | MODEL | Sí | - |
| `eta` | Controla el factor de escala del tamaño de paso (predeterminado: 1.0) | FLOAT | No | 0.0 - 10.0 |
| `sde_start_percent` | El porcentaje inicial del proceso de eliminación de ruido donde comienza el muestreo SDE, convertido a un valor sigma usando el programa de muestreo del modelo (predeterminado: 0.2) | FLOAT | No | 0.0 - 1.0 |
| `sde_end_percent` | El porcentaje final del proceso de eliminación de ruido donde se detiene el muestreo SDE, convertido a un valor sigma usando el programa de muestreo del modelo (predeterminado: 0.8) | FLOAT | No | 0.0 - 1.0 |
| `s_noise` | Controla la cantidad de ruido añadido durante el muestreo (predeterminado: 1.0) | FLOAT | No | 0.0 - 100.0 |
| `predictor_order` | El orden del componente predictor en el solucionador (predeterminado: 3) | INT | No | 1 - 6 |
| `corrector_order` | El orden del componente corrector en el solucionador (predeterminado: 4) | INT | No | 0 - 6 |
| `use_pece` | Activa o desactiva el método PECE (Predict-Evaluate-Correct-Evaluate) | BOOLEAN | No | - |
| `simple_order_2` | Activa o desactiva los cálculos simplificados de segundo orden | BOOLEAN | No | - |

Nota: Todas las entradas excepto `model` son parámetros avanzados, ocultos por defecto en la interfaz del nodo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `sampler` | Un objeto muestreador configurado que puede utilizarse con modelos de difusión | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/es.md)

---
**Source fingerprint (SHA-256):** `31da2d436665bf533c28b32248f632edab8f6d92372402904702ae954230f98d`
