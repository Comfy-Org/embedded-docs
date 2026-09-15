# ByteDanceImageEditNode

El nodo ByteDance Image Edit te permite modificar imágenes usando los modelos de IA de ByteDance a través de una API. Proporcionas una imagen de entrada y un prompt de texto que describe los cambios deseados, y el nodo procesa la imagen según tus instrucciones. El nodo gestiona la comunicación con la API automáticamente y devuelve la imagen editada.

## Entradas

| Parámetro | Descripción | Tipo de datos | Tipo de entrada | Predeterminado | Rango |
| --- | --- | --- | --- | --- | --- |
| `model` | Nombre del modelo | MODEL | COMBO | seededit_3 | Opciones de Image2ImageModelName |
| `image` | La imagen base que se va a editar | IMAGE | IMAGE | - | - |
| `prompt` | Instrucción para editar la imagen | STRING | STRING | "" | - |
| `seed` | Semilla que se usará para la generación | INT | INT | 0 | 0-2147483647 |
| `guidance_scale` | Un valor más alto hace que la imagen siga el prompt con mayor fidelidad | FLOAT | FLOAT | 5.5 | 1.0-10.0 |
| `watermark` | Indica si se debe agregar una marca de agua de "AI generated" a la imagen | BOOLEAN | BOOLEAN | True | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `IMAGE` | La imagen editada devuelta por la API de ByteDance | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageEditNode/es.md)

---
**Source fingerprint (SHA-256):** `9dc13d89f84756b545120efb5535e08ada163d4534975809f5056bdf7d8bfb73`
