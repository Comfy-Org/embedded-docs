# ClipLoader

El nodo CLIPLoader carga un modelo codificador de texto (CLIP, T5 o similar) desde un archivo, poniéndolo a disposición para su uso en otros nodos que necesitan convertir indicaciones de texto en representaciones numéricas. Admite una amplia variedad de arquitecturas de modelo, cada una de las cuales requiere un tipo de codificador específico.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `nombre_clip` | El nombre del archivo del modelo codificador de texto a cargar. Debe ser un archivo ubicado en el directorio `ComfyUI/models/text_encoders/`. | STRING | Sí | Lista de archivos encontrados en la carpeta `text_encoders` |
| `tipo` | El tipo de arquitectura del modelo que se está cargando. Esto determina qué variante de codificador específica se debe usar (predeterminado: `"stable_diffusion"`). | COMBO | Sí | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"`<br>`"lens"`<br>`"pixeldit"`<br>`"ideogram4"`<br>`"boogu"`<br>`"krea2"`<br>`"joyimage"`<br>`"mage"`<br>`"minimax"` |
| `dispositivo` | El dispositivo en el que cargar el modelo. `"default"` usa la GPU si está disponible, mientras que `"cpu"` fuerza la carga en CPU. Esta es una opción avanzada (predeterminado: `"default"`). | COMBO | No | `"default"`<br>`"cpu"` |

### Asignaciones de tipo a codificador compatibles

El parámetro `type` selecciona el codificador correcto para una arquitectura de modelo determinada. Las siguientes son asignaciones comunes:

| Tipo | Codificador |
|------|---------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl / clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cogvideox | t5 xxl (226-token padding) |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |
| hidream | llama-3.1 (recomendado) o t5 |
| omnigen2 | qwen vl 2.5 3B |
| joyimage | qwen3-vl 8B |
| lens | gpt-oss-20b |
| pixeldit | gemma 2 2B elm |
| minimax | MiniMax H3 Qwen3-VL o Music3 Qwen/RVQ |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `clip` | El modelo codificador de texto cargado, listo para conectarse a otros nodos para la codificación de texto y el condicionamiento. | CLIP |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipLoader/es.md)

---
**Source fingerprint (SHA-256):** `7c1586d01410d319468f7c8c153ef0717280804add868ba57bff0c6539fb5dd9`
