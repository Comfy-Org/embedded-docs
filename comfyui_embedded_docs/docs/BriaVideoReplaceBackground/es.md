# Bria Reemplazar Fondo de Video

Este nodo reemplaza el fondo de un video con una imagen o video proporcionado mediante la API de Bria. La salida conserva la resolución y la velocidad de fotogramas del video en primer plano; un fondo con una relación de aspecto diferente se estira para ajustarse, por lo que usar relaciones de aspecto coincidentes produce resultados sin distorsión.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `video` | Video en primer plano cuyo fondo será reemplazado. | VIDEO | Sí | - |
| `background_image` | Imagen de fondo para componer detrás del primer plano. Proporcione una imagen de fondo o un video de fondo, no ambos. | IMAGE | No | - |
| `background_video` | Video de fondo para componer detrás del primer plano. Proporcione una imagen de fondo o un video de fondo, no ambos. | VIDEO | No | - |
| `seed` | La semilla controla si el nodo debe re-ejecutarse; los resultados no son deterministas independientemente de la semilla. (predeterminado: 0) | INT | Sí | 0 a 2147483647 |

**Nota:** Debe proporcionar exactamente uno de `background_image` o `background_video` — no ambos y no ninguno. El video en primer plano debe tener una duración de 60 segundos o menos.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `video` | El video resultante con el fondo reemplazado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoReplaceBackground/es.md)

---
**Source fingerprint (SHA-256):** `4eb9650e5ca88baf2a91a9309b87936b3d18b88e314a56ab4c73d06a9143c645`
