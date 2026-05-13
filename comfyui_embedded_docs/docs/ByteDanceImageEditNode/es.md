> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageEditNode/es.md)

El nodo ByteDance Image Edit permite modificar imágenes utilizando los modelos de IA de ByteDance a través de una API. Debes proporcionar una imagen de entrada y un mensaje de texto que describa los cambios deseados, y el nodo procesará la imagen según tus instrucciones. El nodo maneja automáticamente la comunicación con la API y devuelve la imagen editada.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Valor por Defecto | Rango | Descripción |
|-----------|--------------|-----------------|-------------------|-------|-------------|
| `model` | MODEL | COMBO | seededit_3 | Opciones de Image2ImageModelName | Nombre del modelo |
| `image` | IMAGE | IMAGE | - | - | La imagen base a editar |
| `prompt` | STRING | STRING | "" | - | Instrucción para editar la imagen |
| `seed` | INT | INT | 0 | 0-2147483647 | Semilla a utilizar para la generación |
| `guidance_scale` | FLOAT | FLOAT | 5.5 | 1.0-10.0 | Un valor más alto hace que la imagen siga el mensaje con mayor precisión |
| `watermark` | BOOLEAN | BOOLEAN | True | - | Indica si se debe añadir una marca de agua "Generado por IA" a la imagen |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `IMAGE` | IMAGE | La imagen editada devuelta por la API de ByteDance |

---
**Source fingerprint (SHA-256):** `9dc13d89f84756b545120efb5535e08ada163d4534975809f5056bdf7d8bfb73`
