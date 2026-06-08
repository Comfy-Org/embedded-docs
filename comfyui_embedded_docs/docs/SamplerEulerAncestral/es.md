El nodo SamplerEulerAncestral crea un muestreador Euler Ancestral para generar imágenes. Este muestreador utiliza un enfoque matemático específico que combina la integración de Euler con técnicas de muestreo ancestral para producir variaciones de imagen. El nodo permite configurar el comportamiento del muestreo ajustando parámetros que controlan la aleatoriedad y el tamaño del paso durante el proceso de generación.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `eta` | Controla el tamaño del paso y la estocasticidad del proceso de muestreo (predeterminado: 1.0). Este es un parámetro avanzado. | FLOAT | No | 0.0 - 100.0 |
| `s_ruido` | Controla la cantidad de ruido añadido durante el muestreo (predeterminado: 1.0). Este es un parámetro avanzado. | FLOAT | No | 0.0 - 100.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `sampler` | Devuelve un muestreador Euler Ancestral configurado que puede utilizarse en el proceso de muestreo. | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/es.md)

---
**Source fingerprint (SHA-256):** `4d167de55f003383ccbb4a53daa14496bd931589781d56b62bf282a811669670`
