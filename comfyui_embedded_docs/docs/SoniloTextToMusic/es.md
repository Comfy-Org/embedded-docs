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

El nodo Sonilo Text to Music genera música a partir de una descripción textual utilizando el modelo de IA de Sonilo. Proporcionas un prompt que describe la música que deseas, y el nodo envía una solicitud al servicio Sonilo para crear un archivo de audio. Puedes especificar una duración objetivo o dejar que el modelo la infiera a partir de tu prompt.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt de texto que describe la música a generar. Este campo es obligatorio. | STRING | Sí | N/A |
| `duration` | Duración objetivo en segundos. Establecer en 0 para que el modelo infiera la duración a partir del prompt. Máximo: 6 minutos (360 segundos). Valor por defecto: 0. | INT | No | 0 a 360 |
| `seed` | Semilla para reproducibilidad. Actualmente es ignorada por el servicio Sonilo, pero se mantiene para la consistencia del grafo. Valor por defecto: 0. | INT | No | 0 a 18446744073709551615 |

**Nota:** La entrada `seed` se proporciona para la consistencia del flujo de trabajo, pero actualmente no afecta la salida del servicio Sonilo.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `audio` | La música generada como archivo de audio. | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloTextToMusic/es.md)

---
**Source fingerprint (SHA-256):** `aac2762d9310179279ed7dcc9766f38342400902de2f8791b78d8092a96b86b4`
