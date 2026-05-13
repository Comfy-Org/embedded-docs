> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/es.md)

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

Este nodo genera imágenes a partir de descripciones textuales utilizando los modelos de IA Recraft V4 o V4 Pro. Envía tu indicación a una API externa y devuelve las imágenes generadas. Puedes controlar el resultado especificando el modelo, el tamaño de la imagen y la cantidad de imágenes a crear.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `prompt` | STRING | Sí | N/A | Indicación para la generación de la imagen. Máximo 10,000 caracteres. |
| `negative_prompt` | STRING | No | N/A | Una descripción textual opcional de elementos no deseados en una imagen. |
| `model` | COMBO | Sí | `"recraftv4"`<br>`"recraftv4_pro"` | El modelo a utilizar para la generación. Seleccionar un modelo determina los tamaños de imagen disponibles. |
| `size` | COMBO | Sí | Varía según el modelo | El tamaño de la imagen generada. Las opciones disponibles dependen del modelo seleccionado. Para `recraftv4`, el valor predeterminado es "1024x1024". Para `recraftv4_pro`, el valor predeterminado es "2048x2048". |
| `n` | INT | Sí | 1 a 6 | La cantidad de imágenes a generar (predeterminado: 1). |
| `seed` | INT | Sí | 0 a 18446744073709551615 | Semilla para determinar si el nodo debe re-ejecutarse; los resultados reales son no deterministas independientemente de la semilla (predeterminado: 0). |
| `recraft_controls` | CUSTOM | No | N/A | Controles adicionales opcionales sobre la generación a través del nodo Controles Recraft. |

**Nota:** El parámetro `size` es una entrada dinámica cuyas opciones disponibles cambian según el `model` seleccionado. El valor de `seed` no garantiza resultados de imagen reproducibles.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | IMAGE | La imagen generada o lote de imágenes. |

---
**Source fingerprint (SHA-256):** `77d549a43aeee670b6c42069654017fb6b202ed83ca330389573b790bad6ae6e`
