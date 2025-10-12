> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/es.md)

El nodo SamplerLCMUpscale proporciona un método de muestreo especializado que combina el muestreo de Modelo de Consistencia Latente (LCM) con capacidades de aumento de escala de imagen. Permite escalar imágenes durante el proceso de muestreo utilizando varios métodos de interpolación, siendo útil para generar salidas de mayor resolución manteniendo la calidad de imagen.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `relación_escala` | FLOAT | No | 0.1 - 20.0 | El factor de escala a aplicar durante el aumento de escala (valor por defecto: 1.0) |
| `pasos_escala` | INT | No | -1 - 1000 | El número de pasos a usar para el proceso de aumento de escala. Usar -1 para cálculo automático (valor por defecto: -1) |
| `método_aumento_escala` | COMBO | Sí | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" | El método de interpolación utilizado para aumentar la escala de la imagen |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Devuelve un objeto sampler configurado que puede usarse en el pipeline de muestreo |
