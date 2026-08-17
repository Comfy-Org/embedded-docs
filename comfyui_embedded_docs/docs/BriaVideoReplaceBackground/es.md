# Bria Video Reemplazar Fondo

Reemplaza el fondo de un video con una imagen o video proporcionado usando Bria. La salida conserva la resolución y la velocidad de fotogramas del primer plano; un fondo con una relación de aspecto diferente se estira para ajustarse, así que hazlo coincidir para obtener resultados sin distorsión.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `video` | Video del primer plano cuyo fondo se reemplaza. | VIDEO | Sí | - |
| `background_image` | Imagen de fondo para componer detrás del primer plano. Proporciona una imagen de fondo o un video de fondo, no ambos. | IMAGE | No | - |
| `background_video` | Video de fondo para componer detrás del primer plano. Proporciona una imagen de fondo o un video de fondo, no ambos. | VIDEO | No | - |
| `seed` | La semilla controla si el nodo debe ejecutarse nuevamente; los resultados son no deterministas independientemente de la semilla. (predeterminado: 0) | INT | Sí | 0 a 2147483647 |

**Nota:** Debes proporcionar exactamente uno de `background_image` o `background_video` — no ambos ni ninguno. Tanto el video del primer plano como el video de fondo deben tener una duración de 60 segundos o menos. Si se proporciona una imagen de fondo, su canal alfa (transparencia) se elimina antes de subirla.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El video resultante con el fondo reemplazado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoReplaceBackground/es.md)

---
**Source fingerprint (SHA-256):** `c487cf7dd434b8523ce64f241c2171c82bb5e0abdc5c3ca3e8b1a1259aeab490`
