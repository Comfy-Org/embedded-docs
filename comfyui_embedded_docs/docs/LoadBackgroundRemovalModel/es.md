# Cargar modelo de eliminación de fondo

Carga un modelo de eliminación de fondo desde un archivo y lo deja listo para que otros nodos lo utilicen al eliminar fondos de imágenes. El archivo del modelo se selecciona entre los archivos disponibles en la carpeta de eliminación de fondo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `bg_removal_name` | El modelo utilizado para eliminar fondos de imágenes. | COMBO | Sí | Lista de archivos de modelo disponibles (lista ordenada de archivos en la carpeta background_removal) |

**Nota:** El nodo genera un error si el archivo seleccionado no contiene un modelo de eliminación de fondo válido.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `bg_model` | El modelo de eliminación de fondo cargado, listo para ser utilizado por otros nodos para procesar imágenes. | BACKGROUND_REMOVAL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/es.md)

---
**Source fingerprint (SHA-256):** `76f6536eae849a8b63f46f11c6afcf8c89774e4e89a5976e051253acc6108bcc`
