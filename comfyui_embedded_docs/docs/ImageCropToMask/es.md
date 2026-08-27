# ImageCropToMask

Recorta una imagen al cuadro delimitador de su máscara, produciendo un sujeto centrado sobre un color de fondo sólido. El nodo compone la imagen enmascarada sobre el fondo elegido y redimensiona el resultado a las dimensiones de salida especificadas, lo que lo hace adecuado para pipelines 3D que esperan un sujeto centrado, sin fondo y a una resolución fija.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `images` | La imagen de entrada o lote de imágenes a recortar. | IMAGE | Sí | — |
| `masks` | La máscara o lote de máscaras que define el área del sujeto. Una máscara única se aplica a todas las imágenes; de lo contrario, el tamaño del lote de máscaras debe coincidir con el tamaño del lote de imágenes. Si la resolución de la máscara difiere de la resolución de la imagen, la máscara se redimensiona automáticamente para coincidir. | MASK | Sí | — |
| `width` | Ancho de salida en píxeles. (por defecto: 1024) | INT | Sí | 64 to 4096 (step 8) |
| `height` | Alto de salida en píxeles. (por defecto: 1024) | INT | Sí | 64 to 4096 (step 8) |
| `pad_factor` | Margen adicional alrededor del cuadro delimitador de la máscara como multiplicador. (por defecto: 1.0) | FLOAT | Sí | 1.0 to 2.0 (step 0.01) |
| `grow_mask` | Expandir o contraer la máscara en esta cantidad de píxeles antes de recortar. Los valores positivos expanden la máscara, los negativos la contraen. (por defecto: 0) | INT | Sí | -32 to 32 (step 1) |
| `background` | Color de fondo detrás del sujeto enmascarado. (por defecto: #000000) | COLOR | Sí | — |

Nota: La región de recorte está centrada en el cuadro delimitador de la máscara y su relación de aspecto coincide con `width` / `height`. El nodo detecta y corrige automáticamente una máscara invertida (píxeles de primer plano a lo largo del borde, fondo en el centro). Si la máscara no contiene píxeles de primer plano, el nodo intenta con la máscara invertida; si esta también está vacía, registra una advertencia y recorta la imagen completa. Se produce un error cuando el tamaño del lote de máscaras no coincide con el tamaño del lote de imágenes y no es una máscara única.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `images` | Las imágenes compuestas recortadas (sujeto enmascarado sobre el color de fondo elegido), redimensionadas a `width` x `height`. El tamaño del lote coincide con el lote de imágenes de entrada. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropToMask/es.md)

---
**Source fingerprint (SHA-256):** `fcc14b5db7318699526dd544d404f78f9d1ab362b73769276f113f2b1062b214`
