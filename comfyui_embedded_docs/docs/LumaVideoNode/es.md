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

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Instrucción para la generación del video (por defecto: cadena vacía). Debe tener al menos 3 caracteres. | STRING | Sí | - |
| `modelo` | El modelo de generación de video a utilizar. | COMBO | Sí | `"ray_1_6"`<br>`"ray_2"` |
| `relación de aspecto` | La relación de aspecto para el video generado (por defecto: "16:9"). | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `resolución` | La resolución de salida del video (por defecto: "540p"). Este parámetro se ignora al usar el modelo `ray_1_6`. | COMBO | Sí | `"540p"`<br>`"720p"`<br>`"1080p"` |
| `duración` | La duración del video generado. Este parámetro se ignora al usar el modelo `ray_1_6`. | COMBO | Sí | `"5s"`<br>`"9s"` |
| `bucle` | Si el video debe reproducirse en bucle (por defecto: Falso). | BOOLEAN | Sí | - |
| `semilla` | Semilla para determinar si el nodo debe re-ejecutarse; los resultados reales son no deterministas independientemente de la semilla (por defecto: 0). | INT | Sí | 0 a 18446744073709551615 |
| `luma_concepts` | Conceptos de cámara opcionales para dictar el movimiento de la cámara a través del nodo Luma Concepts. | CUSTOM | No | - |

**Nota:** Al usar el modelo `ray_1_6`, los parámetros `duration` y `resolution` se ignoran automáticamente y no afectan la generación.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `44482bc91c3df2cc9ac22d06197668af45849e8bfde8bd435905f11f2593342c`
