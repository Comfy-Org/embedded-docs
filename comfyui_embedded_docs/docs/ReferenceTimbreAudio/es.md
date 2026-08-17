# ReferenceTimbreAudio

Este nodo establece un timbre de audio de referencia para usar en el proceso "ace step 1.5". Toma una entrada de condicionamiento y una representación latente opcional del audio, y luego adjunta esos datos latentes al condicionamiento para que los nodos posteriores del flujo de trabajo puedan usarlos como audio de referencia. Si no se proporciona un latente, el condicionamiento se devuelve sin cambios.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `conditioning` | Los datos de condicionamiento a los que se adjuntará la información del audio de referencia. | CONDITIONING | Sí |  |
| `latent` | Una representación latente opcional del audio de referencia. Cuando se proporciona, sus muestras se agregan al condicionamiento. | LATENT | No |  |

Cuando se proporciona `latent`, sus muestras se agregan a los latentes de timbre de audio de referencia del condicionamiento. Si no se proporciona `latent`, el condicionamiento original se pasa sin cambios.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `conditioning` | Los datos de condicionamiento modificados, que ahora contienen los latentes de timbre de audio de referencia si se proporcionó la entrada opcional `latent`. Si no se proporciona un latente, el condicionamiento original se devuelve sin cambios. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/es.md)

---
**Source fingerprint (SHA-256):** `2ddccb7676fc45a5324ba32dde0cd2f8f24388ceec20c88a475e1aa9d4276be0`
