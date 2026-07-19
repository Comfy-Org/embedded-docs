# LumaRay32KeyframeNode

Este nodo fija una imagen guía en una posición específica dentro de la línea de tiempo del video de salida de Luma Ray 3.2. Conecta este nodo a la entrada "keyframes" del nodo Luma Ray 3.2 Keyframes to Video, y encadena varios fotogramas clave conectando la entrada opcional "keyframes".

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `image` | Imagen guía para colocar en el momento elegido del video de salida. | IMAGE | Sí | - |
| `position` | Cómo ubicar esta imagen en la línea de tiempo del video de salida. | COMBO | Sí | "Fracción de duración (0.0-1.0)"<br>"Tiempo absoluto (segundos)" |
| `keyframes` | Fotogramas clave anteriores opcionales para encadenar con este. | LUMA_RAY32_KEYFRAME | No | - |

Cuando se selecciona "Fracción de duración (0.0-1.0)" para el parámetro `position`, puedes especificar un valor `fraction` (valor predeterminado: 0.0, rango: 0.0 a 1.0, incremento: 0.01) que determina en qué parte del video de salida se aplica esta imagen (0.0 = inicio, 1.0 = final).

Cuando se selecciona "Tiempo absoluto (segundos)" para el parámetro `position`, puedes especificar un valor `seconds` (valor predeterminado: 0.0, rango: 0.0 a 10.0, incremento: 0.1) que determina el tiempo en segundos desde el inicio del video de salida donde se aplica esta imagen.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `keyframes` | Una cadena de fotogramas clave que incluye el nuevo fotograma clave combinado con cualquier fotograma clave anterior opcional. | LUMA_RAY32_KEYFRAME |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframeNode/es.md)

---
**Source fingerprint (SHA-256):** `b49d879888e6e83d6937068e799ea583ed5c90284e829ac496821eea330fe9c7`
