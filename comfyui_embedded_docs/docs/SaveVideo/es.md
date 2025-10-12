> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/es.md)

El nodo SaveVideo guarda contenido de video de entrada en tu directorio de salida de ComfyUI. Te permite especificar el prefijo del nombre de archivo, el formato de video y el códec para el archivo guardado. El nodo maneja automáticamente la nomenclatura de archivos con incrementos de contador y puede incluir metadatos del flujo de trabajo en el video guardado.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Sí | - | El video a guardar. |
| `prefijo_nombre_archivo` | STRING | No | - | El prefijo para el archivo a guardar. Puede incluir información de formato como %date:yyyy-MM-dd% o %Empty Latent Image.width% para incluir valores de nodos (por defecto: "video/ComfyUI"). |
| `formato` | COMBO | No | Múltiples opciones disponibles | El formato para guardar el video (por defecto: "auto"). |
| `códec` | COMBO | No | Múltiples opciones disponibles | El códec a utilizar para el video (por defecto: "auto"). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| *Sin salidas* | - | Este nodo no devuelve ningún dato de salida. |
