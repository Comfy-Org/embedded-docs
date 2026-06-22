# Stability AI Upscale Conservador

Aquí tienes la traducción al español, siguiendo todas las reglas especificadas:

Amplía la imagen con alteraciones mínimas a resolución 4K. Este nodo utiliza la ampliación conservadora de Stability AI para aumentar la resolución de la imagen preservando el contenido original y realizando solo cambios sutiles.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imagen` | La imagen de entrada que se va a ampliar | IMAGE | Sí | - |
| `prompt` | Lo que deseas ver en la imagen de salida. Un mensaje descriptivo y contundente que defina claramente elementos, colores y sujetos generará mejores resultados. (predeterminado: cadena vacía) | STRING | Sí | - |
| `creatividad` | Controla la probabilidad de crear detalles adicionales que no estén fuertemente condicionados por la imagen inicial. (predeterminado: 0.35) | FLOAT | Sí | 0.2-0.5 |
| `semilla` | La semilla aleatoria utilizada para generar el ruido. (predeterminado: 0) | INT | Sí | 0-4294967294 |
| `prompt negativo` | Palabras clave de lo que NO deseas ver en la imagen de salida. Esta es una función avanzada. (predeterminado: cadena vacía) | STRING | No | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `imagen` | La imagen ampliada a resolución 4K | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleConservativeNode/es.md)

---
**Source fingerprint (SHA-256):** `0a6eed22a37c1019ee97035bba70660b9619b0d65e443111d1d330968ded009a`
