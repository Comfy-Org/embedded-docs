> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/es.md)

El nodo ModelSave guarda modelos entrenados o modificados en el almacenamiento de tu computadora. Toma un modelo como entrada y lo escribe en un archivo con el nombre que especifiques. Esto te permite preservar tu trabajo y reutilizar modelos en proyectos futuros.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo que se guardará en el disco |
| `prefijo_nombre_archivo` | STRING | Sí | - | El prefijo de nombre de archivo y ruta para el archivo de modelo guardado (por defecto: "diffusion_models/ComfyUI") |
| `prompt` | PROMPT | No | - | Información del prompt del flujo de trabajo (proporcionada automáticamente) |
| `extra_pnginfo` | EXTRA_PNGINFO | No | - | Metadatos adicionales del flujo de trabajo (proporcionados automáticamente) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| *Ninguno* | - | Este nodo no devuelve ningún valor de salida |