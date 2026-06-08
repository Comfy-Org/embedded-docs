El nodo SamplerDPMPP_2S_Ancestral crea un muestreador que utiliza el método de muestreo DPM++ 2S Ancestral para generar imágenes. Este muestreador combina elementos deterministas y estocásticos para producir resultados variados, manteniendo al mismo tiempo cierta coherencia. Permite controlar los niveles de aleatoriedad y ruido durante el proceso de muestreo.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `eta` | Controla la cantidad de ruido estocástico añadido durante el muestreo (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 100.0 |
| `s_ruido` | Controla la escala del ruido aplicado durante el proceso de muestreo (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 100.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `sampler` | Devuelve un objeto muestreador configurado que puede utilizarse en el proceso de muestreo | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2S_Ancestral/es.md)

---
**Source fingerprint (SHA-256):** `9634c96934850f5b746cd7c8b29727396af534133b8d54b6bdac12e9e0975189`
