> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxImageToVideoNode/es.md)

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

Genera videos de forma síncrona basándose en una imagen y un prompt, y parámetros opcionales utilizando la API de MiniMax. Este nodo toma una imagen de entrada y una descripción de texto para crear una secuencia de video, con varias opciones de modelo y configuraciones disponibles.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen` | IMAGE | Sí | - | Imagen a utilizar como primer fotograma de la generación de video |
| `texto de prompt` | STRING | Sí | - | Prompt de texto para guiar la generación del video (predeterminado: cadena vacía) |
| `modelo` | COMBO | Sí | "I2V-01-Director"<br>"I2V-01"<br>"I2V-01-live" | Modelo a utilizar para la generación de video (predeterminado: "I2V-01") |
| `semilla` | INT | No | 0 a 18446744073709551615 | Semilla aleatoria utilizada para crear el ruido (predeterminado: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video generado como salida |

---
**Source fingerprint (SHA-256):** `9ad1659352e363361f09d6a7a0e24835056b20cc84532247251f516b0ac284e8`
