> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/es.md)

El nodo SamplerSASolver implementa un algoritmo de muestreo personalizado para modelos de difusión. Utiliza un enfoque predictor-corrector con configuraciones de orden ajustables y parámetros de ecuaciones diferenciales estocásticas (SDE) para generar muestras a partir del modelo de entrada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo de difusión a utilizar para el muestreo |
| `eta` | FLOAT | No | 0.0 - 10.0 | Controla el factor de escala del tamaño de paso (predeterminado: 1.0) |
| `porcentaje_inicio_sde` | FLOAT | No | 0.0 - 1.0 | El porcentaje inicial para el muestreo SDE (predeterminado: 0.2) |
| `porcentaje_fin_sde` | FLOAT | No | 0.0 - 1.0 | El porcentaje final para el muestreo SDE (predeterminado: 0.8) |
| `s_ruido` | FLOAT | No | 0.0 - 100.0 | Controla la cantidad de ruido añadido durante el muestreo (predeterminado: 1.0) |
| `orden_predictor` | INT | No | 1 - 6 | El orden del componente predictor en el solucionador (predeterminado: 3) |
| `orden_corrector` | INT | No | 0 - 6 | El orden del componente corrector en el solucionador (predeterminado: 4) |
| `usar_pece` | BOOLEAN | No | - | Activa o desactiva el método PECE (Predecir-Evaluar-Corregir-Evaluar) |
| `orden_simple_2` | BOOLEAN | No | - | Activa o desactiva los cálculos simplificados de segundo orden |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `sampler` | SAMPLER | Un objeto muestreador configurado que puede utilizarse con modelos de difusión |

---
**Source fingerprint (SHA-256):** `3de8834281c09d0bd1435e29f0c9ae540a2ea42db142277d07cb655ccf814873`
