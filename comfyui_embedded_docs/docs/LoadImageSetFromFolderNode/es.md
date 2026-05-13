> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetFromFolderNode/es.md)

El nodo `LoadImageSetFromFolderNode` carga múltiples imágenes desde un directorio de carpeta especificado con fines de entrenamiento. Detecta automáticamente formatos de imagen comunes y puede redimensionar opcionalmente las imágenes usando diferentes métodos antes de devolverlas como un lote.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `folder` | STRING | Sí | Varias opciones disponibles | La carpeta desde la cual cargar las imágenes. |
| `resize_method` | STRING | No | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | El método a utilizar para redimensionar las imágenes (predeterminado: "None"). |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `IMAGE` | IMAGE | El lote de imágenes cargadas como un único tensor. |

---
**Source fingerprint (SHA-256):** `46fcfbf6a2ad95e707e32e54ed7b4c06bfd1cc290df122042187689f41bed828`
