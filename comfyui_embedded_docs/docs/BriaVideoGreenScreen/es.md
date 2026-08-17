# Bria Video Green Screen

Este nodo reemplaza el fondo de un video con una pantalla de croma sólida mediante la API de Bria. Procesa el video de entrada y devuelve un nuevo video donde el fondo original ha sido eliminado y reemplazado por un color de pantalla verde o azul uniforme.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `video` | El video de entrada a procesar | VIDEO | Sí | Archivo de video |
| `green_shade` | Tono de croma sólido aplicado detrás del primer plano: broadcast_green (#00B140), chroma_green (#00FF00) o blue_screen (#0000FF) | COMBO | Sí | `"broadcast_green"`<br>`"chroma_green"`<br>`"blue_screen"` |
| `seed` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla (valor predeterminado: 0) | INT | Sí | 0 a 2147483647 |

**Nota:** El video de entrada no debe superar los 60 segundos de duración.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El video procesado con el fondo original reemplazado por el tono de croma seleccionado, devuelto como un video MP4 (H.264) | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoGreenScreen/es.md)

---
**Source fingerprint (SHA-256):** `70d2951d0adbbe7492b2bc97d04be6591b65f040ca4b414754ad6365c5db45cf`
