# Guardar Texto

El nodo Guardar Texto escribe contenido de texto en un archivo dentro del directorio de salida. Admite el guardado en formato .txt, .md o .json, y maneja automáticamente el formato JSON con sangría cuando se proporciona JSON válido.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `text` | El contenido de texto a guardar en un archivo. Esta entrada debe estar conectada desde otro nodo. | STRING | Sí | - |
| `filename_prefix` | Prefijo para el nombre del archivo de salida. Se añade un contador de 5 dígitos para evitar sobrescribir archivos existentes (predeterminado: "ComfyUI"). | STRING | No | - |
| `format` | El formato de archivo para guardar el texto (predeterminado: "txt"). Cuando se selecciona "json", el texto JSON válido se imprime con sangría de 2 espacios; de lo contrario, el texto se guarda tal cual. | COMBO | No | `"txt"`<br>`"md"`<br>`"json"` |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `text` | El contenido de texto original que se guardó en el archivo | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/es.md)

---
**Source fingerprint (SHA-256):** `5644d143f415773115b38d7af6d9afea20c9eadef2cea836b0384c15e0dcba6a`
