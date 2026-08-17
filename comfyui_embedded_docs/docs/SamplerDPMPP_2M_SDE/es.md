# SamplerDPMPP_2M_SDE

El nodo SamplerDPMPP_2M_SDE crea un muestreador DPM++ 2M SDE para modelos de difusión. Este muestreador combina un solucionador de paso múltiple de segundo orden con ruido de ecuación diferencial estocástica (SDE) para generar muestras. Proporciona diferentes tipos de solucionador y opciones de manejo de ruido para controlar el proceso de muestreo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `solver_type` | El tipo de solucionador de ecuaciones diferenciales que se utilizará durante el muestreo: "midpoint" o "heun" (predeterminado: "midpoint") | COMBO | Sí | "midpoint"<br>"heun" |
| `eta` | Controla la cantidad de estocasticidad (aleatoriedad) en el proceso de muestreo (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 100.0 |
| `s_noise` | Controla la cantidad de ruido añadido durante el muestreo (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 100.0 |
| `noise_device` | El dispositivo utilizado para los cálculos de ruido. "gpu" realiza la generación de ruido en la GPU para un rendimiento potencialmente más rápido; "cpu" utiliza la CPU (predeterminado: "gpu") | COMBO | Sí | "gpu"<br>"cpu" |

Nota: Cuando `noise_device` está configurado en "cpu", el nodo crea el muestreador `dpmpp_2m_sde`. Cuando está configurado en "gpu", crea la variante `dpmpp_2m_sde_gpu`, que realiza los cálculos relacionados con el ruido en la GPU.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `sampler` | Un objeto muestreador configurado listo para usar en el pipeline de muestreo | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/es.md)

---
**Source fingerprint (SHA-256):** `42f5f098fa7573ca8a1a6085b72675ee6cb0ae8e7865c5793a815a6ef2495f82`
