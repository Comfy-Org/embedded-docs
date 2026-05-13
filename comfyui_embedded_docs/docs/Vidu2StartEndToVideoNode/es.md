> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2StartEndToVideoNode/es.md)

Este documento fue generado por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2StartEndToVideoNode/en.md)

Este nodo genera un video interpolando entre un fotograma inicial y un fotograma final proporcionados, guiado por un texto descriptivo. Utiliza un modelo Vidu específico para crear una transición suave entre las dos imágenes durante una duración determinada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `modelo` | COMBO | Sí | `"viduq2-pro-fast"`<br>`"viduq2-pro"`<br>`"viduq2-turbo"` | El modelo Vidu a utilizar para la generación del video. |
| `fotograma_inicial` | IMAGE | Sí | - | La imagen inicial para la secuencia de video. Solo se permite una sola imagen. |
| `fotograma_final` | IMAGE | Sí | - | La imagen final para la secuencia de video. Solo se permite una sola imagen. |
| `prompt` | STRING | Sí | - | Una descripción textual que guía la generación del video (máximo 2000 caracteres). |
| `duración` | INT | No | 2 a 8 | La duración del video generado en segundos (valor predeterminado: 5). |
| `semilla` | INT | No | 0 a 2147483647 | Un número utilizado para inicializar la generación aleatoria y obtener resultados reproducibles (valor predeterminado: 1). |
| `resolución` | COMBO | No | `"720p"`<br>`"1080p"` | La resolución de salida del video generado. |
| `amplitud_de_movimiento` | COMBO | No | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` | La amplitud de movimiento de los objetos en el fotograma. |

**Nota:** Las imágenes `first_frame` y `end_frame` deben tener relaciones de aspecto similares. El nodo validará que sus relaciones de aspecto estén dentro de un rango relativo de 0.8 a 1.25.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El archivo de video generado. |

---
**Source fingerprint (SHA-256):** `0a2a125fcb0a519e3aa98ed846f0c7bdc14644a27aaaab3953d55945f787de2a`
