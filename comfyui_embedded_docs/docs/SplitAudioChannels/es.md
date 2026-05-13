> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitAudioChannels/es.md)

El nodo SplitAudioChannels separa el audio estéreo en canales individuales izquierdo y derecho. Toma una entrada de audio estéreo con dos canales y genera dos flujos de audio separados, uno para el canal izquierdo y otro para el canal derecho.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `audio` | AUDIO | Sí | - | La entrada de audio estéreo que se separará en canales |

**Nota:** La entrada de audio debe tener exactamente dos canales (estéreo). El nodo generará un error si la entrada de audio tiene solo un canal.

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `left` | AUDIO | El audio del canal izquierdo separado |
| `right` | AUDIO | El audio del canal derecho separado |

---
**Source fingerprint (SHA-256):** `48f329f3eb9749e75eda1038c43caf42ee63d8a1fa66ab29ad3d34b5d136e323`
