# Generación de video multifotograma Vidu

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduMultiFrameVideoNode/en.md)

Este nodo genera un video creando transiciones entre múltiples fotogramas clave. Comienza desde una imagen inicial y anima a través de una secuencia de imágenes finales y avisos definidos por el usuario, produciendo un único archivo de video como salida.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo Vidu a utilizar para la generación de video. | COMBO | Sí | `"viduq2-pro"`<br>`"viduq2-turbo"` |
| `imagen_inicial` | La imagen del fotograma inicial. La relación de aspecto debe estar entre 1:4 y 4:1. | IMAGE | Sí | - |
| `semilla` | Un valor de semilla para la generación de números aleatorios, para garantizar resultados reproducibles (predeterminado: 1). | INT | No | 0 a 2147483647 |
| `resolución` | La resolución del video de salida. | COMBO | Sí | `"720p"`<br>`"1080p"` |
| `fotogramas` | Número de transiciones de fotogramas clave (2-9). Seleccionar un valor revela dinámicamente las entradas requeridas para cada fotograma. | DYNAMICCOMBO | Sí | `"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"` |

**Entradas de Fotogramas (Reveladas Dinámicamente):**
Cuando seleccionas un valor para `frames` (por ejemplo, "3"), el nodo mostrará un conjunto correspondiente de entradas requeridas para cada transición. Para cada fotograma `i` desde 1 hasta el número seleccionado, debes proporcionar:

* `end_image{i}` (IMAGE): La imagen objetivo para esta transición. La relación de aspecto debe estar entre 1:4 y 4:1.
* `prompt{i}` (STRING): Una descripción textual que guía la transición hacia este fotograma (máximo 2000 caracteres).
* `duration{i}` (INT): La duración en segundos para este segmento de transición específico.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El archivo de video generado que contiene todas las transiciones animadas. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduMultiFrameVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `02ddbb1e041b6d9e6654ab6c3cc25f4c2e5bc1545d84a30624608edc85e51f96`
