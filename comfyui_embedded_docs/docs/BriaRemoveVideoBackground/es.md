# Bria Quitar Fondo de Video

Este nodo elimina el fondo de un video mediante el servicio Bria AI. Procesa el video de entrada y reemplaza el fondo original con un color sólido de tu elección. La operación se realiza a través de una API externa, y el resultado se devuelve como un nuevo archivo de video.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `video` | El archivo de video de entrada del que se eliminará el fondo. | VIDEO | Sí | N/D |
| `background_color` | Color de fondo para el video de salida. | COMBO | Sí | `"Black"`<br>`"White"`<br>`"Gray"`<br>`"Red"`<br>`"Green"`<br>`"Blue"`<br>`"Yellow"`<br>`"Cyan"`<br>`"Magenta"`<br>`"Orange"` |
| `seed` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. (valor predeterminado: 0) | INT | Sí | 0 to 2147483647 |

**Nota:** El video de entrada debe tener una duración de 60 segundos o menos.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | El archivo de video procesado con el fondo eliminado y reemplazado por el color seleccionado. El video de salida está codificado como MP4 con H.264. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/es.md)

---
**Source fingerprint (SHA-256):** `dbd6b7393f893be5a40322fc96b90bb3d5f1818bdda7b8109b28f48baac44d59`
