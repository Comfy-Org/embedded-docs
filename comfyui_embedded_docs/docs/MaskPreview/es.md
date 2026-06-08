El nodo MaskPreview guarda los datos de la máscara como una imagen de previsualización en el directorio de salida de ComfyUI, permitiéndote inspeccionar visualmente los datos de la máscara durante la ejecución del flujo de trabajo. Convierte la máscara de entrada a un formato adecuado para la visualización de imágenes y la guarda con un prefijo de nombre de archivo configurable.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `mask` | Los datos de la máscara que se previsualizarán y guardarán como imagen | MASK | Sí | - |
| `filename_prefix` | Prefijo para el nombre del archivo de salida (predeterminado: "ComfyUI") | STRING | No | - |
| `prompt` | Información del prompt para metadatos (proporcionada automáticamente) | PROMPT | No | - |
| `extra_pnginfo` | Información PNG adicional para metadatos (proporcionada automáticamente) | EXTRA_PNGINFO | No | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `ui` | Contiene la información de la imagen de previsualización y los metadatos para mostrar en la interfaz de usuario | DICT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/es.md)

---
**Source fingerprint (SHA-256):** `9f64adf4a0130368618fc1ca3655192686815ab10b4153f9552ef23149928e3f`
