# SaveText

El nodo Guardar Texto escribe contenido de texto en un archivo dentro del directorio de salida. Admite el guardado en formato .txt, .md o .json, y maneja automáticamente el formato JSON con sangría cuando se proporciona JSON válido.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `text` | El contenido de texto que se guardará en un archivo | STRING | Sí | - |
| `filename_prefix` | Prefijo para el nombre del archivo de salida (predeterminado: "ComfyUI") | STRING | No | - |
| `format` | El formato de archivo en el que se guardará el texto (predeterminado: "txt") | STRING | No | `"txt"`<br>`"md"`<br>`"json"` |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `text` | El contenido de texto original que se guardó en el archivo | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/es.md)

---
**Source fingerprint (SHA-256):** `5644d143f415773115b38d7af6d9afea20c9eadef2cea836b0384c15e0dcba6a`
