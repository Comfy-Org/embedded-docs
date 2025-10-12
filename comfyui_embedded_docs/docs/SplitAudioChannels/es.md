> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitAudioChannels/es.md)

El nodo SplitAudioChannels separa audio estéreo en canales izquierdo y derecho individuales. Toma una entrada de audio estéreo con dos canales y produce dos flujos de audio separados, uno para el canal izquierdo y otro para el canal derecho.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Sí | - | La entrada de audio estéreo que se separará en canales |

**Nota:** El audio de entrada debe tener exactamente dos canales (estéreo). El nodo generará un error si el audio de entrada tiene solo un canal.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `left` | AUDIO | El audio del canal izquierdo separado |
| `right` | AUDIO | El audio del canal derecho separado |
