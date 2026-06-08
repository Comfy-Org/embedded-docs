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

Genera imágenes de forma síncrona a través del endpoint GPT Image de OpenAI. Este nodo puede crear nuevas imágenes a partir de indicaciones de texto o editar imágenes existentes cuando se proporciona una imagen de entrada y una máscara opcional. Es compatible con múltiples modelos GPT Image, incluyendo gpt-image-1, gpt-image-1.5 y gpt-image-2.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Indicación de texto para GPT Image (predeterminado: "") | STRING | Sí | - |
| `seed` | Semilla aleatoria para la generación (predeterminado: 0) - aún no implementada en el backend | INT | No | 0 a 2147483647 |
| `quality` | Calidad de la imagen, afecta el costo y el tiempo de generación (predeterminado: "low") | COMBO | No | "low"<br>"medium"<br>"high" |
| `background` | Devuelve la imagen con o sin fondo (predeterminado: "auto") | COMBO | No | "auto"<br>"opaque"<br>"transparent" |
| `size` | Tamaño de la imagen. Seleccione "Custom" para usar el ancho y alto personalizados (solo GPT Image 2) (predeterminado: "auto") | COMBO | No | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024"<br>"2048x2048"<br>"2048x1152"<br>"1152x2048"<br>"3840x2160"<br>"2160x3840"<br>"Custom" |
| `n` | Cuántas imágenes generar (predeterminado: 1) | INT | No | 1 a 8 |
| `image` | Imagen de referencia opcional para edición de imágenes | IMAGE | No | - |
| `mask` | Máscara opcional para inpainting (las áreas blancas serán reemplazadas) | MASK | No | - |
| `model` | Modelo GPT Image a utilizar (predeterminado: "gpt-image-2") | COMBO | No | "gpt-image-1"<br>"gpt-image-1.5"<br>"gpt-image-2" |
| `custom_width` | Se usa solo cuando `size` es "Custom". Debe ser múltiplo de 16 (solo GPT Image 2) (predeterminado: 1024) | INT | No | 1024 a 3840 |
| `custom_height` | Se usa solo cuando `size` es "Custom". Debe ser múltiplo de 16 (solo GPT Image 2) (predeterminado: 1024) | INT | No | 1024 a 3840 |

**Restricciones de parámetros:**

- Cuando se proporciona `image`, el nodo cambia al modo de edición de imágenes
- `mask` solo se puede usar cuando se proporciona `image`
- Al usar `mask`, solo se admiten imágenes individuales (el tamaño del lote debe ser 1)
- `mask` e `image` deben tener el mismo tamaño
- La resolución personalizada (`size` = "Custom") solo es compatible con el modelo gpt-image-2
- El ancho y alto personalizados deben ser múltiplos de 16
- La relación de aspecto de la resolución personalizada no debe exceder 3:1
- El total de píxeles de la resolución personalizada debe estar entre 655,360 y 8,294,400
- El fondo transparente no es compatible con el modelo gpt-image-2
- Los tamaños mayores a 1536x1024 (por ejemplo, 2048x2048, 3840x2160) solo son compatibles con el modelo gpt-image-2

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `IMAGE` | Imagen(es) generada(s) o editada(s) | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/es.md)

---
**Source fingerprint (SHA-256):** `44b258d6afcb388db3836427abdd5a7cb5c09a0328efceef7e114dd61a38eae1`
