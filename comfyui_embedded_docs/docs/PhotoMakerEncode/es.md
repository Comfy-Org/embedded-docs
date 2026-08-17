# PhotoMakerEncode

PhotoMakerEncode crea datos de condicionamiento para la generación de imágenes con IA al combinar una imagen de referencia con un prompt de texto. Busca la palabra "photomaker" en el prompt de texto y, cuando la encuentra, utiliza el modelo PhotoMaker para aplicar las características visuales de la imagen de referencia en esa posición del prompt.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `photomaker` | El modelo PhotoMaker utilizado para procesar la imagen de referencia y generar incrustaciones basadas en imágenes | PHOTOMAKER | Sí | - |
| `image` | La imagen de referencia que proporciona características visuales para el condicionamiento | IMAGE | Sí | - |
| `clip` | El modelo CLIP utilizado para la tokenización y codificación de texto | CLIP | Sí | - |
| `text` | El prompt de texto para la generación de condicionamiento. Admite múltiples líneas y prompts dinámicos (predeterminado: "photograph of photomaker") | STRING | Sí | - |

**Nota:** La palabra "photomaker" debe aparecer como una palabra separada en el prompt de texto (la coincidencia distingue entre mayúsculas y minúsculas) para que se aplique el condicionamiento basado en imágenes. Cuando está presente, las características de la imagen se inyectan en esa posición del prompt. Si no se encuentra "photomaker", el nodo devuelve el condicionamiento de texto estándar sin influencia de la imagen.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `CONDITIONING` | Los datos de condicionamiento que contienen incrustaciones de imagen y texto para guiar la generación de imágenes, junto con la salida agrupada (pooled) del codificador de texto CLIP | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/es.md)

---
**Source fingerprint (SHA-256):** `490a90c504ade253c2bb055e0efb1eb015ba6d7faf8f2370cac188871f678986`
