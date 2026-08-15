# Bria Quitar Fondo de Imagen

Este nodo elimina el fondo de una imagen utilizando el servicio Bria RMBG 2.0. Envía la imagen a una API externa para su procesamiento y devuelve el resultado con el fondo eliminado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `image` | La imagen de entrada a la que se le eliminará el fondo. | IMAGE | Sí | - |
| `moderation` | Configuración de moderación. Cuando se establece en `"true"`, hay opciones de moderación adicionales disponibles. | COMBO | No | `"false"`<br>`"true"` |
| `visual_input_moderation` | Habilita la moderación de contenido visual en la imagen de entrada. Este parámetro solo está disponible cuando `moderation` está establecido en `"true"`. Valor predeterminado: `False`. | BOOLEAN | No | - |
| `visual_output_moderation` | Habilita la moderación de contenido visual en la imagen de salida. Este parámetro solo está disponible cuando `moderation` está establecido en `"true"`. Valor predeterminado: `True`. | BOOLEAN | No | - |
| `seed` | La semilla controla si el nodo debe volver a ejecutarse; los resultados son no deterministas independientemente de la semilla. Valor predeterminado: `0`. | INT | No | 0 a 2147483647 |

**Nota:** Los parámetros `visual_input_moderation` y `visual_output_moderation` dependen del parámetro `moderation`. Solo están activos cuando `moderation` está establecido en `"true"`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `image` | La imagen procesada con su fondo eliminado. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/es.md)

---
**Source fingerprint (SHA-256):** `f62dcd5c9406ec09f5aab44585dd7f25ae0f7d9a934faa10a58e46ef116df110`
