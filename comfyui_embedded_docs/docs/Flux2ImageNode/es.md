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

Genera imágenes utilizando el modelo Flux.2 [pro] o Flux.2 [max] a partir de un texto de instrucción (prompt) e imágenes de referencia opcionales. Este nodo envía tu solicitud a la API de BFL, consulta el resultado y devuelve la imagen generada como un tensor.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Instrucción para la generación o edición de la imagen (por defecto: cadena vacía). | STRING | Sí | N/A |
| `modelo` | La versión del modelo Flux.2 a utilizar. La selección de un modelo desbloquea parámetros adicionales para ancho, alto e imágenes de referencia opcionales. | COMBO | Sí | `"Flux.2 [pro]"`<br>`"Flux.2 [max]"` |
| `semilla` | La semilla aleatoria utilizada para crear el ruido. Se puede configurar para aleatorizar después de cada generación (por defecto: 0). | INT | Sí | 0 a 18446744073709551615 |

**Parámetros Adicionales (desbloqueados por la selección de `model`):**

Cuando seleccionas un modelo, los siguientes parámetros estarán disponibles:

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model.width` | El ancho de la imagen generada en píxeles. | INT | Sí | 256 a 1440 |
| `model.height` | La altura de la imagen generada en píxeles. | INT | Sí | 256 a 1440 |
| `model.images` | Imágenes de referencia opcionales para guiar la generación. Se admite un máximo de 8 imágenes. | IMAGE | No | 0 a 8 imágenes |

**Restricciones:**
- El número máximo de imágenes de referencia es 8. Si se proporcionan más de 8 imágenes, se generará un error.
- Los valores de `model.width` y `model.height` afectan el costo de la generación (consulta la lógica de la insignia de precio en el código fuente).

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `image` | La imagen generada como un tensor, descargada desde el resultado de la API de BFL. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2ImageNode/es.md)

---
**Source fingerprint (SHA-256):** `664ddf45d42f64e4882cc959018f7874915325f2d46519c6bb9a0c5a501228f7`
