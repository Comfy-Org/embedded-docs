> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/es.md)

Codifica texto y establece la condición de resolución para PixArt Alpha. Este nodo procesa la entrada de texto y añade información de ancho y alto para crear datos de condicionamiento específicamente para modelos PixArt Alpha. No aplica para modelos PixArt Sigma.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `width` | INT | Sí | 0 a MAX_RESOLUTION | La dimensión de ancho para el condicionamiento de resolución (predeterminado: 1024) |
| `height` | INT | Sí | 0 a MAX_RESOLUTION | La dimensión de alto para el condicionamiento de resolución (predeterminado: 1024) |
| `text` | STRING | Sí | - | Entrada de texto a codificar, admite entrada multilínea y mensajes dinámicos |
| `clip` | CLIP | Sí | - | Modelo CLIP utilizado para tokenización y codificación |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Datos de condicionamiento codificados con tokens de texto e información de resolución |

---
**Source fingerprint (SHA-256):** `d15df3c7bcca10ec85f0689d6631a6b89aa89e609193c36b658b1bc97f90ee9a`
