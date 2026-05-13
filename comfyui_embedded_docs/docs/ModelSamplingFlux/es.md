> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/es.md)

El nodo ModelSamplingFlux aplica el muestreo del modelo Flux a un modelo determinado calculando un parámetro de desplazamiento basado en las dimensiones de la imagen. Crea una configuración de muestreo especializada que ajusta el comportamiento del modelo según los parámetros de ancho, alto y desplazamiento especificados, y luego devuelve el modelo modificado con la nueva configuración de muestreo aplicada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo al que se aplicará el muestreo Flux |
| `max_shift` | FLOAT | Sí | 0.0 - 100.0 | Valor máximo de desplazamiento para el cálculo del muestreo (predeterminado: 1.15) |
| `base_shift` | FLOAT | Sí | 0.0 - 100.0 | Valor base de desplazamiento para el cálculo del muestreo (predeterminado: 0.5) |
| `width` | INT | Sí | 16 - MAX_RESOLUTION | Ancho de la imagen de destino en píxeles (predeterminado: 1024) |
| `height` | INT | Sí | 16 - MAX_RESOLUTION | Alto de la imagen de destino en píxeles (predeterminado: 1024) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `model` | MODEL | El modelo modificado con la configuración de muestreo Flux aplicada |

---
**Source fingerprint (SHA-256):** `35733ab0cd032884ceada13715cf51e626586844e8e575471a5ba7cf8a1e5e49`
