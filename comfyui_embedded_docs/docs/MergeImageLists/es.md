> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeImageLists/es.md)

El nodo Merge Image Lists combina múltiples listas separadas de imágenes en una sola lista continua. Funciona tomando todas las imágenes de cada entrada conectada y concatenándolas en el orden en que se reciben. Esto es útil para organizar o agrupar imágenes de diferentes fuentes para su posterior procesamiento.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sí | - | Una lista de imágenes que se fusionarán. Esta entrada puede aceptar múltiples conexiones, y cada lista conectada se concatenará en la salida final. |

**Nota:** Este nodo está diseñado para recibir múltiples entradas. Puedes conectar varias listas de imágenes al único conector de entrada `images`. El nodo concatenará automáticamente todas las imágenes de todas las listas conectadas en una sola lista de salida.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `images` | IMAGE | La lista única y fusionada que contiene todas las imágenes de cada lista de entrada conectada. |
