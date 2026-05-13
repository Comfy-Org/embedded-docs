> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/es.md)

El nodo PreviewAny muestra una vista previa de cualquier tipo de dato de entrada en formato de texto. Acepta cualquier tipo de dato como entrada y lo convierte en una representación legible como cadena de texto para su visualización. El nodo maneja automáticamente diferentes tipos de datos, incluyendo cadenas de texto, números, valores booleanos y objetos complejos, intentando serializarlos en formato JSON.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `source` | ANY | Sí | Cualquier tipo de dato | Acepta cualquier tipo de dato de entrada para su visualización previa |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `UI Text Display` | STRING | Muestra los datos de entrada convertidos a formato de texto en la interfaz de usuario. También devuelve el texto como salida de cadena para su posterior procesamiento. |

---
**Source fingerprint (SHA-256):** `6011c39a31ef9a6786a1dff6e135edcf35def2f715b49301dd49a6467f859271`
