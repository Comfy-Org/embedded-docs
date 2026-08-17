# TripoSplat Preprocesar Imagen

Este nodo recorta cada imagen de entrada a un cuadrado centrado sobre un fondo negro y luego añade relleno para alcanzar el tamaño de salida especificado. Está diseñado para preparar imágenes para el modelo 3D TripoSplat, asegurando un encuadre cuadrado consistente y una erosión opcional de la máscara alfa para evitar artefactos en los bordes.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `image` | La(s) imagen(es) de entrada a preprocesar | IMAGE | Sí | - |
| `mask` | Máscara alfa para la imagen, utilizada para determinar la región de recorte | MASK | Sí | - |
| `erode_radius` | Erosiona la máscara alfa en este radio de píxeles antes del recorte (evita el sangrado de bordes). Valor predeterminado: 1 | INT | Sí | 0 to 16 |
| `size` | Tamaño de imagen cuadrada. El modelo se entrena a 1024; otros tamaños funcionan pero quedan fuera de la distribución. Valor predeterminado: 1024 | INT | Sí | 256 to 4096 (step of 16) |

**Nota:** El parámetro `mask` es obligatorio y debe proporcionarse. Si la máscara tiene un tamaño de lote diferente al de la imagen, se repite automáticamente para coincidir. Si las dimensiones de la máscara difieren de las de la imagen, la máscara se redimensiona para coincidir con la imagen mediante interpolación bilineal. El tamaño de salida se redondea automáticamente al múltiplo de 16 más cercano para garantizar la compatibilidad con los requisitos de parche de DINOv3 y de stride del VAE de Flux2. Se genera un error si la máscara no contiene píxeles en primer plano.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La(s) imagen(es) preprocesada(s) recortada(s) a un cuadrado centrado sobre un fondo negro con relleno | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatPreprocessImage/es.md)

---
**Source fingerprint (SHA-256):** `ec66941846398ee6637576b11ae9d2f9576f6b05ed2ef730cdbf99a68fe9b838`
