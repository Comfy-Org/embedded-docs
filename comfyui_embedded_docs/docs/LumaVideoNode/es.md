> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaVideoNode/es.md)

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

Genera videos de forma síncrona basándose en un texto de instrucción y configuraciones de salida. Este nodo crea contenido de video utilizando descripciones textuales y diversos parámetros de generación, produciendo el video final una vez que el proceso de generación se completa.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Instrucción para la generación del video (por defecto: cadena vacía). Debe tener al menos 3 caracteres. |
| `modelo` | COMBO | Sí | `"ray_1_6"`<br>`"ray_2"` | El modelo de generación de video a utilizar. |
| `relación de aspecto` | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` | La relación de aspecto para el video generado (por defecto: "16:9"). |
| `resolución` | COMBO | Sí | `"540p"`<br>`"720p"`<br>`"1080p"` | La resolución de salida del video (por defecto: "540p"). Este parámetro se ignora al usar el modelo `ray_1_6`. |
| `duración` | COMBO | Sí | `"5s"`<br>`"9s"` | La duración del video generado. Este parámetro se ignora al usar el modelo `ray_1_6`. |
| `bucle` | BOOLEAN | Sí | - | Si el video debe reproducirse en bucle (por defecto: Falso). |
| `semilla` | INT | Sí | 0 a 18446744073709551615 | Semilla para determinar si el nodo debe re-ejecutarse; los resultados reales son no deterministas independientemente de la semilla (por defecto: 0). |
| `luma_concepts` | CUSTOM | No | - | Conceptos de cámara opcionales para dictar el movimiento de la cámara a través del nodo Luma Concepts. |

**Nota:** Al usar el modelo `ray_1_6`, los parámetros `duration` y `resolution` se ignoran automáticamente y no afectan la generación.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado. |

---
**Source fingerprint (SHA-256):** `44482bc91c3df2cc9ac22d06197668af45849e8bfde8bd435905f11f2593342c`
