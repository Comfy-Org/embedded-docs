Este nodo establece un timbre de audio de referencia para su uso en el proceso "ace step 1.5". Funciona tomando una entrada de condicionamiento y, opcionalmente, una representación latente de audio, y luego adjunta esos datos latentes al condicionamiento para que los utilicen nodos posteriores en el flujo de trabajo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `condicionamiento` | Los datos de condicionamiento a los que se adjuntará la información del audio de referencia. | CONDITIONING | Sí |  |
| `latente` | Una representación latente opcional del audio de referencia. Cuando se proporciona, sus muestras se añaden al condicionamiento. | LATENT | No |  |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `condicionamiento` | Los datos de condicionamiento modificados, que ahora contienen los latentes del timbre de audio de referencia si se proporcionó la entrada opcional `latente`. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/es.md)

---
**Source fingerprint (SHA-256):** `2d39399eb79cfe76b72d01326b89863e2553bc23414b1166d310e5222b215b29`
