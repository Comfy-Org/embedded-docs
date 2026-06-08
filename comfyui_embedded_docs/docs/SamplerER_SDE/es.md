El nodo SamplerER_SDE proporciona métodos de muestreo especializados para modelos de difusión, ofreciendo diferentes tipos de solucionadores que incluyen ER-SDE, SDE de tiempo inverso y enfoques ODE. Permite controlar el comportamiento estocástico y las etapas computacionales del proceso de muestreo. El nodo ajusta automáticamente los parámetros según el tipo de solucionador seleccionado para garantizar un funcionamiento adecuado.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `tipo_solucionador` | El tipo de solucionador a utilizar para el muestreo. Determina el enfoque matemático para el proceso de difusión. | COMBO | Sí | "ER-SDE"<br>"SDE de tiempo inverso"<br>"ODE" |
| `etapa_máxima` | El número máximo de etapas para el proceso de muestreo (predeterminado: 3). Controla la complejidad computacional y la calidad. | INT | No | 1-3 |
| `eta` | Fuerza estocástica del SDE de tiempo inverso (predeterminado: 1.0). Cuando eta=0, se reduce a ODE determinista. Esta configuración no aplica al tipo de solucionador ER-SDE. | FLOAT | No | 0.0-100.0 |
| `s_ruido` | Factor de escalado de ruido para el proceso de muestreo (predeterminado: 1.0). Controla la cantidad de ruido aplicada durante el muestreo. | FLOAT | No | 0.0-100.0 |

**Restricciones de parámetros:**

- Cuando `solver_type` está configurado como "ODE" o cuando se utiliza "SDE de tiempo inverso" con `eta`=0, tanto `eta` como `s_noise` se establecen automáticamente en 0 independientemente de los valores ingresados por el usuario.
- El parámetro `eta` solo afecta al tipo de solucionador "SDE de tiempo inverso" y no tiene efecto en el tipo de solucionador "ER-SDE".

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `sampler` | Un objeto de muestreador configurado que puede utilizarse en el pipeline de muestreo con la configuración de solucionador especificada. | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/es.md)

---
**Source fingerprint (SHA-256):** `bc24ec3c5dc645aebf55ef3392c5f4a40dcf0461b4b77731e8fe7ff397dcfadf`
