# Bria Eliminar Fondo de Video (Transparente)

Este nodo elimina el fondo de un video utilizando el servicio de IA de Bria y devuelve los fotogramas recortados junto con una máscara alfa. Conecta ambas salidas a un nodo de composición, o envíalas a un nodo Save WEBM para escribir un video transparente.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `video` | El video de entrada a procesar. La duración máxima es de 60 segundos. | VIDEO | Sí | - |
| `seed` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla (por defecto: 0) | INT | Sí | 0 to 2147483647 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `images` | Los fotogramas del video con el fondo eliminado | IMAGE |
| `mask` | La máscara alfa para los fotogramas del video, donde 1 significa transparente | MASK |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaTransparentVideoBackground/es.md)

---
**Source fingerprint (SHA-256):** `536bd52af29218d2a342086e92799d3d9310da5ae5cbf02d705ba7503a4d73c8`
