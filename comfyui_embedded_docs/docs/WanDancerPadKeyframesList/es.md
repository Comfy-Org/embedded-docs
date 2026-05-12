> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframesList/es.md)

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

Este nodo toma una secuencia de imágenes y una pista de audio opcional, y las divide en un número especificado de segmentos rellenados. Está diseñado para preparar secuencias de fotogramas clave para la generación de video, donde cada segmento se rellena hasta una longitud uniforme y se crea una máscara correspondiente para indicar qué fotogramas son válidos.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `images` | IMAGE | Sí | N/A | La secuencia de imágenes de entrada que se dividirá en segmentos. |
| `segment_length` | INT | Sí | 1 a 10000 | Longitud de cada segmento en fotogramas (predeterminado: 149). |
| `num_segments` | INT | Sí | 1 a 100 | Cuántos segmentos rellenados emitir como listas (predeterminado: 1). |
| `audio` | AUDIO | No | N/A | Audio a segmentar para cada segmento emitido. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `keyframes_sequence` | IMAGE | Una lista de secuencias de fotogramas clave rellenadas, una por cada segmento. |
| `keyframes_mask` | MASK | Una lista de máscaras que indican los fotogramas válidos para cada segmento. |
| `audio_segment` | AUDIO | Una lista de segmentos de audio, uno por cada segmento de video. |