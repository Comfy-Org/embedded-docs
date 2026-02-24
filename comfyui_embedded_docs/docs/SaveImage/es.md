> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/es.md)

El nodo SaveImage guarda las imágenes que recibe en el directorio `ComfyUI/output`. Guarda cada imagen como un archivo PNG y puede incrustar metadatos del flujo de trabajo, como el prompt, en el archivo guardado para referencia futura.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imágenes` | IMAGE | Sí | - | Las imágenes a guardar. |
| `prefijo_nombre_archivo` | STRING | Sí | - | El prefijo para el archivo a guardar. Puede incluir información de formato como `%date:yyyy-MM-dd%` o `%Empty Latent Image.width%` para incluir valores de otros nodos (por defecto: "ComfyUI"). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `ui` | UI_RESULT | Este nodo genera un resultado de interfaz de usuario que contiene una lista de las imágenes guardadas con sus nombres de archivo y subcarpetas. No genera datos para conectar a otros nodos. |
