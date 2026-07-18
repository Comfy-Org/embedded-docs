# SyncTalkingImageNode

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

Por favor traduce la siguiente documentación al español, sin incluir la aviso de IA:

5. **CRÍTICO - Nombres de salida:** La primera columna de la tabla de Salidas contiene nombres de salida (ej. `positive`, `negative`, `latent`, `image`, `model`, `conditioning`) que DEBEN permanecer en inglés. Traducir estos nombres crea entradas duplicadas y rompe la estructura del documento.

Convierte un retrato estático en un video parlante impulsado por audio de voz, utilizando el modelo sync-3 de sync.so. La duración de salida coincide con la duración del audio, y el costo escala con la duración de la salida.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `image` | Una sola imagen con un rostro claramente visible, de hasta 4K (4096x2160). | IMAGE | Sí | Exactamente una imagen requerida |
| `audio` | Audio de voz que impulsa el video parlante; la duración de la salida coincide con él. Conecta cualquier nodo TTS aquí para impulsar la animación desde texto. | AUDIO | Sí | Duración máxima: 600 segundos |
| `prompt` | Guía opcional sobre cómo cobra vida el retrato, ej. 'haz que el sujeto sonría y mire a la cámara'. Déjalo vacío para un movimiento de habla natural. (predeterminado: "") | STRING | No | Texto multilínea |
| `seed` | La semilla controla si el nodo debe re-ejecutarse; los resultados no son deterministas independientemente de la semilla. (predeterminado: 0) | INT | No | 0 a 2147483647 |
| `model` | Modelo de generación de sync.so. La entrada de imagen es exclusiva de sync-3. | COMBO | Sí | `"sync-3"` |
| `speaker_selection` | Qué rostro animar cuando varias personas son visibles. `default`: dejar que el modelo decida. `coordinates`: apuntar al rostro en el píxel (speaker_x, speaker_y) de la imagen. La detección automática no es compatible con imágenes. (predeterminado: "default") | COMBO | No | `"default"`<br>`"coordinates"` |
| `speaker_x` | Coordenada X en píxeles del rostro del hablante. Solo se usa cuando speaker_selection es 'coordinates'. (predeterminado: 0) | INT | No | 0 a 4096 |
| `speaker_y` | Coordenada Y en píxeles del rostro del hablante. Solo se usa cuando speaker_selection es 'coordinates'. (predeterminado: 0) | INT | No | 0 a 4096 |
| `auto_downscale` | Redimensiona automáticamente la imagen si excede el límite de entrada de 4K (4096x2160); las coordenadas del hablante se escalan para coincidir. Cuando está deshabilitado, una imagen sobredimensionada genera un error. (predeterminado: True) | BOOLEAN | No | True<br>False |

**Nota:** Los parámetros `speaker_x` y `speaker_y` solo se utilizan cuando `speaker_selection` está configurado en `"coordinates"`. Cuando `auto_downscale` está habilitado, las coordenadas del hablante se escalan automáticamente para coincidir con las dimensiones de la imagen redimensionada.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `video` | El video parlante generado con el retrato animado sincronizado con el audio de entrada. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SyncTalkingImageNode/es.md)

---
**Source fingerprint (SHA-256):** `21f722cdcc5ff017949887ed2252854feebb9b913034dc6a6c3ce196ad089468`
