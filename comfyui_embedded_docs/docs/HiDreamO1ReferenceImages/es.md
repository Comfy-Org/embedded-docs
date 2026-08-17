# Imágenes de Referencia HiDream-O1

## Resumen

Adjunta imágenes de referencia tanto al condicionamiento positivo como al negativo. Este nodo le permite proporcionar una o más imágenes de referencia que se utilizarán para guiar el proceso de generación de imágenes, ya sea para edición basada en una instrucción o para personalización basada en un sujeto.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positive` | El condicionamiento positivo al que se adjuntan las imágenes de referencia. | CONDITIONING | Sí | - |
| `negative` | El condicionamiento negativo al que se adjuntan las imágenes de referencia. | CONDITIONING | Sí | - |
| `images` | Imágenes de referencia. 1 imagen = edición por instrucción; 2-10 imágenes = referencia múltiple. | IMAGE | Sí | 1 a 10 imágenes |

**Nota sobre el parámetro `images`:** Esta es una entrada de crecimiento automático que acepta entre 1 y 10 imágenes. Las imágenes se etiquetan como `image_1` hasta `image_10`. Debe proporcionar al menos 1 imagen. El número de imágenes determina el modo de funcionamiento: una sola imagen se usa para instrucciones de edición, mientras que varias imágenes (2-10) se usan para la personalización basada en el sujeto.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | El condicionamiento positivo con las imágenes de referencia adjuntas. | CONDITIONING |
| `negative` | El condicionamiento negativo con las imágenes de referencia adjuntas. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/es.md)

---
**Source fingerprint (SHA-256):** `f05f6be19df8b8697a98507163e8f60fd0cf2048c81f92597d2ae0a3395b8c6d`
