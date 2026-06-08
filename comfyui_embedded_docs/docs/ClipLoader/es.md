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

El nodo CLIPLoader carga un modelo codificador de texto (CLIP, T5 o similar) desde un archivo, poniéndolo a disposición para su uso en otros nodos que necesitan convertir indicaciones de texto en representaciones numéricas. Soporta una amplia variedad de arquitecturas de modelos, cada una requiriendo un tipo de codificador específico.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `nombre_clip` | El nombre del archivo del modelo codificador de texto a cargar. Este debe ser un archivo ubicado en el directorio `ComfyUI/models/text_encoders/` o `ComfyUI/models/clip/`. | STRING | Sí | Lista de archivos encontrados en la carpeta `text_encoders` |
| `tipo` | El tipo de arquitectura del modelo que se está cargando. Esto determina qué variante de codificador específica usar. El valor predeterminado es `"stable_diffusion"`. | STRING | Sí | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"` |
| `dispositivo` | El dispositivo en el que cargar el modelo. `"default"` usa la GPU si está disponible, mientras que `"cpu"` fuerza la carga en CPU. Esta es una opción avanzada (predeterminado: `"default"`). | STRING | No | `"default"`<br>`"cpu"` |

### Mapeos Compatibles de Tipo a Codificador

El parámetro `type` selecciona el codificador correcto para una arquitectura de modelo determinada. Los siguientes son mapeos comunes:

| Tipo | Codificador |
|------|---------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl / clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cogvideox | t5 xxl (relleno de 226 tokens) |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |
| hidream | llama-3.1 (recomendado) o t5 |
| omnigen2 | qwen vl 2.5 3B |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `clip` | El modelo codificador de texto cargado, listo para ser conectado a otros nodos para codificación de texto y acondicionamiento. | CLIP |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPLoader/es.md)

---
**Source fingerprint (SHA-256):** `1051bfe5570dff81719682cb09938bae4c03e94e0e72f7a2be84867cccb48017`
