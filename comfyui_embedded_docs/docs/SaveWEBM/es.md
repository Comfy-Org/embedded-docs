# GuardarWEBM

El nodo SaveWEBM guarda una secuencia de imágenes como un archivo de video WEBM. Toma múltiples imágenes de entrada y las codifica en un video utilizando el códec VP9 o AV1 con configuraciones de calidad y velocidad de fotogramas ajustables. El archivo de video resultante se guarda en el directorio de salida con metadatos que incluyen información de la instrucción (prompt).

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imágenes` | Secuencia de imágenes de entrada para codificar como fotogramas de video | IMAGE | Sí | - |
| `prefijo_nombre_archivo` | Prefijo para el nombre del archivo de salida (predeterminado: "ComfyUI") | STRING | No | - |
| `códec` | Códec de video a utilizar para la codificación | COMBO | Sí | "vp9"<br>"av1" |
| `fps` | Velocidad de fotogramas para el video de salida (predeterminado: 24.0) | FLOAT | No | 0.01-1000.0 |
| `crf` | Configuración de calidad donde un crf más alto significa menor calidad con un tamaño de archivo más pequeño, y un crf más bajo significa mayor calidad con un tamaño de archivo más grande (predeterminado: 32.0) | FLOAT | No | 0-63.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `ui` | Vista previa del video que muestra el archivo WEBM guardado | PREVIEW |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/es.md)

---
**Source fingerprint (SHA-256):** `761ce5148c273ffe3789be75c2a00268241d3ec7ecebd5b10efd1b1cc98d85ea`
