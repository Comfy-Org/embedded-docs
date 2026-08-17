# SamplerDPMPP_SDE

El nodo SamplerDPMPP_SDE crea un muestreador DPM++ SDE (Ecuación Diferencial Estocástica) para usar en el proceso de muestreo. Este muestreador proporciona un método de muestreo estocástico con parámetros de ruido configurables y selección de dispositivo. Devuelve un objeto muestreador que puede utilizarse en el pipeline de muestreo.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `eta` | Controla la estocasticidad del proceso de muestreo (por defecto: 1.0) | FLOAT | Sí | 0.0 - 100.0 |
| `s_noise` | Controla la cantidad de ruido añadido durante el muestreo (por defecto: 1.0) | FLOAT | Sí | 0.0 - 100.0 |
| `r` | Un parámetro que influye en el comportamiento del muestreo (por defecto: 0.5) | FLOAT | Sí | 0.0 - 100.0 |
| `noise_device` | Selecciona el dispositivo donde se realizan los cálculos de ruido (por defecto: "gpu"). Cuando se establece en "cpu", se utiliza el muestreador estándar `dpmpp_sde`; cuando se establece en "gpu", se utiliza el muestreador `dpmpp_sde_gpu`. | COMBO | Sí | "gpu"<br>"cpu" |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `sampler` | Devuelve un objeto muestreador DPM++ SDE configurado para usar en pipelines de muestreo | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/es.md)

---
**Source fingerprint (SHA-256):** `56949712f245abfcc48c09d7d14a1a7778e80ba58535e538484c382d7e0d02c6`
