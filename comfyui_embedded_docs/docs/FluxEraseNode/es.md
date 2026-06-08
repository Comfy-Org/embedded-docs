# Nodo Flux Erase

Elimina el objeto enmascarado de una imagen y reconstruye el fondo. Pinte la máscara sobre lo que desea borrar, y el nodo rellena el área con contenido de fondo plausible.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `imagen` | La imagen de entrada a procesar | IMAGE | Sí | - |
| `máscara` | Las áreas blancas se eliminan; las áreas negras se conservan | MASK | Sí | - |
| `dilatar_pixeles` | Expande los bordes de la máscara para garantizar una cobertura limpia de los bordes del objeto (valor predeterminado: 10) | INT | Sí | 0 a 25 |
| `seed` | La semilla aleatoria utilizada para crear el ruido (valor predeterminado: 0) | INT | No | 0 a 2147483647 |

**Nota:** La imagen de entrada debe tener al menos 256x256 píxeles en ambas dimensiones. La máscara se redimensiona automáticamente para coincidir con las dimensiones de la imagen.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|-------------|-------------|-----------|
| `IMAGE` | La imagen resultante con el objeto enmascarado eliminado y el fondo reconstruido | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxEraseNode/es.md)

---
**Source fingerprint (SHA-256):** `70cf3223bc1ba0528cf99e84f073bd7a1bbcc26164cef99f4deb1645038fbf11`
