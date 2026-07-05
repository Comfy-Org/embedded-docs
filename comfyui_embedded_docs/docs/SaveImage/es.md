# Guardar Imagen

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/en.md)

El nodo SaveImage guarda las imágenes que recibe en tu directorio `ComfyUI/output`. Guarda cada imagen como un archivo PNG y puede incrustar metadatos del flujo de trabajo, como el prompt, en el archivo guardado para futuras referencias.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imágenes` | Las imágenes a guardar. | IMAGE | Sí | - |
| `prefijo_nombre_archivo` | El prefijo para el archivo a guardar. Puede incluir información de formato como `%date:yyyy-MM-dd%` o `%Empty Latent Image.width%` para incluir valores de nodos (por defecto: "ComfyUI"). | STRING | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `images` | Este nodo genera un resultado de interfaz de usuario que contiene una lista de las imágenes guardadas con sus nombres de archivo y subcarpetas. No produce datos para conectar a otros nodos. | UI_RESULT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/es.md)

---
**Source fingerprint (SHA-256):** `fa88c26e5e03f788dcc545434a54124c5e9d03b559da67f0857b52faec0e97e7`
