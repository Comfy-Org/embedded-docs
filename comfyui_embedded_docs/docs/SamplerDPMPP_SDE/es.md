> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/es.md)

El nodo SamplerDPMPP_SDE crea un muestreador DPM++ SDE (Ecuación Diferencial Estocástica) para su uso en el proceso de muestreo. Este muestreador proporciona un método de muestreo estocástico con parámetros de ruido configurables y selección de dispositivo. Devuelve un objeto muestreador que puede utilizarse en el flujo de trabajo de muestreo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `eta` | FLOAT | Sí | 0.0 - 100.0 | Controla la estocasticidad del proceso de muestreo (predeterminado: 1.0) |
| `s_noise` | FLOAT | Sí | 0.0 - 100.0 | Controla la cantidad de ruido añadido durante el muestreo (predeterminado: 1.0) |
| `r` | FLOAT | Sí | 0.0 - 100.0 | Un parámetro que influye en el comportamiento del muestreo (predeterminado: 0.5) |
| `noise_device` | COMBO | Sí | "gpu"<br>"cpu" | Selecciona el dispositivo donde se realizan los cálculos de ruido (predeterminado: "gpu") |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `sampler` | SAMPLER | Devuelve un objeto muestreador DPM++ SDE configurado para su uso en flujos de trabajo de muestreo |

---
**Source fingerprint (SHA-256):** `43b3b3c4b2756a6e7979c12418de1dba79e3e0c0fde2a06505cf0a6825e6ebbf`
