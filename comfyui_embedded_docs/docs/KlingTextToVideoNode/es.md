> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/es.md)

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

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `prompt` | STRING | Sí | - | Indicación de texto positiva |
| `negative_prompt` | STRING | Sí | - | Indicación de texto negativa |
| `cfg_scale` | FLOAT | No | 0.0 a 1.0 | Valor de escala de configuración (predeterminado: 1.0) |
| `aspect_ratio` | COMBO | No | Opciones de KlingVideoGenAspectRatio | Configuración de la relación de aspecto del video (predeterminado: "16:9") |
| `mode` | COMBO | No | Múltiples opciones disponibles | Configuración a utilizar para la generación de video siguiendo el formato: modo / duración / nombre_del_modelo. (predeterminado: modes[8]) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `video_id` | VIDEO | La salida de video generada |
| `duration` | STRING | Identificador único para el video generado |
| `duration` | STRING | Información de duración del video generado |

---
**Source fingerprint (SHA-256):** `467f89a47890bfbfe6cebac8897fef3bce37d888d3419b248d13be89bed442f3`
