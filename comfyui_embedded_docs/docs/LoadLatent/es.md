> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/es.md)

El nodo LoadLatent carga representaciones latentes previamente guardadas desde archivos .latent en el directorio de entrada. Lee los datos del tensor latente del archivo y aplica cualquier ajuste de escalado necesario antes de devolver los datos latentes para su uso en otros nodos.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `latente` | STRING | Sí | Todos los archivos .latent en el directorio de entrada | Selecciona qué archivo .latent cargar de los archivos disponibles en el directorio de entrada |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Devuelve los datos de representación latente cargados desde el archivo seleccionado |