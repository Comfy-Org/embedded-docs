> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseTextToVideoApi/es.md)

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

## Resumen

Genera un video basado en una descripción de texto utilizando el modelo HappyHorse. Este nodo envía tu descripción y configuración a la API de HappyHorse, espera a que se genere el video y luego descarga el resultado.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | DICT | Sí | Ver Descripción | Un diccionario que contiene la selección del modelo y sus parámetros asociados. El modelo debe ser `"happyhorse-1.0-t2v"`. Este diccionario incluye los siguientes subparámetros:<br><br>**`prompt`** (STRING): La descripción textual del video que deseas generar. Admite inglés y chino. (valor predeterminado: "").<br>**`resolution`** (COMBO): La resolución del video de salida. Opciones: `"720P"`, `"1080P"`.<br>**`ratio`** (COMBO): La relación de aspecto del video de salida. Opciones: `"16:9"`, `"9:16"`, `"1:1"`, `"4:3"`, `"3:4"`.<br>**`duration`** (INT): La duración del video en segundos. (valor predeterminado: 5, mínimo: 3, máximo: 15, paso: 1). |
| `seed` | INT | Sí | 0 a 2147483647 | Semilla a utilizar para la generación. Usar la misma semilla con las mismas entradas producirá el mismo resultado. (valor predeterminado: 0). |
| `watermark` | BOOLEAN | No | True / False | Si se debe agregar una marca de agua generada por IA al resultado. (valor predeterminado: False). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `VIDEO` | VIDEO | El archivo de video generado. |