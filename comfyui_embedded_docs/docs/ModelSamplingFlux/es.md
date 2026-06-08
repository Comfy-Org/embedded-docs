El nodo ModelSamplingFlux aplica el muestreo del modelo Flux a un modelo determinado calculando un parámetro de desplazamiento basado en las dimensiones de la imagen. Crea una configuración de muestreo especializada que ajusta el comportamiento del modelo según los parámetros de ancho, alto y desplazamiento especificados, y luego devuelve el modelo modificado con la nueva configuración de muestreo aplicada.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo al que se aplicará el muestreo Flux | MODEL | Sí | - |
| `desplazamiento_max` | Valor máximo de desplazamiento para el cálculo del muestreo (predeterminado: 1.15) | FLOAT | Sí | 0.0 - 100.0 |
| `desplazamiento_base` | Valor base de desplazamiento para el cálculo del muestreo (predeterminado: 0.5) | FLOAT | Sí | 0.0 - 100.0 |
| `ancho` | Ancho de la imagen de destino en píxeles (predeterminado: 1024) | INT | Sí | 16 - MAX_RESOLUTION |
| `altura` | Alto de la imagen de destino en píxeles (predeterminado: 1024) | INT | Sí | 16 - MAX_RESOLUTION |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `modelo` | El modelo modificado con la configuración de muestreo Flux aplicada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/es.md)

---
**Source fingerprint (SHA-256):** `35733ab0cd032884ceada13715cf51e626586844e8e575471a5ba7cf8a1e5e49`
