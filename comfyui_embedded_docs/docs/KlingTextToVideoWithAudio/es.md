> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoWithAudio/es.md)

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

El nodo Kling Text to Video with Audio genera un video corto a partir de una descripción textual. Envía una solicitud al servicio de IA de Kling, que procesa el prompt y devuelve un archivo de video. El nodo también puede generar audio de acompañamiento para el video basado en el texto.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model_name` | COMBO | Sí | `"kling-v2-6"` | El modelo de IA específico a utilizar para la generación de video. |
| `prompt` | STRING | Sí | - | Prompt de texto positivo. La descripción utilizada para generar el video. Debe tener entre 1 y 2500 caracteres. |
| `mode` | COMBO | Sí | `"pro"` | El modo operativo para la generación de video. |
| `aspect_ratio` | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"` | La relación ancho-alto deseada para el video generado. |
| `duration` | COMBO | Sí | `5`<br>`10` | La duración del video en segundos. |
| `generate_audio` | BOOLEAN | No | - | Controla si se genera audio para el video. Cuando está habilitado, la IA creará sonido basado en el prompt. (valor predeterminado: `True`) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El archivo de video generado. |

---
**Source fingerprint (SHA-256):** `eff4549816c347a090e2f6e8ae8ba832bd2c5b7aef7c729b51c9d72b7a814d5a`
