El nodo SamplerDPMPP_3M_SDE crea un muestreador DPM++ 3M SDE para usar en el proceso de muestreo. Este muestreador utiliza un método de ecuación diferencial estocástica multietapa de tercer orden con parámetros de ruido configurables. El nodo permite elegir si los cálculos de ruido se realizan en la GPU o en la CPU.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `eta` | Controla la estocasticidad del proceso de muestreo (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 100.0 |
| `s_ruido` | Controla la cantidad de ruido añadido durante el muestreo (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 100.0 |
| `dispositivo_ruido` | Selecciona el dispositivo para los cálculos de ruido, ya sea GPU o CPU (predeterminado: "gpu") | COMBO | Sí | "gpu"<br>"cpu" |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `sampler` | Devuelve un objeto muestreador configurado para usar en flujos de trabajo de muestreo | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/es.md)

---
**Source fingerprint (SHA-256):** `817ce8c12245063e5f2f3421f57dd55801aae96dfd8fe1bf3f88f814799b830a`
