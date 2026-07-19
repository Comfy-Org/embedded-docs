# OpenAI Sora - Video

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

El nodo OpenAIVideoSora2 genera videos utilizando los modelos Sora de OpenAI. Crea contenido de video basado en instrucciones de texto e imágenes de entrada opcionales, y luego devuelve el video generado como salida. El nodo admite diferentes duraciones y resoluciones de video según el modelo seleccionado.

**AVISO DE OBSOLESCENCIA:** OpenAI dejará de ofrecer la API de Sora v2 en septiembre de 2026. Este nodo será eliminado de ComfyUI en ese momento.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo OpenAI Sora a utilizar para la generación de video (predeterminado: "sora-2") | COMBO | Sí | "sora-2"<br>"sora-2-pro" |
| `prompt` | Texto guía; puede estar vacío si hay una imagen de entrada presente (predeterminado: vacío) | STRING | Sí | - |
| `tamaño` | La resolución del video generado (predeterminado: "1280x720") | COMBO | Sí | "720x1280"<br>"1280x720"<br>"1024x1792"<br>"1792x1024" |
| `duración` | La duración del video generado en segundos (predeterminado: 8) | COMBO | Sí | 4<br>8<br>12 |
| `imagen` | Imagen de entrada opcional para la generación de video | IMAGE | No | - |
| `semilla` | Semilla para determinar si el nodo debe re-ejecutarse; los resultados reales son no deterministas independientemente de la semilla (predeterminado: 0) | INT | No | 0 a 2147483647 |

**Restricciones y Limitaciones:**

- El modelo "sora-2" solo admite las resoluciones "720x1280" y "1280x720"
- Solo se admite una imagen de entrada al utilizar el parámetro `image`
- Los resultados son no deterministas independientemente del valor de la semilla

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El video generado como salida | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIVideoSora2/es.md)

---
**Source fingerprint (SHA-256):** `c87b696dd92c6a6a929f49d189a375b1ebed80bf47f24667ee17c0b210330e55`
