# Bria Quitar Fondo de Imagen

Este nodo elimina el fondo de una imagen utilizando el servicio Bria RMBG 2.0. Envía la imagen a una API externa para su procesamiento y devuelve el resultado con el fondo eliminado.

## Entradas

El selector `moderation` revela opciones de moderación adicionales cuando se establece en `"true"`.

### Entradas comunes

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `moderation` | Configuración de moderación. Cuando se establece en `"true"`, opciones de moderación adicionales quedan disponibles. | DYNAMIC_COMBO | No | `"false"`<br>`"true"` |
| `image` | La imagen de entrada de la que se eliminará el fondo. | IMAGE | Sí | - |
| `seed` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. Por defecto: `0`. | INT | No | 0 a 2147483647 |

### Entradas de moderación "true"

Estos parámetros aparecen solo cuando `moderation` se establece en `"true"`. La opción `"false"` no añade entradas adicionales.

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `visual_input_moderation` | Habilita la moderación de contenido visual en la imagen de entrada. Por defecto: `False`. | BOOLEAN | No | - |
| `visual_output_moderation` | Habilita la moderación de contenido visual en la imagen de salida. Por defecto: `True`. | BOOLEAN | No | - |

**Nota:** Los parámetros `visual_input_moderation` y `visual_output_moderation` dependen del parámetro `moderation`. Solo están activos cuando `moderation` se establece en `"true"`.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `image` | La imagen procesada con su fondo eliminado. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/es.md)

---
**Source fingerprint (SHA-256):** `f62dcd5c9406ec09f5aab44585dd7f25ae0f7d9a934faa10a58e46ef116df110`
