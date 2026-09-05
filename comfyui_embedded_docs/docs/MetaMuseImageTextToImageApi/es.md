# MetaMuseImageTextToImageApi

Meta Muse Image Text to Image genera imágenes a partir de un prompt de texto utilizando el modelo Muse Image de Meta. El modelo razona sobre el prompt antes del renderizado y puede utilizar la búsqueda web, la búsqueda de imágenes y la ejecución de código mientras planifica la imagen. El nodo llama a la API de Muse Image y devuelve la imagen o las imágenes resultantes.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | Modelo que se va a utilizar. | DYNAMIC_COMBO | Sí | `"muse-image-1.0"` |

Al seleccionar un modelo en la lista se muestran los ajustes que ofrece. El único modelo disponible es `muse-image-1.0`; sus ajustes se enumeran a continuación.

### Entradas de muse-image-1.0

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Prompt que describe la imagen. El modelo razona sobre el prompt y puede usar su búsqueda web y de imágenes integrada antes del renderizado. | STRING | Sí | Texto multilínea, mínimo 1 carácter |
| `aspect_ratio` | Relación de aspecto de la imagen de salida. Las imágenes se renderizan a aproximadamente 2.5 megapíxeles (1:1 corresponde a 1600x1600 y 16:9 a 2048x1152); "auto" permite que el modelo elija a partir del prompt. | COMBO | Sí | `"auto"`<br>`"1:1"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"5:4"`<br>`"4:5"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"`<br>`"9:21"`<br>`"2:1"`<br>`"1:2"` |
| `reasoning_strength` | Grado en que el modelo piensa, planifica y refina sus resultados antes del renderizado. | COMBO | Sí | `"high"`<br>`"low"` |
| `enable_web_search` | Permite que el modelo busque en la web datos e información actualizada mientras planifica la imagen. | BOOLEAN | No | True<br>False (por defecto: True) |
| `enable_image_search` | Permite que el modelo busque imágenes de referencia mientras planifica la imagen. | BOOLEAN | No | True<br>False (por defecto: True) |
| `enable_shell` | Permite que el modelo ejecute código mientras planifica para lograr composiciones, gráficos y diagramas precisos; cuando está desactivado, las cantidades y la alineación se aproximan. | BOOLEAN | No | True<br>False (por defecto: True) |
| `seed` | Semilla que determina si el nodo debe volver a ejecutarse; la API no utiliza semilla, por lo que los resultados reales son no deterministas independientemente de este valor. | INT | Sí | 0 – 2147483647 (por defecto: 42) |

Nota: El prompt debe contener al menos un carácter. Cuando `aspect_ratio` se define como "auto", no se envía ningún tamaño explícito a la API y el modelo decide el tamaño de salida a partir del prompt. El parámetro `seed` solo controla cuándo se vuelve a ejecutar el nodo; no se envía a la API, por lo que los resultados generados son no deterministas.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La imagen generada devuelta por la API, decodificada y proporcionada como una imagen en lote. Si la respuesta de la API contiene varias imágenes, se combinan en un solo lote. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MetaMuseImageTextToImageApi/es.md)

---
**Source fingerprint (SHA-256):** `59ebd72fab3db44a35ceac723606de4eabb5fe2b690d0b701db50e0e22a9e699`
