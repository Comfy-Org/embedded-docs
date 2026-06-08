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

El nodo Runway Image to Video (Gen3a Turbo) genera un video a partir de un único fotograma inicial utilizando el modelo Gen3a Turbo de Runway. Toma un texto de instrucción y un fotograma de imagen inicial, luego crea una secuencia de video basada en la duración y relación de aspecto especificadas. Este nodo se conecta a la API de Runway para procesar la generación de forma remota.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Texto de instrucción para la generación (por defecto: "") | STRING | Sí | N/A |
| `fotograma_inicial` | Fotograma inicial que se utilizará para el video | IMAGE | Sí | N/A |
| `duración` | Duración del video en segundos (por defecto: "5") | COMBO | Sí | `"5"`<br>`"10"` |
| `relación` | Relación de aspecto del video generado (por defecto: "1280x720") | COMBO | Sí | `"1280x720"`<br>`"720x1280"`<br>`"1920x1080"`<br>`"1080x1920"`<br>`"1080x1080"` |
| `semilla` | Semilla aleatoria para la generación (por defecto: 0) | INT | No | 0 a 4294967295 |

**Restricciones de los parámetros:**

- El `start_frame` debe tener dimensiones que no superen los 7999x7999 píxeles.
- El `start_frame` debe tener una relación de aspecto entre 0.5 y 2.0.
- El `prompt` debe contener al menos un carácter (no puede estar vacío).

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | La secuencia de video generada | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/es.md)

---
**Source fingerprint (SHA-256):** `4f3270ce070ce50580699292e21c5f9e3b1a56dd8ac981f67a9026ef6fc8ed76`
