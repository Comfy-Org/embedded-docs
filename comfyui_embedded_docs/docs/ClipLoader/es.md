# Cargar CLIP

El nodo CLIPLoader carga un modelo de codificador de texto (CLIP, T5 o similar) desde un archivo, poniéndolo a disposición de otros nodos que necesitan convertir prompts de texto en representaciones numéricas. Es compatible con una amplia variedad de arquitecturas de modelos, cada una de las cuales requiere un tipo de codificador específico.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `clip_name` | El nombre del archivo del modelo de codificador de texto a cargar. Debe ser un archivo ubicado en el directorio `ComfyUI/models/text_encoders/`. | COMBO | Sí | Lista de archivos encontrados en la carpeta `text_encoders` |
| `type` | El tipo de arquitectura del modelo que se está cargando. Esto determina qué variante de codificador específica usar (por defecto: `"stable_diffusion"`). | COMBO | Sí | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"`<br>`"lens"`<br>`"pixeldit"`<br>`"ideogram4"`<br>`"boogu"`<br>`"krea2"`<br>`"joyimage"`<br>`"mage"`<br>`"minimax"` |
| `device` | El dispositivo en el que se cargará el modelo. `"default"` usa el dispositivo predeterminado (normalmente la GPU si está disponible), mientras que `"cpu"` fuerza la carga en la CPU. Esta es una opción avanzada (por defecto: `"default"`). | COMBO | No | `"default"`<br>`"cpu"` |

### Asignaciones de tipo a codificador compatibles

El parámetro `type` selecciona el codificador correcto para una arquitectura de modelo determinada. Las siguientes asignaciones comunes se enumeran en la descripción del nodo:

| Tipo | Codificador |
|------|-------------|
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
| `clip` | El modelo de codificador de texto cargado, listo para conectarse a otros nodos para la codificación de texto y el condicionamiento. | CLIP |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPLoader/es.md)

---
**Source fingerprint (SHA-256):** `7c1586d01410d319468f7c8c153ef0717280804add868ba57bff0c6539fb5dd9`
