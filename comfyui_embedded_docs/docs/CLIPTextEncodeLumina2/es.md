El nodo Codificación de Texto CLIP para Lumina2 codifica un mensaje de sistema y un mensaje de usuario utilizando un modelo CLIP en una incrustación que puede guiar al modelo de difusión para generar imágenes específicas. Combina un mensaje de sistema predefinido con tu mensaje de texto personalizado y los procesa a través del modelo CLIP para crear datos de condicionamiento para la generación de imágenes.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `system_prompt` | Lumina2 proporciona dos tipos de mensajes de sistema: "superior" genera imágenes con una alineación superior entre imagen y texto; "alignment" genera imágenes de alta calidad con el mayor grado de alineación entre imagen y texto. | STRING | Sí | `"superior"`<br>`"alignment"` |
| `user_prompt` | El texto a codificar. Admite entrada multilínea y mensajes dinámicos. | STRING | Sí | N/A |
| `clip` | El modelo CLIP utilizado para codificar el texto. | CLIP | Sí | N/A |

**Nota:** La entrada `clip` es obligatoria y no puede ser nula. Si la entrada de clip no es válida, el nodo generará un error indicando que el punto de control puede no contener un modelo CLIP o codificador de texto válido.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `CONDITIONING` | Un condicionamiento que contiene el texto incrustado utilizado para guiar al modelo de difusión. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/es.md)

---
**Source fingerprint (SHA-256):** `fcc0802180ffc2c0757b395850d54632da011473da0c6b1c5268b42da3747024`
