# Wan 2.7 Continuación de Video

El nodo **Continuación de Video Wan 2.7** genera un nuevo segmento de video que continúa sin interrupciones desde el final de un clip de video de entrada. Utiliza el modelo Wan 2.7 para sintetizar la continuación basándose en un prompt de texto y, opcionalmente, puede guiar el final hacia un fotograma objetivo específico.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de generación de video a utilizar. | COMBO | Sí | `"wan2.7-i2v"` |
| `model.prompt` | Prompt que describe los elementos y características visuales. Compatible con inglés y chino. (predeterminado: cadena vacía) | STRING | Sí | - |
| `model.negative_prompt` | Prompt negativo que describe lo que se debe evitar. (predeterminado: cadena vacía) | STRING | Sí | - |
| `model.resolution` | La resolución del video de salida. | COMBO | Sí | `"720P"`<br>`"1080P"` |
| `model.duration` | Duración total de salida en segundos. El modelo genera la continuación para llenar el tiempo restante después del clip de entrada. (predeterminado: 5) | INT | Sí | 2 a 15 |
| `primer_clip` | Video de entrada desde el cual continuar. Duración: 2s-10s. La relación de aspecto de salida se deriva de este video. | VIDEO | Sí | - |
| `último_fotograma` | Imagen del último fotograma. La continuación hará una transición hacia este fotograma. | IMAGE | No | - |
| `semilla` | Semilla a utilizar para la generación. (predeterminado: 0) | INT | Sí | 0 a 2147483647 |
| `extender_prompt` | Si se debe mejorar el prompt con asistencia de IA. (predeterminado: True) | BOOLEAN | Sí | - |
| `marca de agua` | Si se debe agregar una marca de agua generada por IA al resultado. (predeterminado: False) | BOOLEAN | Sí | - |

**Nota:** El video de entrada `first_clip` debe tener una duración de entre 2 y 10 segundos.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | La continuación de video generada. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoContinuationApi/es.md)

---
**Source fingerprint (SHA-256):** `5e9d2c7800603660f5f994d125e1e32f2b310234c4b6a24d502c764d91be49e8`
