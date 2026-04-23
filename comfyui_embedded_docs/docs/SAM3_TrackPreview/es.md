> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_TrackPreview/es.md)

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

Este nodo crea una vista previa de video de objetos rastreados, dibujando cada objeto rastreado con una superposición de color distintiva y una etiqueta numérica. No genera ningún tensor de imagen o video; en su lugar, guarda el video de vista previa resultante directamente en un archivo temporal.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `track_data` | TRACK_DATA | Sí | - | Los datos de rastreo que contienen máscaras empaquetadas e información de objetos provenientes de un nodo de rastreo SAM3. |
| `images` | IMAGE | No | - | Imágenes de entrada opcionales para usar como fondo de la vista previa. Si no se proporcionan, se utiliza un fondo negro. |
| `opacity` | FLOAT | No | 0.0 a 1.0 (paso: 0.05) | La opacidad de la superposición de color aplicada a los objetos rastreados (predeterminado: 0.5). |
| `fps` | FLOAT | No | 1.0 a 120.0 (paso: 1.0) | La velocidad de fotogramas del video de salida (predeterminado: 24.0). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `ui` | PREVIEW_VIDEO | Un elemento de interfaz de usuario que muestra el video de vista previa generado. No se devuelve ningún tensor de datos. |