# TextEncodeQwenImageEditPlus

El nodo `TextEncodeQwenImageEditPlus` procesa prompts de texto e imágenes opcionales para generar datos de condicionamiento para tareas de generación o edición de imágenes. Utiliza una plantilla especializada para analizar las imágenes de entrada y comprender cómo las instrucciones de texto deben modificarlas, luego codifica esta información para usarla en pasos posteriores de generación. El nodo puede manejar hasta tres imágenes de entrada y generar opcionalmente latentes de referencia cuando se proporciona un VAE.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `clip` | El modelo CLIP utilizado para la tokenización y codificación | CLIP | Sí | - |
| `prompt` | Instrucción de texto que describe la modificación deseada de la imagen (admite entrada multilínea y prompts dinámicos) | STRING | Sí | - |
| `vae` | Modelo VAE opcional para generar latentes de referencia a partir de las imágenes de entrada | VAE | No | - |
| `imagen1` | Primera imagen de entrada opcional para análisis y modificación | IMAGE | No | - |
| `imagen2` | Segunda imagen de entrada opcional para análisis y modificación | IMAGE | No | - |
| `imagen3` | Tercera imagen de entrada opcional para análisis y modificación | IMAGE | No | - |

**Nota:** Cuando se proporciona un VAE, el nodo genera latentes de referencia a partir de todas las imágenes de entrada proporcionadas. Se pueden procesar hasta tres imágenes a la vez. Las imágenes se escalan a un área objetivo de 384x384 píxeles (conservando la relación de aspecto) para el procesamiento de visión y lenguaje, y a dimensiones divisibles por 8 (con un área objetivo de 1024x1024 píxeles) para la codificación VAE.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `CONDITIONING` | Datos de condicionamiento codificados que contienen tokens de texto y latentes de referencia opcionales para la generación de imágenes | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/es.md)

---
**Source fingerprint (SHA-256):** `5eea53a84045924b44d445244e6149b341188d22573aaaced87bac8a139dac96`
