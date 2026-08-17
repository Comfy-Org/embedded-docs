# GuardarWEBM

El nodo SaveWEBM guarda una secuencia de imágenes como un archivo de video WEBM. Codifica las imágenes de entrada en un video utilizando el códec VP9 o AV1 con configuración de velocidad de fotogramas y calidad ajustables, y guarda el archivo en el directorio de salida. Los metadatos del prompt y del flujo de trabajo se incrustan en el archivo de video cuando están disponibles.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `images` | La secuencia de imágenes a codificar en el video. Las imágenes RGBA se guardan con su canal alfa como transparencia (solo códec vp9). | IMAGE | Sí | - |
| `filename_prefix` | Prefijo para el nombre del archivo de salida; se añaden automáticamente un contador y la extensión .webm (por defecto: "ComfyUI") | STRING | No | - |
| `codec` | Códec de video utilizado para la codificación | COMBO | Sí | "vp9"<br>"av1" |
| `fps` | Velocidad de fotogramas para el video de salida (por defecto: 24.0) | FLOAT | No | 0.01-1000.0 |
| `crf` | Un crf más alto significa menor calidad con un tamaño de archivo más pequeño; un crf más bajo significa mayor calidad y mayor tamaño de archivo (por defecto: 32.0) | FLOAT | No | 0-63.0 |

**Nota sobre el canal alfa:** El canal alfa de las imágenes RGBA solo se conserva cuando se utiliza el códec vp9. Al usar el códec av1, se ignora el canal alfa y solo se codifican los datos RGB.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `images` | La secuencia de imágenes de entrada, pasada sin cambios | IMAGE |
| `ui` | Vista previa de video que muestra el archivo WEBM guardado | PREVIEW |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/es.md)

---
**Source fingerprint (SHA-256):** `55496b10af66a908ef035d236f8fab8193c1ae44408dab9d202deadff3be2715`
