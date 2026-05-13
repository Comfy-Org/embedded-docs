> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3InfiniteStyleLibrary/es.md)

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

Este nodo te permite seleccionar un estilo de la Biblioteca Infinita de Estilos de Recraft utilizando un UUID preexistente. Recupera la información del estilo basándose en el identificador de estilo proporcionado y lo devuelve para usarlo en otros nodos de Recraft.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `style_id` | STRING | Sí | Cualquier UUID válido | UUID del estilo de la Biblioteca Infinita de Estilos. |

**Nota:** La entrada `style_id` no puede estar vacía. Si se proporciona una cadena vacía, el nodo generará una excepción.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `recraft_style` | STYLEV3 | El objeto de estilo seleccionado de la Biblioteca Infinita de Estilos de Recraft |

---
**Source fingerprint (SHA-256):** `37d7d9eff1232cc17912c6fca908dc5b8c404c0b6cf0a36e8fecc837ff2a1eea`
