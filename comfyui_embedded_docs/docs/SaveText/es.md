# Guardar Texto

El nodo Save Text escribe contenido de texto en un archivo en el directorio de salida. Admite guardar en formato .txt, .csv, .md o .json, y automáticamente aplica un formato legible al JSON cuando se proporciona JSON válido.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `text` | El contenido de texto a guardar en un archivo. Esta entrada debe estar conectada desde otro nodo. | STRING | Sí | - |
| `filename_prefix` | Prefijo para el nombre del archivo de salida. Se añade un contador de 5 dígitos para evitar sobrescribir archivos existentes (predeterminado: "ComfyUI"). | STRING | No | - |
| `format` | El formato de archivo en el que se guardará el texto (predeterminado: "txt"). Cuando se selecciona "json", el texto JSON válido se formatea con sangría de 2 espacios; de lo contrario, el texto se guarda tal cual. | COMBO | No | `"txt"`<br>`"csv"`<br>`"md"`<br>`"json"` |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `text` | El contenido de texto original que se guardó en el archivo | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/es.md)

---
**Source fingerprint (SHA-256):** `09bd896cab770358132834892c1b37efd2ffa0cb0aa7b02b7ef91163331dc9b1`
