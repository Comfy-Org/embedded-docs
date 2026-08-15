# Luma Ray 3.2 Fotograma Clave

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `image` | Imagen guía para colocar en el momento elegido del video de salida. | IMAGE | Sí | - |
| `position` | Cómo colocar esta imagen en la línea de tiempo del video de salida. | COMBO | Sí | "Fraction of duration (0.0-1.0)"<br>"Absolute time (seconds)" |
| `keyframes` | Fotogramas clave anteriores opcionales para encadenar con este. | LUMA_RAY32_KEYFRAME | No | - |

Cuando se selecciona "Fraction of duration (0.0-1.0)" para el parámetro `position`, puedes especificar un valor `fraction` (predeterminado: 0.0, rango: 0.0 a 1.0, paso: 0.01) que determina dónde se aplica esta imagen en el video de salida (0.0 = inicio, 1.0 = fin).

Cuando se selecciona "Absolute time (seconds)" para el parámetro `position`, puedes especificar un valor `seconds` (predeterminado: 0.0, rango: 0.0 a 10.0, paso: 0.1) que determina el tiempo en segundos desde el inicio del video de salida donde se aplica esta imagen.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `keyframes` | Una cadena de fotogramas clave que incluye el nuevo fotograma clave combinado con cualquier fotograma clave anterior opcional. | LUMA_RAY32_KEYFRAME |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframeNode/es.md)

---
**Source fingerprint (SHA-256):** `b49d879888e6e83d6937068e799ea583ed5c90284e829ac496821eea330fe9c7`
