> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/es.md)

Este nodo elimina el fondo de una imagen utilizando el servicio Bria RMBG 2.0. Envía la imagen a una API externa para su procesamiento y devuelve el resultado con el fondo eliminado.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen` | IMAGE | Sí | - | La imagen de entrada a la que se le eliminará el fondo. |
| `moderación` | COMBO | No | `"false"`<br>`"true"` | Configuración de moderación. Cuando se establece en `"true"`, aparecen opciones de moderación adicionales. |
| `visual_input_moderation` | BOOLEAN | No | - | Habilita la moderación de contenido visual en la imagen de entrada. Este parámetro solo está disponible cuando `moderación` está establecido en `"true"`. Valor predeterminado: `False`. |
| `visual_output_moderation` | BOOLEAN | No | - | Habilita la moderación de contenido visual en la imagen de salida. Este parámetro solo está disponible cuando `moderación` está establecido en `"true"`. Valor predeterminado: `True`. |
| `semilla` | INT | No | 0 a 2147483647 | Un valor de semilla que controla si el nodo debe ejecutarse nuevamente. Los resultados no son deterministas independientemente del valor de la semilla. Valor predeterminado: `0`. |

**Nota:** Los parámetros `visual_input_moderation` y `visual_output_moderation` dependen del parámetro `moderation`. Solo están activos y son necesarios si `moderation` está establecido en `"true"`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `imagen` | IMAGE | La imagen procesada con su fondo eliminado. |

---
**Source fingerprint (SHA-256):** `2b2dd3ca0d026af1a2bf3f7222165928527b05b65817073b50230ff18d39bc6c`
