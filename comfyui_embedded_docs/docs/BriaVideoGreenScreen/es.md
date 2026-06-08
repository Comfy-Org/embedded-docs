# Bria Video Green Screen

Este nodo reemplaza el fondo de un video con una pantalla de clave cromática sólida utilizando la API de Bria. Procesa el video de entrada y devuelve un nuevo video donde el fondo original ha sido eliminado y reemplazado con un color uniforme de pantalla verde o azul.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `video` | El video de entrada a procesar | VIDEO | Sí | Archivo de video |
| `green_shade` | Tono de clave cromática sólida aplicado detrás del primer plano: broadcast_green (#00B140), chroma_green (#00FF00) o blue_screen (#0000FF) | STRING | Sí | `"broadcast_green"`<br>`"chroma_green"`<br>`"blue_screen"` |
| `seed` | La semilla controla si el nodo debe re-ejecutarse; los resultados no son deterministas independientemente de la semilla (valor predeterminado: 0) | INT | Sí | 0 a 2147483647 |

**Nota:** El video de entrada no debe exceder los 60 segundos de duración.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `video` | El video procesado con el fondo original reemplazado por el tono de clave cromática seleccionado | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoGreenScreen/es.md)

---
**Source fingerprint (SHA-256):** `663b41bf51bd8d871a59e756f226e4bf6244bb616ebcd2e8ccfa426137f2a05b`
