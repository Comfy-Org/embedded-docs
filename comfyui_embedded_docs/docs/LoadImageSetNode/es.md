> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetNode/es.md)

El nodo LoadImageSetNode carga múltiples imágenes desde el directorio de entrada para su procesamiento por lotes y fines de entrenamiento. Admite varios formatos de imagen y puede redimensionar opcionalmente las imágenes utilizando diferentes métodos. Este nodo procesa todas las imágenes seleccionadas como un lote y las devuelve como un único tensor.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `images` | IMAGE | Sí | Múltiples archivos de imagen | Selecciona múltiples imágenes del directorio de entrada. Admite formatos PNG, JPG, JPEG, WEBP, BMP, GIF, JPE, APNG, TIF y TIFF. Permite la selección por lotes de imágenes. |
| `resize_method` | STRING | No | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | Método opcional para redimensionar las imágenes cargadas (predeterminado: "None"). Elija "None" para mantener los tamaños originales, "Stretch" para forzar el redimensionamiento, "Crop" para mantener la relación de aspecto recortando, o "Pad" para mantener la relación de aspecto añadiendo relleno. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `IMAGE` | IMAGE | Un tensor que contiene todas las imágenes cargadas como un lote para su procesamiento posterior. |

---
**Source fingerprint (SHA-256):** `acf0255bcf170ef3ac3b86a3f3e060c3b81064ca8924918a026ec8e3b86f7ac0`
