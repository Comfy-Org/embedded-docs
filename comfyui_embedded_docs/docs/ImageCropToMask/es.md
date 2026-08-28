# ImageCropToMask

Recorta una imagen al cuadro delimitador de su máscara, produciendo un sujeto centrado sobre un color de fondo sólido. El nodo compone la imagen enmascarada sobre el fondo elegido y redimensiona el resultado a las dimensiones de salida especificadas, lo que lo hace adecuado para flujos de trabajo 3D que esperan un sujeto centrado, sin fondo y a una resolución fija.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `imágenes` | La imagen de entrada o lote de imágenes que se va a recortar. | IMAGE | Sí | — |
| `máscaras` | La máscara o lote de máscaras que define el área del sujeto. Se aplica una sola máscara a todas las imágenes; de lo contrario, el tamaño del lote de máscaras debe coincidir con el tamaño del lote de imágenes. Si la resolución de la máscara difiere de la resolución de la imagen, la máscara se redimensiona automáticamente para que coincida. | MASK | Sí | — |
| `ancho` | Ancho de salida en píxeles. (por defecto: 1024) | INT | Sí | 64 a 4096 (paso 8) |
| `alto` | Alto de salida en píxeles. (por defecto: 1024) | INT | Sí | 64 a 4096 (paso 8) |
| `pad_factor` | Margen adicional alrededor del cuadro delimitador de la máscara como multiplicador. (por defecto: 1.0) | FLOAT | Sí | 1.0 a 2.0 (paso 0.01) |
| `grow_mask` | Aumenta o reduce la máscara esta cantidad de píxeles antes de recortar. Los valores positivos expanden la máscara; los negativos la encogen. (por defecto: 0) | INT | Sí | -32 a 32 (paso 1) |
| `fondo` | Color de fondo detrás del sujeto enmascarado. (por defecto: #000000) | COLOR | Sí | — |

Nota: La región de recorte está centrada en el cuadro delimitador de la máscara y su relación de aspecto coincide con `width` / `height`. El nodo detecta y corrige automáticamente una máscara invertida (píxeles de primer plano en el borde y fondo en el centro). Si la máscara no contiene píxeles de primer plano, el nodo prueba con la máscara invertida; si esta también está vacía, registra una advertencia y recorta la imagen completa. Se produce un error cuando el tamaño del lote de máscaras no coincide con el tamaño del lote de imágenes y no es una máscara única.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `imágenes` | Las imágenes compuestas recortadas (sujeto enmascarado sobre el color de fondo elegido), redimensionadas a `width` x `height`. El tamaño del lote coincide con el lote de imágenes de entrada. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropToMask/es.md)

---
**Source fingerprint (SHA-256):** `fcc14b5db7318699526dd544d404f78f9d1ab362b73769276f113f2b1062b214`
