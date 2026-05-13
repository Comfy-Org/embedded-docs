> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/es.md)

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias para mejorar, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/en.md)

El nodo de Generación de Video a partir de Texto de Vidu crea videos a partir de descripciones textuales. Utiliza el modelo de generación de video Vidu para transformar tus indicaciones de texto en contenido de video con configuraciones personalizables para duración, relación de aspecto y estilo visual.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `modelo` | COMBO | Sí | `viduq1` | Nombre del modelo |
| `prompt` | STRING | Sí | - | Descripción textual para la generación del video |
| `duración` | INT | No | 5-5 | Duración del video de salida en segundos (predeterminado: 5) |
| `semilla` | INT | No | 0-2147483647 | Semilla para la generación del video (0 para aleatorio) (predeterminado: 0) |
| `relación_de_aspecto` | COMBO | No | `16:9`<br>`9:16`<br>`1:1` | Relación de aspecto del video de salida |
| `resolución` | COMBO | No | `1080p` | Los valores compatibles pueden variar según el modelo y la duración |
| `amplitud_movimiento` | COMBO | No | `auto`<br>`small`<br>`medium`<br>`large` | Amplitud de movimiento de los objetos en el encuadre |

**Nota:** El campo `prompt` es obligatorio y no puede estar vacío. El parámetro `duration` actualmente está fijado en 5 segundos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El video generado a partir de la indicación de texto |

---
**Source fingerprint (SHA-256):** `0d331d3eab8a4af9c90831f3f8fd8ae34aa0c393142cb6f89404edc94024d95f`
