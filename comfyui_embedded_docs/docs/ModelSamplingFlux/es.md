> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/es.md)

El nodo ModelSamplingFlux aplica muestreo de modelo Flux a un modelo dado calculando un parámetro de desplazamiento basado en las dimensiones de la imagen. Crea una configuración de muestreo especializada que ajusta el comportamiento del modelo según los parámetros de ancho, alto y desplazamiento especificados, luego devuelve el modelo modificado con los nuevos ajustes de muestreo aplicados.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo al que aplicar el muestreo Flux |
| `desplazamiento_max` | FLOAT | Sí | 0.0 - 100.0 | Valor de desplazamiento máximo para el cálculo de muestreo (predeterminado: 1.15) |
| `desplazamiento_base` | FLOAT | Sí | 0.0 - 100.0 | Valor de desplazamiento base para el cálculo de muestreo (predeterminado: 0.5) |
| `ancho` | INT | Sí | 16 - MAX_RESOLUTION | Ancho de la imagen objetivo en píxeles (predeterminado: 1024) |
| `altura` | INT | Sí | 16 - MAX_RESOLUTION | Alto de la imagen objetivo en píxeles (predeterminado: 1024) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `modelo` | MODEL | El modelo modificado con la configuración de muestreo Flux aplicada |
