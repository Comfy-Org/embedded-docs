# SamplerEulerAncestral

El nodo SamplerEulerAncestral crea un muestreador Euler Ancestral para generar imágenes. Este muestreador utiliza un enfoque matemático específico que combina la integración de Euler con técnicas de muestreo ancestral para producir variaciones de imagen. El nodo permite configurar el comportamiento del muestreo ajustando parámetros que controlan la aleatoriedad y el tamaño del paso durante el proceso de generación.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `eta` | Controla el tamaño del paso y la estocasticidad del proceso de muestreo (valor predeterminado: 1.0). Este es un parámetro avanzado. | FLOAT | No | 0.0 - 100.0 |
| `s_noise` | Controla la cantidad de ruido añadido durante el muestreo (valor predeterminado: 1.0). Este es un parámetro avanzado. | FLOAT | No | 0.0 - 100.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `sampler` | Devuelve un muestreador Euler Ancestral configurado que puede utilizarse en el pipeline de muestreo. | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/es.md)

---
**Source fingerprint (SHA-256):** `0d3c1f0ffe01eb6cc17fd53e743713f659218ec19001c670440472ae7d0d3887`
