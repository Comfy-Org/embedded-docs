# Generación de video de inicio/fin de Vidu Q3

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

Este nodo genera un video interpolando entre un fotograma inicial y un fotograma final proporcionados, guiado por un texto descriptivo. Utiliza el modelo Vidu Q3 para crear una transición fluida entre las dos imágenes, produciendo un video con una duración y resolución específicas.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo a utilizar para la generación de video. Seleccionar una opción revela parámetros de configuración adicionales para `resolution`, `duration` y `audio`. | COMBO | Sí | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `model.resolution` | Resolución del video de salida. Este parámetro se revela después de seleccionar un `modelo`. | COMBO | Sí | `"720p"`<br>`"1080p"` |
| `model.duration` | Duración del video de salida en segundos (predeterminado: 5). Este parámetro se revela después de seleccionar un `modelo`. | INT | Sí | 1 a 16 |
| `model.audio` | Cuando está habilitado, genera video con sonido (incluyendo diálogos y efectos de sonido) (predeterminado: False). Este parámetro se revela después de seleccionar un `modelo`. | BOOLEAN | Sí | `True` / `False` |
| `fotograma inicial` | La imagen inicial para la secuencia de video. | IMAGE | Sí | - |
| `fotograma final` | La imagen final para la secuencia de video. | IMAGE | Sí | - |
| `prompt` | Una descripción textual que guía la generación del video (máximo 2000 caracteres). | STRING | Sí | - |
| `semilla` | Un valor semilla para controlar la aleatoriedad de la generación (predeterminado: 1). | INT | No | 0 a 2147483647 |

**Nota:** Las imágenes `first_frame` y `end_frame` deben tener relaciones de aspecto similares para obtener resultados óptimos. La relación de aspecto de las dos imágenes debe estar dentro del 80% al 125% una de la otra (una proximidad relativa entre 0.8 y 1.25).

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `video` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `4a0a8d6657702d80278dc9239370683f408d7c051e91e8396939b7b81b87b4ed`
