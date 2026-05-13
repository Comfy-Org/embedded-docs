> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxTextToVideoNode/es.md)

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

Genera videos de forma síncrona basándose en un prompt y parámetros opcionales utilizando la API de MiniMax. Este nodo crea contenido de video a partir de descripciones de texto conectándose al servicio de texto a video de MiniMax.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `prompt_text` | STRING | Sí | - | Prompt de texto para guiar la generación del video |
| `model` | COMBO | No | "T2V-01"<br>"T2V-01-Director" | Modelo a utilizar para la generación de video (predeterminado: "T2V-01") |
| `seed` | INT | No | 0 a 18446744073709551615 | Semilla aleatoria utilizada para crear el ruido (predeterminado: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El video generado basado en el prompt de entrada |

---
**Source fingerprint (SHA-256):** `bdbd8f9defc4c626f07b36c1ba9859155fa90a2d7ef9a491c30dac4d003d39be`
