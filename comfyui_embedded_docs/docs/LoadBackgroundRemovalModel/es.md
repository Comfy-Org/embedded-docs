# Cargar modelo de eliminación de fondo

Carga un modelo de eliminación de fondos desde un archivo. Este nodo prepara el modelo para su uso en la eliminación de fondos de imágenes.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `nombre_del_modelo_de_eliminación_de_fondo` | El modelo utilizado para eliminar fondos de imágenes. Seleccione de la lista de archivos de modelo de eliminación de fondos disponibles. | COMBO | Sí | Lista de archivos de modelo disponibles (ordenados alfabéticamente) |

Nota: Si el archivo seleccionado no contiene un modelo válido de eliminación de fondos, el nodo genera un RuntimeError.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `modelo_de_fondo` | El modelo de eliminación de fondos cargado, listo para ser utilizado por otros nodos para procesar imágenes. | BACKGROUND_REMOVAL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/es.md)

---
**Source fingerprint (SHA-256):** `76f6536eae849a8b63f46f11c6afcf8c89774e4e89a5976e051253acc6108bcc`
