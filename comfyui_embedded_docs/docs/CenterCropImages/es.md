> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CenterCropImages/es.md)

El nodo **Center Crop Images** recorta una imagen desde su centro hasta un ancho y alto especificados. Calcula la región central de la imagen de entrada y extrae un área rectangular con las dimensiones definidas. Si el tamaño de recorte solicitado es mayor que la imagen, el recorte se limitará a los bordes de la imagen.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se va a recortar. |
| `width` | INT | Sí | 1 a 8192 | El ancho del área de recorte (predeterminado: 512). |
| `height` | INT | Sí | 1 a 8192 | El alto del área de recorte (predeterminado: 512). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | La imagen resultante después de la operación de recorte centrado. |

---
**Source fingerprint (SHA-256):** `4361b6630ab1833e035d6ab04a130fb36fff33cddc36b54ff5a2d8e04534a555`
