> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/es.md)

Codifica texto y establece el acondicionamiento de resolución para PixArt Alpha. Este nodo procesa la entrada de texto y añade información de ancho y alto para crear datos de acondicionamiento específicos para modelos PixArt Alpha. No se aplica a modelos PixArt Sigma.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `width` | INT | Input | 1024 | 0 a MAX_RESOLUTION | La dimensión de ancho para el acondicionamiento de resolución |
| `height` | INT | Input | 1024 | 0 a MAX_RESOLUTION | La dimensión de alto para el acondicionamiento de resolución |
| `text` | STRING | Input | - | - | Entrada de texto a codificar, admite entrada multilínea y prompts dinámicos |
| `clip` | CLIP | Input | - | - | Modelo CLIP utilizado para tokenización y codificación |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Datos de acondicionamiento codificados con tokens de texto e información de resolución |