> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToImageApi/es.md)

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

El nodo Wan Text to Image genera imágenes basadas en descripciones textuales. Utiliza modelos de IA para crear contenido visual a partir de indicaciones escritas, compatible con entrada de texto tanto en inglés como en chino. El nodo proporciona varios controles para ajustar el tamaño, la calidad y las preferencias de estilo de la imagen de salida.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | COMBO | Sí | "wan2.5-t2i-preview" | Modelo a utilizar (predeterminado: "wan2.5-t2i-preview") |
| `prompt` | STRING | Sí | - | Indicación que describe los elementos y características visuales. Compatible con inglés y chino (predeterminado: vacío) |
| `negative_prompt` | STRING | No | - | Indicación negativa que describe lo que se debe evitar (predeterminado: vacío) |
| `width` | INT | No | 768-1440 | Ancho de la imagen en píxeles (predeterminado: 1024, incremento: 32) |
| `height` | INT | No | 768-1440 | Alto de la imagen en píxeles (predeterminado: 1024, incremento: 32) |
| `seed` | INT | No | 0-2147483647 | Semilla a utilizar para la generación (predeterminado: 0) |
| `prompt_extend` | BOOLEAN | No | - | Si se debe mejorar la indicación con asistencia de IA (predeterminado: True) |
| `watermark` | BOOLEAN | No | - | Si se debe añadir una marca de agua generada por IA al resultado (predeterminado: False) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | IMAGE | La imagen generada basada en la indicación textual |

---
**Source fingerprint (SHA-256):** `2a59551d7ff0fc0553f41561afd94092d2d950ac3e1aa3f6402436540da7d6fb`
