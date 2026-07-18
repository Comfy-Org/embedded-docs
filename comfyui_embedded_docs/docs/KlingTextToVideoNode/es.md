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

El nodo Kling Text to Video convierte descripciones textuales en contenido de video. Toma indicaciones de texto y genera secuencias de video correspondientes según los ajustes de configuración especificados. El nodo admite diferentes relaciones de aspecto y modos de generación para producir videos de duración y calidad variables.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Indicación de texto positiva | STRING | Sí | - |
| `negative_prompt` | Indicación de texto negativa | STRING | Sí | - |
| `cfg_scale` | Valor de escala de configuración (predeterminado: 1.0) | FLOAT | No | 0.0 a 1.0 |
| `aspect_ratio` | Configuración de la relación de aspecto del video (predeterminado: "16:9") | COMBO | No | Opciones de KlingVideoGenAspectRatio |
| `mode` | Configuración a utilizar para la generación de video siguiendo el formato: modo / duración / nombre_del_modelo. (predeterminado: modes[8]) | COMBO | No | Múltiples opciones disponibles |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `video_id` | La salida de video generada | VIDEO |
| `video_id` | Identificador único para el video generado | STRING |
| `duration` | Información de duración del video generado | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `467f89a47890bfbfe6cebac8897fef3bce37d888d3419b248d13be89bed442f3`
