El Nodo de Referencia de Imagen ByteDance genera un video utilizando un texto de descripción y de una a cuatro imágenes de referencia. Envía las imágenes y el texto a un servicio API externo que crea un video que coincide con tu descripción, incorporando al mismo tiempo el estilo visual y el contenido de tus imágenes de referencia. El nodo proporciona varios controles para la resolución del video, la relación de aspecto, la duración y otros parámetros de generación.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de IA a utilizar para la generación de video (predeterminado: `"seedance-1-0-lite-i2v-250428"`). | STRING | Sí | `"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-i2v-250428"` |
| `prompt` | El texto de descripción utilizado para generar el video. | STRING | Sí | - |
| `imágenes` | De una a cuatro imágenes. Cada imagen debe tener entre 300x300 y 6000x6000 píxeles, con una relación de aspecto entre 0.4 y 2.5. | IMAGE | Sí | - |
| `resolución` | La resolución del video de salida. | STRING | Sí | `"480p"`<br>`"720p"` |
| `relación_de_aspecto` | La relación de aspecto del video de salida (predeterminado: `"adaptive"`). | STRING | Sí | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duración` | La duración del video de salida en segundos (predeterminado: 5). | INT | Sí | 3 - 12 |
| `semilla` | Semilla a utilizar para la generación (predeterminado: 0). | INT | No | 0 - 2147483647 |
| `marca_de_agua` | Si se debe agregar una marca de agua "generado por IA" al video (predeterminado: Falso). | BOOLEAN | No | - |

**Nota:** El texto de descripción no debe contener las siguientes cadenas de parámetros: `--resolution`, `--ratio`, `--duration`, `--seed` o `--watermark`. Estos valores se controlan exclusivamente a través de sus widgets de entrada dedicados.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El archivo de video generado basado en el texto de descripción de entrada y las imágenes de referencia. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageReferenceNode/es.md)

---
**Source fingerprint (SHA-256):** `d5d1292d6af2fe24dc5c8a10174204546a5a6054ea1f43db44a45ce1017957d6`
