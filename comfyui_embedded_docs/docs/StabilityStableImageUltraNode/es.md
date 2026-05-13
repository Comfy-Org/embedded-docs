> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageUltraNode/es.md)

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

Genera imágenes de forma síncrona basándose en un prompt y una resolución. Este nodo crea imágenes utilizando el modelo Stable Image Ultra de Stability AI, procesando tu prompt de texto y generando una imagen correspondiente con la relación de aspecto y el estilo especificados.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Lo que deseas ver en la imagen de salida. Un prompt fuerte y descriptivo que defina claramente elementos, colores y sujetos generará mejores resultados. Para controlar el peso de una palabra específica, usa el formato `(palabra:peso)`, donde `palabra` es la palabra cuyo peso deseas controlar y `peso` es un valor entre 0 y 1. Por ejemplo: `El cielo era de un (azul:0.3) y (verde:0.8) nítidos` transmitiría un cielo que era azul y verde, pero más verde que azul. |
| `aspect_ratio` | COMBO | Sí | `"1:1"`<br>`"16:9"`<br>`"21:9"`<br>`"2:3"`<br>`"3:2"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"9:21"` | Relación de aspecto de la imagen generada (predeterminado: "1:1"). |
| `style_preset` | COMBO | No | `"3d-model"`<br>`"analog-film"`<br>`"anime"`<br>`"cinematic"`<br>`"comic-book"`<br>`"digital-art"`<br>`"enhance"`<br>`"fantasy-art"`<br>`"isometric"`<br>`"line-art"`<br>`"low-poly"`<br>`"modeling-compound"`<br>`"neon-punk"`<br>`"origami"`<br>`"photographic"`<br>`"pixel-art"`<br>`"tile-texture"` | Estilo deseado opcional de la imagen generada. Selecciona "None" para no aplicar ningún preset de estilo. |
| `seed` | INT | Sí | 0 - 4294967294 | La semilla aleatoria utilizada para crear el ruido. |
| `image` | IMAGE | No | - | Imagen de entrada opcional para generación de imagen a imagen. |
| `negative_prompt` | STRING | No | - | Un texto que describe lo que NO deseas ver en la imagen de salida. Esta es una función avanzada. |
| `image_denoise` | FLOAT | No | 0.0 - 1.0 | Denoising de la imagen de entrada; 0.0 produce una imagen idéntica a la de entrada, 1.0 es como si no se hubiera proporcionado ninguna imagen (predeterminado: 0.5). |

**Nota:** Cuando no se proporciona una imagen de entrada, el parámetro `image_denoise` se desactiva automáticamente y se ignora.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | IMAGE | La imagen generada basada en los parámetros de entrada. |

---
**Source fingerprint (SHA-256):** `2fd9e106a3460a39c33ecc9a15ab6414dab1914fdc43e4f546827e02c889cf62`
