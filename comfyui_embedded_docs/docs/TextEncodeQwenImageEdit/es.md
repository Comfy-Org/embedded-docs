# TextEncodeQwenImageEdit

El nodo TextEncodeQwenImageEdit procesa prompts de texto e imágenes opcionales para generar datos de condicionamiento para la generación o edición de imágenes. Utiliza un modelo CLIP para tokenizar la entrada y puede codificar opcionalmente imágenes de referencia usando un VAE para crear latentes de referencia. Cuando se proporciona una imagen, el nodo la redimensiona automáticamente para mantener dimensiones de procesamiento consistentes.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `clip` | El modelo CLIP utilizado para la tokenización de texto e imágenes | CLIP | Sí | - |
| `prompt` | Prompt de texto para la generación de condicionamiento, admite entrada multilínea y prompts dinámicos | STRING | Sí | - |
| `vae` | Modelo VAE opcional para codificar imágenes de referencia en latentes | VAE | No | - |
| `image` | Imagen de entrada opcional para fines de referencia o edición | IMAGE | No | - |

**Nota:** Cuando se proporcionan tanto `image` como `vae`, el nodo codifica la imagen en latentes de referencia y los adjunta a la salida de condicionamiento. La imagen se redimensiona automáticamente para mantener una escala de procesamiento coherente de aproximadamente 1024x1024 píxeles.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `CONDITIONING` | Datos de condicionamiento que contienen tokens de texto y latentes de referencia opcionales para la generación de imágenes | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEdit/es.md)

---
**Source fingerprint (SHA-256):** `ec6980a63eab0d6c95be3abea00b2bf3018d30a1267f0b39a21be29a3e9228fe`
