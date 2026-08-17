# SamplerDPMPP_2S_Ancestral

El nodo SamplerDPMPP_2S_Ancestral crea un muestreador que utiliza el método de muestreo ancestral DPM++ 2S para generar imágenes. Este muestreador combina elementos deterministas y estocásticos para producir resultados variados manteniendo cierta consistencia. Permite controlar la aleatoriedad y los niveles de ruido durante el proceso de muestreo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `eta` | Controla la cantidad de ruido estocástico añadido durante el muestreo (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 100.0 (paso 0.01) |
| `s_noise` | Controla la escala del ruido aplicado durante el proceso de muestreo (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 100.0 (paso 0.01) |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `sampler` | Devuelve un objeto muestreador configurado que se puede utilizar en el pipeline de muestreo | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2S_Ancestral/es.md)

---
**Source fingerprint (SHA-256):** `8d20ec21e6c699965753413d9ef8b6191553c4b7b606d93c10470aa9d988a308`
