# PixVerse Texto a Video

Genera videos basándose en un prompt de texto y varios parámetros de generación. Este nodo crea contenido de video utilizando la API de PixVerse, permitiendo controlar la relación de aspecto, la calidad, la duración, el estilo de movimiento y más.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `prompt` | Prompt para la generación de video (por defecto: "") | STRING | Sí | - |
| `relación_de_aspecto` | Relación de aspecto para el video generado | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `calidad` | Configuración de calidad de video (por defecto: "540p") | COMBO | Sí | `"540p"`<br>`"1080p"` |
| `duración_segundos` | Duración del video generado en segundos | COMBO | Sí | `"5"`<br>`"10"` |
| `modo_de_movimiento` | Estilo de movimiento para la generación de video | COMBO | Sí | `"normal"`<br>`"fast"` |
| `semilla` | Semilla para la generación de video (por defecto: 0) | INT | Sí | 0 a 2147483647 |
| `prompt_negativo` | Una descripción de texto opcional de elementos no deseados en una imagen (por defecto: "") | STRING | No | - |
| `plantilla_pixverse` | Una plantilla opcional para influir en el estilo de generación, creada por el nodo PixVerse Template | CUSTOM | No | - |

**Nota:** El `prompt` debe contener al menos 1 carácter. Al usar calidad 1080p, el modo de movimiento se establece automáticamente en `normal` y la duración se limita a 5 segundos. Para duraciones distintas de 5 segundos, el modo de movimiento también se establece automáticamente en `normal`.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `output` | El archivo de video generado | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `cb95579dc6c9afa17455b0216ec46571ad2c0455606cf3b9c725ca512c45f938`
