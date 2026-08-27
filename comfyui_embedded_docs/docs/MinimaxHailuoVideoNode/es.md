# MiniMax Hailuo Video

Genera videos a partir de indicaciones de texto utilizando el modelo MiniMax Hailuo-02. Opcionalmente, puedes proporcionar una imagen inicial como primer fotograma para crear un video que continúe desde esa imagen.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `texto_del_prompt` | Indicación de texto para guiar la generación del video. | STRING | Sí | - |
| `semilla` | La semilla aleatoria utilizada para crear el ruido (predeterminado: 0). | INT | No | 0 a 18446744073709551615 |
| `imagen_primer_fotograma` | Imagen opcional para usar como primer fotograma para generar un video. | IMAGE | No | - |
| `optimizador_de_prompt` | Optimizar la indicación para mejorar la calidad de generación cuando sea necesario (predeterminado: True). | BOOLEAN | No | True<br>False |
| `duración` | La duración del video de salida en segundos (predeterminado: 6). | COMBO | No | 6<br>10 |
| `resolución` | Las dimensiones de la pantalla del video. 1080p es 1920x1080, 768p es 1366x768 (predeterminado: "768P"). | COMBO | No | "768P"<br>"1080P" |

**Nota:** Cuando `resolution` está configurado en "1080P", `duration` se limita a 6 segundos. Cuando no se proporciona `first_frame_image`, `prompt_text` no debe estar vacío.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `f371aae15cfbe7353236bc679c8a6d558703c5037e49ab7ddb9bdf5c50ef0995`
