> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceMask/es.md)

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceMask/en.md)

## Resumen

Este nodo crea una máscara binaria (una imagen en blanco y negro) basada en los puntos de referencia faciales detectados por MediaPipe. Dibuja formas de polígonos rellenos para cada región facial detectada, generando una máscara por fotograma en un lote. Cuando se detectan múltiples rostros en el mismo fotograma, sus máscaras se combinan en una sola máscara.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `face_landmarks` | FACE_LANDMARKS | Sí | - | Los datos de puntos de referencia faciales provenientes de un nodo de detección facial de MediaPipe. |
| `regions` | COMBO | Sí | `"all"`<br>`"custom"` | Selecciona qué regiones faciales incluir en la máscara. `"all"` crea una máscara a partir de la unión de todas las regiones faciales (óvalo facial, labios, ojos, iris). `"custom"` permite activar o desactivar cada región individualmente. Valor predeterminado: `"all"` |

Cuando `regions` se establece en `"custom"`, los siguientes parámetros booleanos adicionales están disponibles:

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `face_oval` | BOOLEAN | No | Verdadero/Falso | Incluir la región del óvalo facial en la máscara. Valor predeterminado: Verdadero |
| `lips` | BOOLEAN | No | Verdadero/Falso | Incluir la región de los labios en la máscara. Valor predeterminado: Verdadero |
| `eyes` | BOOLEAN | No | Verdadero/Falso | Incluir la región de los ojos en la máscara. Valor predeterminado: Verdadero |
| `irises` | BOOLEAN | No | Verdadero/Falso | Incluir la región de los iris en la máscara. Valor predeterminado: Verdadero |

**Nota:** Al usar el modo `"all"`, la máscara incluye todas las regiones combinadas. Dado que el óvalo facial envuelve las demás regiones, seleccionar `"all"` produce efectivamente el mismo resultado que seleccionar solo el óvalo facial.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `MASK` | MASK | Un tensor de máscara binaria donde las regiones faciales son blancas (valor 1.0) y el fondo es negro (valor 0.0). La máscara tiene las mismas dimensiones que la imagen de entrada y contiene una máscara por fotograma en el lote. |

---
**Source fingerprint (SHA-256):** `92270002a42ed59bc75e676a6881e1899186d3c8a1bb4dd4c0d39b3762b5bb66`
