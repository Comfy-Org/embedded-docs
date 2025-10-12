> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU_V2/es.md)

El nodo FreeU_V2 aplica una mejora basada en frecuencia a los modelos de difusión mediante la modificación de la arquitectura U-Net. Escala diferentes canales de características utilizando parámetros configurables para mejorar la calidad de la generación de imágenes sin requerir entrenamiento adicional. El nodo funciona aplicando parches a los bloques de salida del modelo para aplicar factores de escala a dimensiones de canal específicas.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo de difusión al que aplicar la mejora FreeU |
| `b1` | FLOAT | Sí | 0.0 - 10.0 | Factor de escala de características backbone para el primer bloque (por defecto: 1.3) |
| `b2` | FLOAT | Sí | 0.0 - 10.0 | Factor de escala de características backbone para el segundo bloque (por defecto: 1.4) |
| `s1` | FLOAT | Sí | 0.0 - 10.0 | Factor de escala de características skip para el primer bloque (por defecto: 0.9) |
| `s2` | FLOAT | Sí | 0.0 - 10.0 | Factor de escala de características skip para el segundo bloque (por defecto: 0.2) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `modelo` | MODEL | El modelo de difusión mejorado con las modificaciones FreeU aplicadas |
