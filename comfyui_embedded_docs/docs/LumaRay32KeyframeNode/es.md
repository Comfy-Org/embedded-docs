# Luma Ray 3.2 Fotograma Clave

Este nodo ancla una imagen guía a una posición específica en la línea de tiempo del video de salida de Luma Ray 3.2. Conecta este nodo a la entrada `"keyframes"` del nodo Luma Ray 3.2 Keyframes to Video, y encadena varios keyframes conectando la entrada opcional `"keyframes"`.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `image` | Imagen guía para colocar en el momento elegido del video de salida. | IMAGE | Sí | - |
| `position` | Cómo colocar esta imagen en la línea de tiempo del video de salida. | DYNAMIC_COMBO | Sí | "Fraction of duration (0.0-1.0)"<br>"Absolute time (seconds)" |
| `keyframes` | Keyframes anteriores opcionales para encadenar con este. | LUMA_RAY32_KEYFRAME | No | - |

El parámetro `position` determina qué valor se utiliza para colocar la imagen en la línea de tiempo.

Cuando se selecciona "Fraction of duration (0.0-1.0)" para el parámetro `position`, puedes especificar un valor `fraction` (predeterminado: 0.0, rango: 0.0 a 1.0, paso: 0.01) que determina en qué parte del video de salida se aplica esta imagen (0.0 = inicio, 1.0 = final).

Cuando se selecciona "Absolute time (seconds)" para el parámetro `position`, puedes especificar un valor `seconds` (predeterminado: 0.0, rango: 0.0 a 10.0, paso: 0.1) que determina el tiempo en segundos desde el inicio del video de salida donde se aplica esta imagen.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `keyframes` | Una cadena de keyframes que incluye el nuevo keyframe combinado con cualquier keyframe anterior opcional. | LUMA_RAY32_KEYFRAME |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframeNode/es.md)

---
**Source fingerprint (SHA-256):** `b49d879888e6e83d6937068e799ea583ed5c90284e829ac496821eea330fe9c7`
