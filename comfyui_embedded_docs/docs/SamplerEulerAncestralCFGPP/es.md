> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/es.md)

El nodo SamplerEulerAncestralCFGPP crea un muestreador especializado para generar imágenes utilizando el método Euler Ancestral con guía libre de clasificador. Este muestreador combina técnicas de muestreo ancestral con condicionamiento de guía para producir variaciones diversas de imágenes mientras mantiene la coherencia. Permite ajustar finamente el proceso de muestreo a través de parámetros que controlan el ruido y los ajustes del tamaño de paso.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | Sí | 0.0 - 1.0 | Controla el tamaño del paso durante el muestreo, donde valores más altos resultan en actualizaciones más agresivas (valor por defecto: 1.0) |
| `s_noise` | FLOAT | Sí | 0.0 - 10.0 | Ajusta la cantidad de ruido añadido durante el proceso de muestreo (valor por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Devuelve un objeto muestreador configurado que puede ser utilizado en el pipeline de generación de imágenes |