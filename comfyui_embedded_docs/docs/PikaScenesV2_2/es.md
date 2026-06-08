El nodo PikaScenes v2.2 combina múltiples imágenes para crear un video que incorpora objetos de todas las imágenes de entrada. Puedes cargar hasta cinco imágenes diferentes como ingredientes y generar un video de alta calidad que las fusione de manera uniforme.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt_text` | Descripción textual de lo que se desea generar | STRING | Sí | - |
| `negative_prompt` | Descripción textual de lo que se debe evitar en la generación | STRING | Sí | - |
| `seed` | Valor de semilla aleatoria para la generación | INT | Sí | - |
| `resolution` | Resolución de salida del video | STRING | Sí | - |
| `duration` | Duración del video generado | INT | Sí | - |
| `ingredients_mode` | Modo para combinar ingredientes (predeterminado: "creative") | STRING | No | "creative"<br>"precise" |
| `aspect_ratio` | Relación de aspecto (ancho / alto) (predeterminado: 1.778) | FLOAT | No | 0.4 - 2.5 |
| `image_ingredient_1` | Imagen que se usará como ingrediente para crear un video | IMAGE | No | - |
| `image_ingredient_2` | Imagen que se usará como ingrediente para crear un video | IMAGE | No | - |
| `image_ingredient_3` | Imagen que se usará como ingrediente para crear un video | IMAGE | No | - |
| `image_ingredient_4` | Imagen que se usará como ingrediente para crear un video | IMAGE | No | - |
| `image_ingredient_5` | Imagen que se usará como ingrediente para crear un video | IMAGE | No | - |

**Nota:** Puedes proporcionar hasta 5 ingredientes de imagen, pero se requiere al menos una imagen para generar un video. El nodo utilizará todas las imágenes proporcionadas para crear la composición final del video.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El video generado que combina todas las imágenes de entrada | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaScenesV2_2/es.md)

---
**Source fingerprint (SHA-256):** `dda8f10a58527c2b9037744f59f30821cdde37ad23427b856ba5e699a05acafd`
