# Bria Eliminar Fondo de Video (Transparente)

Este nodo elimina el fondo de un video utilizando el servicio de IA de Bria y genera los fotogramas recortados junto con una máscara alfa. Conecte ambas salidas a un nodo de composición, o envíelas a un nodo Guardar WEBM para escribir un video transparente.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `video` | El video de entrada a procesar | VIDEO | Sí | - |
| `semilla` | La semilla controla si el nodo debe re-ejecutarse; los resultados no son deterministas independientemente de la semilla (predeterminado: 0) | INT | Sí | 0 a 2147483647 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `imágenes` | Los fotogramas del video con el fondo eliminado | IMAGE |
| `mask` | La máscara alfa para los fotogramas del video | MASK |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaTransparentVideoBackground/es.md)

---
**Source fingerprint (SHA-256):** `45fb3fc185b5c6420d6ac2b87f2403566e1ef6dcdc57791fb833b6ccb2a64cd9`
