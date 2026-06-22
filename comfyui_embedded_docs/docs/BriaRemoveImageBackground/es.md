# Bria Quitar Fondo de Imagen

Este nodo elimina el fondo de una imagen utilizando el servicio Bria RMBG 2.0. Envía la imagen a una API externa para su procesamiento y devuelve el resultado con el fondo eliminado.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imagen` | La imagen de entrada a la que se le eliminará el fondo. | IMAGE | Sí | - |
| `moderación` | Configuración de moderación. Cuando se establece en `"true"`, aparecen opciones de moderación adicionales. | COMBO | No | `"false"`<br>`"true"` |
| `visual_input_moderation` | Habilita la moderación de contenido visual en la imagen de entrada. Este parámetro solo está disponible cuando `moderación` está establecido en `"true"`. Valor predeterminado: `False`. | BOOLEAN | No | - |
| `visual_output_moderation` | Habilita la moderación de contenido visual en la imagen de salida. Este parámetro solo está disponible cuando `moderación` está establecido en `"true"`. Valor predeterminado: `True`. | BOOLEAN | No | - |
| `semilla` | Un valor de semilla que controla si el nodo debe ejecutarse nuevamente. Los resultados no son deterministas independientemente del valor de la semilla. Valor predeterminado: `0`. | INT | No | 0 a 2147483647 |

**Nota:** Los parámetros `visual_input_moderation` y `visual_output_moderation` dependen del parámetro `moderation`. Solo están activos y son necesarios si `moderation` está establecido en `"true"`.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `imagen` | La imagen procesada con su fondo eliminado. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/es.md)

---
**Source fingerprint (SHA-256):** `2b2dd3ca0d026af1a2bf3f7222165928527b05b65817073b50230ff18d39bc6c`
