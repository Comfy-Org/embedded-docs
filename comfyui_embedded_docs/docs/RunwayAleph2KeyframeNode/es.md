# Nodo Runway Aleph2 Keyframe

Este nodo ancla una imagen de guía a un momento específico de tu video de entrada, para que el modelo Aleph2 dirija la edición en ese punto de tu metraje. Conecta este nodo a la entrada "keyframes" del nodo Runway Aleph2 Video to Video, y encadena varios (hasta 5) mediante la entrada opcional "keyframes".

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `image` | La imagen de guía para aplicar en el momento elegido del video de entrada. | IMAGE | Sí | - |
| `timing` | Cómo ubicar esta imagen en la línea de tiempo del video de entrada. | COMBO | Sí | Ver abajo |
| `keyframes` | Fotogramas clave anteriores opcionales para encadenar con este. | KEYFRAME | No | - |

### Opciones del Parámetro Timing

El parámetro `timing` tiene dos modos:

| Modo | Subparámetro | Descripción | Rango |
|------|--------------|-------------|-------|
| "Segundos absolutos" | `seconds` | Tiempo en segundos desde el inicio del video de entrada donde se aplica esta imagen (predeterminado: 0.0) | 0.0 a 30.0, paso 0.1 |
| "Fracción de duración" | `fraction` | Dónde en el video de entrada se aplica esta imagen, como fracción de su duración (0.0 = inicio, 1.0 = final) (predeterminado: 0.0) | 0.0 a 1.0, paso 0.01 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `keyframes` | Una cadena de fotogramas clave que incluye este y cualquier fotograma clave previamente conectado. | KEYFRAME |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2KeyframeNode/es.md)

---
**Source fingerprint (SHA-256):** `b5ac6553166b7366fd35f97740861be163f91bc2353f5f83bdc2f04bf40f8478`
