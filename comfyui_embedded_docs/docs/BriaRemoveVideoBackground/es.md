# Bria Quitar Fondo de Video

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `video` | El archivo de video de entrada al que se le eliminará el fondo. | VIDEO | Sí | N/A |
| `color de fondo` | Color de fondo para el video de salida. | COMBO | Sí | `"Black"`<br>`"White"`<br>`"Gray"`<br>`"Red"`<br>`"Green"`<br>`"Blue"`<br>`"Yellow"`<br>`"Cyan"`<br>`"Magenta"`<br>`"Orange"` |
| `semilla` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. (predeterminado: 0) | INT | Sí | 0 a 2147483647 |

**Nota:** El video de entrada debe tener una duración de 60 segundos o menos.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | El archivo de video procesado con el fondo eliminado y reemplazado por el color seleccionado, codificado como MP4 con códec H.264. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/es.md)

---
**Source fingerprint (SHA-256):** `dbd6b7393f893be5a40322fc96b90bb3d5f1818bdda7b8109b28f48baac44d59`
