> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2ImageNode/es.md)

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

Genera imágenes utilizando el modelo Flux.2 [pro] o Flux.2 [max] a partir de un texto de indicación e imágenes de referencia opcionales. Este nodo envía tu solicitud a la API de BFL, consulta el resultado y devuelve la imagen generada como un tensor.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `prompt` | STRING | Sí | N/A | Indicación para la generación o edición de la imagen (valor predeterminado: cadena vacía). |
| `model` | COMBO | Sí | `"Flux.2 [pro]"`<br>`"Flux.2 [max]"` | La versión del modelo Flux.2 a utilizar. Al seleccionar un modelo se desbloquean parámetros adicionales para ancho, alto e imágenes de referencia opcionales. |
| `seed` | INT | Sí | 0 a 18446744073709551615 | La semilla aleatoria utilizada para crear el ruido. Se puede configurar para aleatorizar después de cada generación (valor predeterminado: 0). |

**Parámetros Adicionales (desbloqueados por la selección de `model`):**

Cuando seleccionas un modelo, los siguientes parámetros estarán disponibles:

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model.width` | INT | Sí | 256 a 1440 | El ancho de la imagen generada en píxeles. |
| `model.height` | INT | Sí | 256 a 1440 | La altura de la imagen generada en píxeles. |
| `model.images` | IMAGE | No | 0 a 8 imágenes | Imágenes de referencia opcionales para guiar la generación. Se admite un máximo de 8 imágenes. |

**Restricciones:**
- El número máximo de imágenes de referencia es 8. Si se proporcionan más de 8 imágenes, se generará un error.
- Los valores de `model.width` y `model.height` afectan el costo de la generación (consulta la lógica de la etiqueta de precio en el código fuente).

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | La imagen generada como un tensor, descargada desde el resultado de la API de BFL. |