# SamplerEulerAncestralCFG++

El nodo `SamplerEulerAncestralCFGPP` crea un muestreador que utiliza el método Euler Ancestral con guía libre de clasificador (CFG++) para la generación de imágenes. Este muestreador combina técnicas de muestreo ancestral con condicionamiento por guía para producir variaciones de imagen diversas manteniendo la coherencia, y permite un ajuste fino mediante parámetros que controlan el ruido y el tamaño de paso.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `eta` | Controla el tamaño de paso durante el muestreo; valores más altos producen actualizaciones más agresivas (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `s_noise` | Ajusta la cantidad de ruido añadida durante el proceso de muestreo (por defecto: 1.0) | FLOAT | Sí | 0.0 - 10.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `sampler` | Devuelve un objeto de muestreador configurado que puede utilizarse en el pipeline de generación de imágenes | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/es.md)

---
**Source fingerprint (SHA-256):** `de83cb4c3e9aeee60f1554ad1af8181adb4fa62e3d23cec02a6f4396b96500c1`
