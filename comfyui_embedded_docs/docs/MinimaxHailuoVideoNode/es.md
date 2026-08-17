# MiniMax Hailuo Video

Genera videos a partir de prompts de texto utilizando el modelo MiniMax Hailuo-02. Opcionalmente, puedes proporcionar una imagen inicial como primer fotograma para crear un video que continúe a partir de esa imagen.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt_text` | Prompt de texto para guiar la generación del video. | STRING | Sí | - |
| `seed` | La semilla aleatoria utilizada para crear el ruido (por defecto: 0). | INT | No | 0 a 18446744073709551615 |
| `first_frame_image` | Imagen opcional para usar como primer fotograma para generar un video. | IMAGE | No | - |
| `prompt_optimizer` | Optimiza el prompt para mejorar la calidad de generación cuando sea necesario (por defecto: True). | BOOLEAN | No | - |
| `duration` | La duración del video de salida en segundos (por defecto: 6). | COMBO | No | `6`<br>`10` |
| `resolution` | Las dimensiones de la visualización del video. 1080p es 1920x1080, 768p es 1366x768 (por defecto: "768P"). | COMBO | No | `"768P"`<br>`"1080P"` |

**Notas:**
- `prompt_text` debe ser una cadena no vacía cuando no se proporcione `first_frame_image`.
- Al usar el modelo MiniMax-Hailuo-02 con resolución 1080P, la duración se limita a 6 segundos.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `f371aae15cfbe7353236bc679c8a6d558703c5037e49ab7ddb9bdf5c50ef0995`
