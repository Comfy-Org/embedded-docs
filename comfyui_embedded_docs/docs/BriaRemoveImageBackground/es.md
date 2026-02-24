> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/es.md)

Este nodo elimina el fondo de una imagen utilizando el servicio Bria RMBG 2.0. Envía la imagen a una API externa para su procesamiento y devuelve el resultado con el fondo eliminado.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada a la que se le eliminará el fondo. |
| `moderation` | COMBO | No | `"false"`<br>`"true"` | Configuración de moderación. Cuando se establece en `"true"`, se habilitan opciones de moderación adicionales. |
| `visual_input_moderation` | BOOLEAN | No | - | Habilita la moderación de contenido visual en la imagen de entrada. Este parámetro solo está disponible cuando `moderation` está establecido en `"true"`. Valor por defecto: `False`. |
| `visual_output_moderation` | BOOLEAN | No | - | Habilita la moderación de contenido visual en la imagen de salida. Este parámetro solo está disponible cuando `moderation` está establecido en `"true"`. Valor por defecto: `True`. |
| `seed` | INT | No | 0 a 2147483647 | Un valor de semilla que controla si el nodo debe volver a ejecutarse. Los resultados no son deterministas, independientemente del valor de la semilla. Valor por defecto: `0`. |

**Nota:** Los parámetros `visual_input_moderation` y `visual_output_moderation` dependen del parámetro `moderation`. Solo están activos y son obligatorios si `moderation` está establecido en `"true"`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen procesada con su fondo eliminado. |
