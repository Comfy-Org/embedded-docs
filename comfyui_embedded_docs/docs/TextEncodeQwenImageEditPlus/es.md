> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/es.md)

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

El nodo TextEncodeQwenImageEditPlus procesa instrucciones de texto e imágenes opcionales para generar datos de condicionamiento para tareas de generación o edición de imágenes. Utiliza una plantilla especializada para analizar las imágenes de entrada y comprender cómo las instrucciones de texto deben modificarlas, luego codifica esta información para su uso en pasos posteriores de generación. El nodo puede manejar hasta tres imágenes de entrada y, opcionalmente, generar latentes de referencia cuando se proporciona un VAE.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `clip` | CLIP | Sí | - | El modelo CLIP utilizado para la tokenización y codificación |
| `prompt` | STRING | Sí | - | Instrucción de texto que describe la modificación deseada de la imagen (admite entrada multilínea y prompts dinámicos) |
| `vae` | VAE | No | - | Modelo VAE opcional para generar latentes de referencia a partir de las imágenes de entrada |
| `imagen1` | IMAGE | No | - | Primera imagen de entrada opcional para análisis y modificación |
| `imagen2` | IMAGE | No | - | Segunda imagen de entrada opcional para análisis y modificación |
| `imagen3` | IMAGE | No | - | Tercera imagen de entrada opcional para análisis y modificación |

**Nota:** Cuando se proporciona un VAE, el nodo genera latentes de referencia a partir de todas las imágenes de entrada. El nodo puede procesar hasta tres imágenes simultáneamente. Las imágenes se redimensionan automáticamente a 384x384 píxeles para el procesamiento de visión-lenguaje, y a dimensiones divisibles por 8 (con un área objetivo de 1024x1024 píxeles) para la codificación VAE.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Datos de condicionamiento codificados que contienen tokens de texto y latentes de referencia opcionales para la generación de imágenes |

---
**Source fingerprint (SHA-256):** `54889d9a3b70e41d623020f3fd5e3c798c72799492c67a9efd99f543c88bb968`
