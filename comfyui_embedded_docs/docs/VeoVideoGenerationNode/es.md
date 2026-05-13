> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeoVideoGenerationNode/es.md)

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias para mejorar, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeoVideoGenerationNode/en.md)

Genera videos a partir de indicaciones de texto utilizando la API de Veo 2 de Google. Este nodo puede crear videos a partir de descripciones de texto y entradas de imagen opcionales, con control sobre parámetros como la relación de aspecto, la duración y más.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `prompt` | STRING | Sí | - | Descripción textual del video (predeterminado: vacío) |
| `aspect_ratio` | COMBO | Sí | "16:9"<br>"9:16" | Relación de aspecto del video de salida (predeterminado: "16:9") |
| `negative_prompt` | STRING | No | - | Indicación de texto negativa para guiar qué evitar en el video (predeterminado: vacío) |
| `duration_seconds` | INT | No | 5-8 | Duración del video de salida en segundos (predeterminado: 5) |
| `enhance_prompt` | BOOLEAN | No | - | Si se debe mejorar la indicación con asistencia de IA (predeterminado: True). Este es un parámetro avanzado. |
| `person_generation` | COMBO | No | "ALLOW"<br>"BLOCK" | Si se permite generar personas en el video (predeterminado: "ALLOW"). Este es un parámetro avanzado. |
| `seed` | INT | No | 0-4294967295 | Semilla para la generación del video (0 para aleatorio) (predeterminado: 0). Este es un parámetro avanzado. |
| `image` | IMAGE | No | - | Imagen de referencia opcional para guiar la generación del video |
| `modelo` | COMBO | No | "veo-2.0-generate-001" | Modelo Veo 2 a utilizar para la generación del video (predeterminado: "veo-2.0-generate-001") |

**Nota:** El parámetro `generate_audio` solo está disponible para los modelos Veo 3.0 y es manejado automáticamente por el nodo según el modelo seleccionado. Al usar modelos Veo 3.0, el parámetro `enhance_prompt` se fuerza a True.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El archivo de video generado |

---
**Source fingerprint (SHA-256):** `1a8b8ffe82fce32566815248f4a2434a1b865b5e5651935ccb3b92c7e38adee9`
