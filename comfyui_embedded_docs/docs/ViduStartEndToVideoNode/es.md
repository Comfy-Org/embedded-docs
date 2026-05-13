> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduStartEndToVideoNode/es.md)

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

El nodo Vidu Start End To Video Generation crea un video generando fotogramas entre un fotograma inicial y un fotograma final. Utiliza un prompt de texto para guiar el proceso de generación del video y admite varios modelos de video con diferentes configuraciones de resolución y movimiento. El nodo valida que los fotogramas inicial y final tengan relaciones de aspecto compatibles antes de procesarlos.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | `"viduq1"` | Nombre del modelo |
| `first_frame` | IMAGE | Sí | - | Fotograma inicial |
| `end_frame` | IMAGE | Sí | - | Fotograma final |
| `prompt` | STRING | No | - | Una descripción textual para la generación del video |
| `duration` | INT | No | 5-5 | Duración del video de salida en segundos (predeterminado: 5, fijo en 5 segundos) |
| `seed` | INT | No | 0-2147483647 | Semilla para la generación del video (0 para aleatorio) (predeterminado: 0) |
| `resolution` | COMBO | No | `"1080p"` | Los valores admitidos pueden variar según el modelo y la duración (predeterminado: "1080p") |
| `movement_amplitude` | COMBO | No | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` | La amplitud de movimiento de los objetos en el fotograma (predeterminado: "auto") |

**Nota:** Los fotogramas inicial y final deben tener relaciones de aspecto compatibles (validadas con una tolerancia de relación min_rel=0.8, max_rel=1.25).

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado |

---
**Source fingerprint (SHA-256):** `d859d67b3ff73977b95e3903b461509f933f9652fedc016e1cd362f6bef1b8dc`
