> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageModifyNode/es.md)

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

Modifica imágenes de forma síncrona basándose en un prompt de texto y la relación de aspecto de la imagen original. Este nodo toma una imagen de entrada y la transforma de acuerdo con el prompt proporcionado, utilizando un peso de imagen configurable para controlar cuánto se altera la imagen original.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `imagen` | IMAGE | Sí | - | La imagen de entrada que se va a modificar |
| `prompt` | STRING | Sí | - | Prompt para la generación de la imagen (predeterminado: "") |
| `peso_imagen` | FLOAT | No | 0.0-0.98 | Peso de la imagen; cuanto más cercano a 1.0, menos se modificará la imagen (predeterminado: 0.1). Internamente, este valor se invierte (1.0 - image_weight) y se limita entre 0.0 y 0.98. |
| `modelo` | STRING | Sí | `"photon-flash-1"`<br>`"photon-1"`<br>`"photon"` | El modelo Luma a utilizar para la modificación de la imagen. Diferentes modelos tienen diferentes costos. |
| `semilla` | INT | No | 0-18446744073709551615 | Semilla para determinar si el nodo debe re-ejecutarse; los resultados reales son no deterministas independientemente de la semilla (predeterminado: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `imagen` | IMAGE | La imagen modificada generada por el modelo Luma |

---
**Source fingerprint (SHA-256):** `078542bdba19945037c95fefa30d1b403ebf58e29270c8067dcb8ff21a99b7e0`
