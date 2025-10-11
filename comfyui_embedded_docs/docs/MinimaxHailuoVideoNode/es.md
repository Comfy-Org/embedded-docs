> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/es.md)

Genera videos a partir de textos descriptivos utilizando el modelo MiniMax Hailuo-02. Opcionalmente, puedes proporcionar una imagen inicial como primer fotograma para crear un video que continúe a partir de esa imagen.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt_text` | STRING | Sí | - | Texto descriptivo para guiar la generación del video. |
| `seed` | INT | No | 0 a 18446744073709551615 | La semilla aleatoria utilizada para crear el ruido (valor predeterminado: 0). |
| `first_frame_image` | IMAGE | No | - | Imagen opcional para usar como primer fotograma y generar un video. |
| `prompt_optimizer` | BOOLEAN | No | - | Optimiza el texto descriptivo para mejorar la calidad de generación cuando es necesario (valor predeterminado: True). |
| `duration` | COMBO | No | `6`<br>`10` | La duración del video de salida en segundos (valor predeterminado: 6). |
| `resolution` | COMBO | No | `"768P"`<br>`"1080P"` | Las dimensiones de visualización del video. 1080p es 1920x1080, 768p es 1366x768 (valor predeterminado: "768P"). |

**Nota:** Cuando se utiliza el modelo MiniMax-Hailuo-02 con resolución 1080P, la duración está limitada a 6 segundos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado. |