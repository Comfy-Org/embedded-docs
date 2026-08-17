# MuestreoDeModeloFlux

El nodo ModelSamplingFlux aplica el muestreo del modelo Flux a un modelo dado calculando un parámetro de desplazamiento basado en las dimensiones de la imagen. Crea una configuración de muestreo especializada que ajusta el comportamiento del modelo según los parámetros de ancho, alto y desplazamiento especificados, y luego devuelve el modelo modificado con los nuevos ajustes de muestreo aplicados.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo al que aplicar el muestreo Flux | MODEL | Sí | - |
| `max_shift` | Valor máximo de desplazamiento para el cálculo de muestreo (por defecto: 1.15) | FLOAT | Sí | 0.0 - 100.0 |
| `base_shift` | Valor base de desplazamiento para el cálculo de muestreo (por defecto: 0.5) | FLOAT | Sí | 0.0 - 100.0 |
| `width` | Ancho de la imagen objetivo en píxeles (por defecto: 1024) | INT | Sí | 16 - MAX_RESOLUTION |
| `height` | Altura de la imagen objetivo en píxeles (por defecto: 1024) | INT | Sí | 16 - MAX_RESOLUTION |

El valor de desplazamiento efectivo se interpola entre `base_shift` y `max_shift` según el tamaño latente derivado de `width` y `height`. El valor `step` es 0.01 para `max_shift` y `base_shift`, y 8 para `width` y `height`. Los parámetros `max_shift` y `base_shift` están marcados como opciones avanzadas en la interfaz de usuario.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo modificado con la configuración de muestreo Flux aplicada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/es.md)

---
**Source fingerprint (SHA-256):** `04065b54ace30a2b20476ed085df871ea89794650e98ae30c40f750357663834`
