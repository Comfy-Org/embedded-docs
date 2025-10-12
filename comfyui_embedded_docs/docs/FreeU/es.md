> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/es.md)

El nodo FreeU aplica modificaciones en el dominio de frecuencia a los bloques de salida de un modelo para mejorar la calidad de la generación de imágenes. Funciona escalando diferentes grupos de canales y aplicando filtrado de Fourier a mapas de características específicos, permitiendo un control afinado sobre el comportamiento del modelo durante el proceso de generación.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo al que aplicar las modificaciones FreeU |
| `b1` | FLOAT | Sí | 0.0 - 10.0 | Factor de escalado backbone para características model_channels × 4 (valor por defecto: 1.1) |
| `b2` | FLOAT | Sí | 0.0 - 10.0 | Factor de escalado backbone para características model_channels × 2 (valor por defecto: 1.2) |
| `s1` | FLOAT | Sí | 0.0 - 10.0 | Factor de escalado de conexión de salto para características model_channels × 4 (valor por defecto: 0.9) |
| `s2` | FLOAT | Sí | 0.0 - 10.0 | Factor de escalado de conexión de salto para características model_channels × 2 (valor por defecto: 0.2) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `modelo` | MODEL | El modelo modificado con los parches FreeU aplicados |
