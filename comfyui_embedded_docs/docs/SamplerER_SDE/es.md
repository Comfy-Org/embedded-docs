# SamplerER_SDE

El nodo SamplerER_SDE proporciona métodos de muestreo especializados para modelos de difusión, ofreciendo tres tipos de solver: ER-SDE, Reverse-time SDE y ODE. Permite controlar el comportamiento estocástico y el número de etapas computacionales del proceso de muestreo. El nodo ajusta automáticamente la configuración de ruido cuando se selecciona el solver ODE o una configuración determinista (`eta`=0).

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `solver_type` | El tipo de solver a utilizar para el muestreo. Determina el comportamiento de escalado de ruido del proceso de difusión (por defecto: "ER-SDE"). | COMBO | Sí | "ER-SDE"<br>"Reverse-time SDE"<br>"ODE" |
| `max_stage` | El número máximo de etapas para el proceso de muestreo (por defecto: 3). Controla la complejidad computacional y la calidad. Parámetro avanzado. | INT | Sí | 1-3 |
| `eta` | Intensidad estocástica de las SDE.<br>Cuando eta=0, se reducen a ODE determinista.<br>Un eta grande puede causar salidas inválidas. Si esto ocurre, intenta disminuir este valor. (por defecto: 1.0). Parámetro avanzado. | FLOAT | Sí | 0.0-10.0 |
| `s_noise` | Factor de escalado de ruido para el proceso de muestreo (por defecto: 1.0). Controla la cantidad de ruido aplicada durante el muestreo. Parámetro avanzado. | FLOAT | Sí | 0.0-100.0 |

**Restricciones de parámetros:**

- Cuando `solver_type` es "ODE" o `eta` es 0, el nodo fuerza `s_noise` a 0.0 y cambia el solver a "ODE".
- `eta` afecta tanto al tipo de solver "ER-SDE" como a "Reverse-time SDE". Los valores grandes pueden causar salidas inválidas.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `sampler` | Un objeto sampler configurado que puede utilizarse en el pipeline de muestreo con la configuración de solver especificada. | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/es.md)

---
**Source fingerprint (SHA-256):** `5299ae9b45444cdc7c36bcb3c5e5a0600f9f904e57ae614554033434afdffd30`
