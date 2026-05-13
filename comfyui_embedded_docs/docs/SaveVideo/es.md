> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/es.md)

El nodo SaveVideo guarda contenido de video de entrada en tu directorio de salida de ComfyUI. Permite especificar el prefijo del nombre de archivo, el formato de video y el códec para el archivo guardado. El nodo maneja automáticamente la numeración de archivos con incrementos de contador y puede incluir metadatos del flujo de trabajo en el video guardado.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `video` | VIDEO | Sí | - | El video a guardar. |
| `prefijo_nombre_archivo` | STRING | No | - | El prefijo para el archivo a guardar. Puede incluir información de formato como %date:yyyy-MM-dd% o %Empty Latent Image.width% para incluir valores de nodos (predeterminado: "video/ComfyUI"). |
| `formato` | COMBO | No | `"auto"`<br>`"mp4"`<br>`"webm"`<br>`"mkv"`<br>`"gif"` | El formato para guardar el video (predeterminado: "auto"). |
| `códec` | COMBO | No | `"auto"`<br>`"h264"`<br>`"h265"`<br>`"vp9"`<br>`"av1"`<br>`"prores"` | El códec a utilizar para el video (predeterminado: "auto"). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| *Sin salidas* | - | Este nodo no devuelve ningún dato de salida. |

---
**Source fingerprint (SHA-256):** `506ddc8820924688cccb9fd838ff9c0f5217a38f708f28f15a060be9325cea61`
