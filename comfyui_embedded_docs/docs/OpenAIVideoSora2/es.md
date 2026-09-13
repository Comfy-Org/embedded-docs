# OpenAI Sora - Video

El nodo OpenAIVideoSora2 genera videos con los modelos Sora de OpenAI. Toma un prompt de texto junto con una única imagen de referencia opcional, envía la solicitud a OpenAI, espera a que finalice la generación y devuelve el video resultante. Las duraciones y resoluciones admitidas dependen del modelo seleccionado.

**AVISO DE OBSOLESCENCIA:** OpenAI dejará de ofrecer la API de Sora v2 en septiembre de 2026. Este nodo se eliminará de ComfyUI en ese momento.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo OpenAI Sora que se usará para la generación de video (predeterminado: "sora-2") | COMBO | Sí | "sora-2"<br>"sora-2-pro" |
| `prompt` | Texto guía; puede estar vacío si hay una imagen de entrada presente (predeterminado: cadena vacía) | STRING | Sí | - |
| `tamaño` | La resolución del video generado (predeterminado: "1280x720") | COMBO | Sí | "720x1280"<br>"1280x720"<br>"1024x1792"<br>"1792x1024" |
| `duración` | La duración del video generado en segundos (predeterminado: 8) | COMBO | Sí | 4<br>8<br>12 |
| `imagen` | Imagen de referencia de entrada opcional usada para la generación de video; solo se admite una única imagen | IMAGE | No | - |
| `semilla` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales no son deterministas independientemente de la semilla (predeterminado: 0) | INT | No | 0 a 2147483647 |

**Restricciones y limitaciones:**

- El modelo "sora-2" solo admite los tamaños "720x1280" y "1280x720"; seleccionar "1024x1792" o "1792x1024" con "sora-2" genera un error. Los tamaños más grandes solo están disponibles con "sora-2-pro".
- Cuando se conecta una imagen, debe contener exactamente una imagen; conectar más de una imagen genera un error.
- Los resultados no son deterministas independientemente del valor de la semilla.
- La estimación de precio mostrada depende del `model`, `size` y `duration` seleccionados.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | El video generado por OpenAI Sora | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIVideoSora2/es.md)

---
**Source fingerprint (SHA-256):** `d19eb6b65d7f712278828e4b1f7105068cc5e7cb72813b7549ab24520e7719fc`
