# SamplerDPMPP_SDE

El nodo SamplerDPMPP_SDE crea un muestreador DPM++ SDE (Ecuación Diferencial Estocástica) para su uso en el proceso de muestreo. Este muestreador proporciona un método de muestreo estocástico con parámetros de ruido configurables y selección de dispositivo. Devuelve un objeto muestreador que puede utilizarse en el flujo de trabajo de muestreo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `eta` | Controla la estocasticidad del proceso de muestreo (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 100.0 |
| `s_ruido` | Controla la cantidad de ruido añadido durante el muestreo (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 100.0 |
| `r` | Un parámetro que influye en el comportamiento del muestreo (predeterminado: 0.5) | FLOAT | Sí | 0.0 - 100.0 |
| `dispositivo_ruido` | Selecciona el dispositivo donde se realizan los cálculos de ruido (predeterminado: "gpu") | COMBO | Sí | "gpu"<br>"cpu" |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `sampler` | Devuelve un objeto muestreador DPM++ SDE configurado para su uso en flujos de trabajo de muestreo | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/es.md)

---
**Source fingerprint (SHA-256):** `43b3b3c4b2756a6e7979c12418de1dba79e3e0c0fde2a06505cf0a6825e6ebbf`
