> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/es.md)

El nodo SamplerDPMPP_2M_SDE crea un muestreador DPM++ 2M SDE para modelos de difusión. Este muestreador utiliza solucionadores de ecuaciones diferenciales de segundo orden con ecuaciones diferenciales estocásticas para generar muestras. Ofrece diferentes tipos de solucionadores y opciones de manejo de ruido para controlar el proceso de muestreo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `solver_type` | STRING | Sí | `"midpoint"`<br>`"heun"` | El tipo de solucionador de ecuaciones diferenciales a utilizar en el proceso de muestreo |
| `eta` | FLOAT | Sí | 0.0 - 100.0 | Controla la estocasticidad del proceso de muestreo (valor predeterminado: 1.0) |
| `s_noise` | FLOAT | Sí | 0.0 - 100.0 | Controla la cantidad de ruido añadido durante el muestreo (valor predeterminado: 1.0) |
| `noise_device` | STRING | Sí | `"gpu"`<br>`"cpu"` | El dispositivo donde se realizan los cálculos de ruido. Cuando se establece en "cpu", el muestreador utiliza generación de ruido basada en CPU; cuando se establece en "gpu", utiliza generación de ruido basada en GPU para un rendimiento potencialmente más rápido |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `sampler` | SAMPLER | Un objeto muestreador configurado listo para usar en el pipeline de muestreo |

---
**Source fingerprint (SHA-256):** `4a6a16e3494e8270f3707e172f252e7fc4e1b65efbecd3dd086b1a1edc5ba23a`
