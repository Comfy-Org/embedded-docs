> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/es.md)

# Descripción General

Adjunta imágenes de referencia tanto al condicionamiento positivo como al negativo. Este nodo permite proporcionar una o más imágenes de referencia que se utilizarán para guiar el proceso de generación de imágenes, ya sea para edición basada en una instrucción o para personalización dirigida por un sujeto.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `positivo` | CONDITIONING | Sí | - | El condicionamiento positivo al que adjuntar las imágenes de referencia. |
| `negativo` | CONDITIONING | Sí | - | El condicionamiento negativo al que adjuntar las imágenes de referencia. |
| `imágenes` | IMAGE | Sí | 1 a 10 imágenes | Imágenes de referencia. 1 imagen habilita la edición basada en instrucciones; 2-10 imágenes habilitan la personalización dirigida por un sujeto con múltiples referencias. |

**Nota sobre el parámetro `images`:** Esta es una entrada de crecimiento automático que acepta entre 1 y 10 imágenes. Las imágenes se etiquetan como `image_1` hasta `image_10`. Debes proporcionar al menos 1 imagen. La cantidad de imágenes determina el modo de operación: una sola imagen se utiliza para instrucciones de edición, mientras que múltiples imágenes (2-10) se utilizan para personalización dirigida por un sujeto.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `negativo` | CONDITIONING | El condicionamiento positivo con las imágenes de referencia adjuntas. |
| `negativo` | CONDITIONING | El condicionamiento negativo con las imágenes de referencia adjuntas. |

---
**Source fingerprint (SHA-256):** `b14a8fc2acd44618370bd7e94758d469ff37530f2e19498a6c72ee3748559303`
