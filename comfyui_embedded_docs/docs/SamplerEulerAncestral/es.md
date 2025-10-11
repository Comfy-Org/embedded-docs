> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/es.md)

El nodo SamplerEulerAncestral crea un muestreador Euler Ancestral para generar imágenes. Este muestreador utiliza un enfoque matemático específico que combina la integración de Euler con técnicas de muestreo ancestral para producir variaciones de imagen. El nodo permite configurar el comportamiento del muestreo ajustando parámetros que controlan la aleatoriedad y el tamaño del paso durante el proceso de generación.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | Sí | 0.0 - 100.0 | Controla el tamaño del paso y la estocasticidad del proceso de muestreo (valor por defecto: 1.0) |
| `s_noise` | FLOAT | Sí | 0.0 - 100.0 | Controla la cantidad de ruido añadido durante el muestreo (valor por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Devuelve un muestreador Euler Ancestral configurado que puede utilizarse en el pipeline de muestreo |