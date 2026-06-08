Codifica texto y establece la condición de resolución para PixArt Alpha. Este nodo procesa la entrada de texto y añade información de ancho y alto para crear datos de condicionamiento específicamente para modelos PixArt Alpha. No aplica para modelos PixArt Sigma.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `width` | La dimensión de ancho para el condicionamiento de resolución (predeterminado: 1024) | INT | Sí | 0 a MAX_RESOLUTION |
| `height` | La dimensión de alto para el condicionamiento de resolución (predeterminado: 1024) | INT | Sí | 0 a MAX_RESOLUTION |
| `text` | Entrada de texto a codificar, admite entrada multilínea y mensajes dinámicos | STRING | Sí | - |
| `clip` | Modelo CLIP utilizado para tokenización y codificación | CLIP | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `CONDITIONING` | Datos de condicionamiento codificados con tokens de texto e información de resolución | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/es.md)

---
**Source fingerprint (SHA-256):** `d15df3c7bcca10ec85f0689d6631a6b89aa89e609193c36b658b1bc97f90ee9a`
