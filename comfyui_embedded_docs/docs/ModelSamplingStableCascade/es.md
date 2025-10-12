> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/es.md)

El nodo ModelSamplingStableCascade aplica muestreo de cascada estable a un modelo ajustando los parámetros de muestreo con un valor de desplazamiento. Crea una versión modificada del modelo de entrada con configuración de muestreo personalizada para la generación de cascada estable.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo de entrada al que aplicar el muestreo de cascada estable |
| `desplazamiento` | FLOAT | Sí | 0.0 - 100.0 | El valor de desplazamiento a aplicar a los parámetros de muestreo (por defecto: 2.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `modelo` | MODEL | El modelo modificado con muestreo de cascada estable aplicado |