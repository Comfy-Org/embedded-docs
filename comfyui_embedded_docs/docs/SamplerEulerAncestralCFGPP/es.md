> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/es.md)

El nodo SamplerEulerAncestralCFGPP crea un muestreador que utiliza el método Euler Ancestral con guía libre de clasificador (CFG++) para la generación de imágenes. Este muestreador combina técnicas de muestreo ancestral con condicionamiento guiado para producir variaciones diversas de imágenes manteniendo la coherencia, y permite un ajuste fino mediante parámetros que controlan el ruido y las modificaciones en el tamaño del paso.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `eta` | FLOAT | Sí | 0.0 - 1.0 | Controla el tamaño del paso durante el muestreo, donde valores más altos generan actualizaciones más agresivas (predeterminado: 1.0) |
| `s_ruido` | FLOAT | Sí | 0.0 - 10.0 | Ajusta la cantidad de ruido añadido durante el proceso de muestreo (predeterminado: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `sampler` | SAMPLER | Devuelve un objeto muestreador configurado que puede utilizarse en el flujo de trabajo de generación de imágenes |

---
**Source fingerprint (SHA-256):** `7eceec539a6a045db4d9953214add17011ef9d17e663dbbbbbb2bae0cbe40aa2`
