# Imágenes de Referencia HiDream-O1

## Resumen

Adjunta imágenes de referencia tanto al condicionamiento positivo como al negativo. Este nodo permite proporcionar de 1 a 10 imágenes de referencia; una sola imagen se utiliza para edición basada en instrucciones, mientras que varias imágenes (2-10) habilitan la personalización dirigida por el sujeto.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | El condicionamiento positivo al que se adjuntarán las imágenes de referencia. | CONDITIONING | Sí | - |
| `negativo` | El condicionamiento negativo al que se adjuntarán las imágenes de referencia. | CONDITIONING | Sí | - |
| `imágenes` | Imágenes de referencia. 1 imagen = edición por instrucciones; 2-10 imágenes = referencia múltiple. | IMAGE | Sí | 1 a 10 imágenes |

**Nota sobre el parámetro `images`:** Esta es una entrada de crecimiento automático (autogrow) que acepta entre 1 y 10 imágenes. Las imágenes se etiquetan como `image_1` hasta `image_10`. Debe proporcionar al menos 1 imagen. El número de imágenes determina el modo de funcionamiento: una sola imagen se usa para instrucciones de edición, mientras que varias imágenes (2-10) se usan para la personalización dirigida por el sujeto.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positivo` | El condicionamiento positivo con las imágenes de referencia adjuntas. | CONDITIONING |
| `negativo` | El condicionamiento negativo con las imágenes de referencia adjuntas. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/es.md)

---
**Source fingerprint (SHA-256):** `f05f6be19df8b8697a98507163e8f60fd0cf2048c81f92597d2ae0a3395b8c6d`
