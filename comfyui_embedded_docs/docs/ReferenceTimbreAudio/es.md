# ReferenceTimbreAudio

Este nodo establece un timbre de audio de referencia para usarlo en el proceso "ace step 1.5". Funciona tomando una entrada de condicionamiento y, opcionalmente, una representación latente de audio, y luego adjunta esos datos latentes al condicionamiento para que los usen nodos posteriores en el flujo de trabajo. Este nodo está actualmente marcado como experimental.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `condicionamiento` | Los datos de condicionamiento a los que se adjuntará la información de audio de referencia. | CONDITIONING | Sí |  |
| `latente` | Una representación latente opcional del audio de referencia. Cuando se proporciona, sus muestras se agregan (se adjuntan) al condicionamiento para que puedan usarse como latentes de timbre de audio de referencia. | LATENT | No |  |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `conditioning` | Los datos de condicionamiento modificados, que ahora contienen los latentes de timbre de audio de referencia si se proporcionó la entrada opcional `latent`. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/es.md)

---
**Source fingerprint (SHA-256):** `2ddccb7676fc45a5324ba32dde0cd2f8f24388ceec20c88a475e1aa9d4276be0`
