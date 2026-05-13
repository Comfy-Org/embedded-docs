> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleConservativeNode/es.md)

Aquí tienes la traducción al español, siguiendo todas las reglas especificadas:

Amplía la imagen con alteraciones mínimas a resolución 4K. Este nodo utiliza la ampliación conservadora de Stability AI para aumentar la resolución de la imagen preservando el contenido original y realizando solo cambios sutiles.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se va a ampliar |
| `prompt` | STRING | Sí | - | Lo que deseas ver en la imagen de salida. Un mensaje descriptivo y contundente que defina claramente elementos, colores y sujetos generará mejores resultados. (predeterminado: cadena vacía) |
| `creativity` | FLOAT | Sí | 0.2-0.5 | Controla la probabilidad de crear detalles adicionales que no estén fuertemente condicionados por la imagen inicial. (predeterminado: 0.35) |
| `seed` | INT | Sí | 0-4294967294 | La semilla aleatoria utilizada para generar el ruido. (predeterminado: 0) |
| `negative_prompt` | STRING | No | - | Palabras clave de lo que NO deseas ver en la imagen de salida. Esta es una función avanzada. (predeterminado: cadena vacía) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen ampliada a resolución 4K |

---
**Source fingerprint (SHA-256):** `0a6eed22a37c1019ee97035bba70660b9619b0d65e443111d1d330968ded009a`
