# GuardarLatente

El nodo SaveLatent guarda muestras latentes en disco como archivos .latent para su uso o intercambio posteriores. Escribe los datos del tensor latente en la carpeta de salida utilizando el prefijo de nombre de archivo especificado e incrusta metadatos opcionales, como la información del prompt. El nodo también devuelve las muestras latentes originales sin cambios, para que el flujo de trabajo pueda seguir utilizándolas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `samples` | Las muestras latentes que se guardarán en disco | LATENT | Sí | - |
| `filename_prefix` | El prefijo utilizado para generar el nombre de archivo de salida y la ruta de subcarpeta (por defecto: "latents/ComfyUI") | STRING | Sí | - |
| `prompt` | Los datos del prompt del flujo de trabajo, almacenados como metadatos JSON en el archivo guardado (entrada oculta, suministrada automáticamente) | PROMPT | No | - |
| `extra_pnginfo` | Metadatos adicionales del flujo de trabajo, almacenados como JSON en el archivo guardado (entrada oculta, suministrada automáticamente) | EXTRA_PNGINFO | No | - |

Nota: Los metadatos se escriben en el archivo .latent guardado a menos que ComfyUI se inicie con el argumento `--disable-metadata`. El archivo guardado se nombra usando el patrón `{filename}_{5-digit counter}_.latent`, por ejemplo `ComfyUI_00001_.latent`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `samples` | Las muestras latentes originales, devueltas sin cambios | LATENT |
| `ui` | Detalles de ubicación del archivo (nombre de archivo, subcarpeta y tipo de salida) para el archivo latente guardado | UI |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/es.md)

---
**Source fingerprint (SHA-256):** `137d52d589d93d8229940a8572621ab6eeb25a4e13ac05172e9f8609f1af038a`
