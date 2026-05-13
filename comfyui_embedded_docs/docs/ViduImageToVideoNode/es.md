> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduImageToVideoNode/es.md)

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

El nodo de Generación de Video a partir de Imagen de Vidu crea un video corto a partir de una imagen inicial y una descripción textual opcional. Utiliza un modelo de IA para generar contenido de video que continúa a partir del fotograma de imagen proporcionado, y devuelve el video resultante.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `model` | COMBO | Sí | `viduq1` | Nombre del modelo (predeterminado: viduq1) |
| `image` | IMAGE | Sí | - | Una imagen que se usará como fotograma inicial del video generado |
| `prompt` | STRING | No | - | Una descripción textual para la generación del video (predeterminado: vacío) |
| `duration` | INT | No | 5-5 | Duración del video de salida en segundos (predeterminado: 5, fijo en 5 segundos) |
| `seed` | INT | No | 0-2147483647 | Semilla para la generación del video (0 para aleatorio) (predeterminado: 0) |
| `resolution` | COMBO | No | `1080p` | Los valores admitidos pueden variar según el modelo y la duración (predeterminado: 1080p) |
| `movement_amplitude` | COMBO | No | `auto`<br>`small`<br>`medium`<br>`large` | La amplitud de movimiento de los objetos en el fotograma (predeterminado: auto) |

**Restricciones:**

- Solo se permite una imagen de entrada (no puede procesar múltiples imágenes).
- La imagen de entrada debe tener una relación de aspecto entre 1:4 y 4:1.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | La salida de video generada |

---
**Source fingerprint (SHA-256):** `064b3efba8219770595e68a6607a6f8113d1be7c9f3863a4740ee5c3a146d91e`
