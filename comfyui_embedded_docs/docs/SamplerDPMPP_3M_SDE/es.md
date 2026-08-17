# SamplerDPMPP_3M_SDE

El nodo SamplerDPMPP_3M_SDE crea un muestreador DPM++ 3M SDE para usar en el proceso de muestreo. Este muestreador utiliza un método de ecuación diferencial estocástica multietapa de tercer orden con parámetros de ruido configurables. El nodo permite elegir si los cálculos de ruido se realizan en la GPU o la CPU.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `eta` | Controla la estocasticidad del proceso de muestreo (por defecto: 1.0) | FLOAT | Sí | 0.0 - 100.0 |
| `s_noise` | Controla la cantidad de ruido agregado durante el muestreo (por defecto: 1.0) | FLOAT | Sí | 0.0 - 100.0 |
| `noise_device` | Selecciona el dispositivo para los cálculos de ruido, ya sea GPU o CPU (por defecto: "gpu") | COMBO | Sí | "gpu"<br>"cpu" |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `sampler` | Devuelve un objeto muestreador configurado para usar en flujos de trabajo de muestreo | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/es.md)

---
**Source fingerprint (SHA-256):** `0f624398c67e50639fc41384b50b91bab93797bd785dda25f1f5fc649e46825b`
