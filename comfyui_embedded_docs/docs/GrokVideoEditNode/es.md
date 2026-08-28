# Edición de video Grok

Este nodo utiliza la API de Grok para editar un video existente basado en un prompt de texto. Carga tu video, envía una solicitud al modelo de IA para modificarlo según tu descripción y devuelve el video recién generado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `modelo` | El modelo de IA a utilizar para la edición de video (predeterminado: "grok-imagine-video"). | COMBO | Sí | "grok-imagine-video" |
| `indicación` | Descripción de texto del video deseado. | STRING | Sí | N/A |
| `video` | El video de entrada que se va a editar. La duración máxima admitida es de 8.7 segundos y un tamaño de archivo de 50 MB. | VIDEO | Sí | N/A |
| `semilla` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (predeterminado: 0). | INT | No | 0 a 2147483647 |

**Restricciones:**

* El `prompt` no debe estar vacío.
* El `video` de entrada debe tener una duración entre 1 y 8.7 segundos.
* El tamaño del archivo del `video` de entrada no debe exceder los 50 MB.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El video editado generado por el modelo de IA. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoEditNode/es.md)

---
**Source fingerprint (SHA-256):** `7ceedff2f858bc0849b5e0d92d10ed51e7fdccd1391c6a6966561cb05999b4b1`
