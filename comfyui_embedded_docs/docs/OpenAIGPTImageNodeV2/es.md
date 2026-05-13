> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/es.md)

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

Este nodo genera imágenes utilizando la API de OpenAI GPT Image. Es compatible con múltiples modelos, permite proporcionar imágenes de entrada para edición y puede usar una máscara para especificar qué partes de la imagen modificar.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `prompt` | STRING | Sí | N/A | Texto de instrucción para GPT Image (valor predeterminado: ""). |
| `model` | COMBO | Sí | `"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` | El modelo OpenAI GPT Image a utilizar. Seleccionar un modelo revela parámetros adicionales específicos de ese modelo. |
| `model.size` | COMBO | Sí | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` | Tamaño de la imagen. Seleccione 'Custom' para usar ancho y alto personalizados (valor predeterminado: "auto"). Solo disponible para `gpt-image-2`. |
| `model.custom_width` | INT | No | 1024 a 3840 | Se usa solo cuando `size` es 'Custom'. Debe ser múltiplo de 16 (valor predeterminado: 1024). Solo disponible para `gpt-image-2`. |
| `model.custom_height` | INT | No | 1024 a 3840 | Se usa solo cuando `size` es 'Custom'. Debe ser múltiplo de 16 (valor predeterminado: 1024). Solo disponible para `gpt-image-2`. |
| `model.background` | COMBO | Sí | `"auto"`<br>`"opaque"` | Devuelve la imagen con o sin fondo (valor predeterminado: "auto"). Solo disponible para `gpt-image-2`. |
| `model.quality` | COMBO | Sí | `"standard"`<br>`"hd"` | La calidad de la imagen generada. Solo disponible para `gpt-image-2`. |
| `model.images` | IMAGE | No | N/A | Imágenes de entrada para edición. Solo disponible para `gpt-image-2`. |
| `model.mask` | MASK | No | N/A | Una máscara para especificar qué partes de la imagen de entrada editar. Solo disponible para `gpt-image-2`. |
| `n` | INT | Sí | 1 a 8 | Cuántas imágenes generar (valor predeterminado: 1). |
| `seed` | INT | Sí | 0 a 2147483647 | Semilla para reproducibilidad (valor predeterminado: 0). Nota: aún no implementado en el backend. |

**Restricciones y limitaciones de los parámetros:**

- Al usar `gpt-image-2` con un `model.size` de "Custom", el `custom_width` y `custom_height` deben ser múltiplos de 16, el borde máximo debe ser <= 3840, la relación de aspecto no debe exceder 3:1, y el recuento total de píxeles debe estar entre 655,360 y 8,294,400.
- Si se proporciona una `mask`, se requiere una imagen de entrada (`model.images`). No se puede usar una máscara sin una imagen de entrada.
- No se puede usar una máscara con múltiples imágenes de entrada.
- Cuando se proporciona una máscara, las dimensiones de la máscara deben coincidir con las dimensiones de la imagen de entrada.
- El parámetro `seed` actualmente no es funcional.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | La imagen o imágenes generadas. |

---
**Source fingerprint (SHA-256):** `a757208cf6cc151594599b35b0ef73f2caf7274189e948799211c0714a6a8f89`
