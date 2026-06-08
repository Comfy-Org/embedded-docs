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

El nodo Moonvalley Marey Imagen a Video transforma una imagen de referencia en un video utilizando la API de Moonvalley. Toma una imagen de entrada y un prompt de texto para generar un video con resolución, ajustes de calidad y controles creativos especificados. El nodo gestiona todo el proceso, desde la carga de la imagen hasta la generación y descarga del video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `image` | La imagen de referencia utilizada para generar el video | IMAGE | Sí | - |
| `prompt` | Descripción textual para la generación del video (entrada multilínea) | STRING | Sí | - |
| `negative_prompt` | Texto de prompt negativo para excluir elementos no deseados (predeterminado: lista extensa de prompts negativos) | STRING | No | - |
| `resolution` | Resolución del video de salida (predeterminado: "16:9 (1920 x 1080)") | COMBO | No | "16:9 (1920 x 1080)"<br>"9:16 (1080 x 1920)"<br>"1:1 (1152 x 1152)"<br>"4:3 (1536 x 1152)"<br>"3:4 (1152 x 1536)" |
| `prompt_adherence` | Escala de guía para el control de generación (predeterminado: 4.5, paso: 1.0) | FLOAT | No | 1.0 - 20.0 |
| `seed` | Valor de semilla aleatoria (predeterminado: 9, control después de generar habilitado) | INT | No | 0 - 4294967295 |
| `steps` | Número de pasos de eliminación de ruido (predeterminado: 33, paso: 1) | INT | No | 1 - 100 |

**Restricciones:**

- La imagen de entrada debe tener dimensiones entre 300x300 píxeles y la altura/ancho máximo permitido
- La longitud del texto del prompt y del prompt negativo está limitada a la longitud máxima de prompt de Moonvalley Marey

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El video generado como salida | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyImg2VideoNode/es.md)

---
**Source fingerprint (SHA-256):** `674e69a7f106f6f961f10c179008b7bb1147bf0e569c72d207a105f3fab2aaf5`
