# Guardar Imagen

El nodo SaveImage guarda las imágenes de entrada como archivos PNG en tu directorio de salida de ComfyUI. Puede incrustar metadatos del flujo de trabajo, como el prompt, en cada archivo guardado, y devuelve las imágenes sin cambios para que otros nodos puedan seguir usándolas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `imágenes` | Las imágenes a guardar. | IMAGE | Sí | - |
| `prefijo_nombre_archivo` | El prefijo para el archivo a guardar. Esto puede incluir información de formato como `%date:yyyy-MM-dd%` o `%Empty Latent Image.width%` para incluir valores de nodos (por defecto: "ComfyUI"). | STRING | Sí | - |

El nodo también recibe dos entradas ocultas, `prompt` y `extra_pnginfo`, que ComfyUI completa automáticamente con el prompt del flujo de trabajo e información PNG adicional. Cuando los metadatos están habilitados, esta información se incrusta como metadatos de texto en cada archivo PNG guardado.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `images` | Las imágenes de entrada originales, devueltas sin cambios después de guardarse en el disco. | IMAGE |
| `ui` | Un resultado solo de interfaz que contiene la lista de archivos de imagen guardados (nombre de archivo, subcarpeta y tipo) para mostrarse en la interfaz. | UI_RESULT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/es.md)

---
**Source fingerprint (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`
