> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/es.md)

Eres un experto en traducción técnica especializado en documentación de nodos ComfyUI del inglés al español.

## Reglas de Traducción

1. **Contenido que NO debe traducirse:**
   - Nombres de parámetros entre comillas invertidas: `image`, `seed`, `model`
   - Tipos de datos en MAYÚSCULAS: IMAGE, STRING, INT, FLOAT, MODEL, CONDITIONING, etc.
   - Valores en columna Range: números, "auto", nombres de opciones
   - Código, rutas de archivos

2. **Contenido que SÍ debe traducirse:**
   - Títulos de secciones: ## Descripción general, ## Entradas, ## Salidas
   - Todo el texto descriptivo y explicativo
   - Descripciones de parámetros

3. **Calidad de traducción:**
   - Usar español estándar y neutral
   - Mantener tono profesional pero accesible
   - Asegurar precisión técnica
   - Usar terminología técnica estándar en español

4. **Formato:**
   - Mantener todo el formato Markdown
   - Preservar estructura de tablas
   - No agregar ninguna nota o enlace al inicio del documento (será agregado automáticamente)

Por favor traduce la siguiente documentación al español, sin incluir la nota inicial del documento:

Genera videos a partir de descripciones de texto utilizando la API de Veo 3 de Google. Este nodo es compatible con múltiples modelos de Veo 3, incluyendo variantes rápidas y ligeras, y permite especificar la resolución, duración y generación de audio del video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Descripción textual del video (por defecto: "") |
| `aspect_ratio` | COMBO | Sí | "16:9"<br>"9:16" | Relación de aspecto del video de salida (por defecto: "16:9") |
| `resolution` | COMBO | No | "720p"<br>"1080p"<br>"4k" | Resolución del video de salida. 4K no está disponible para los modelos veo-3.1-lite y veo-3.0. (por defecto: "720p") |
| `negative_prompt` | STRING | No | - | Descripción textual negativa para indicar qué evitar en el video (por defecto: "") |
| `duration_seconds` | INT | No | 4-8 | Duración del video de salida en segundos, en incrementos de 2 (por defecto: 8) |
| `enhance_prompt` | BOOLEAN | No | - | Este parámetro está obsoleto y se ignora. (por defecto: True) |
| `person_generation` | COMBO | No | "ALLOW"<br>"BLOCK" | Permite o bloquea la generación de personas en el video (por defecto: "ALLOW") |
| `seed` | INT | No | 0-4294967295 | Semilla para la generación del video (0 para aleatorio) (por defecto: 0) |
| `image` | IMAGE | No | - | Imagen de referencia opcional para guiar la generación del video |
| `model` | COMBO | No | "veo-3.1-generate"<br>"veo-3.1-fast-generate"<br>"veo-3.1-lite"<br>"veo-3.0-generate-001"<br>"veo-3.0-fast-generate-001" | Modelo Veo 3 a utilizar para la generación del video (por defecto: "veo-3.0-generate-001") |
| `generate_audio` | BOOLEAN | No | - | Generar audio para el video. Compatible con todos los modelos Veo 3. (por defecto: False) |

**Nota:** El parámetro `enhance_prompt` está obsoleto y su valor se ignora. El nodo siempre mejora el prompt internamente. Además, el parámetro `resolution` solo se aplica al usar un modelo veo-3.1; se ignora para los modelos veo-3.0.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado |

---
**Source fingerprint (SHA-256):** `36ea9d3f0ea717eb7b8146ca35dfdfbe538fbbf164541ee1d1b19b660543e375`
