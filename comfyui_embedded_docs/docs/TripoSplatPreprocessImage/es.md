# TripoSplat Preprocesar Imagen

Este nodo recorta cada imagen de entrada a un cuadrado centrado sobre un fondo negro, luego agrega relleno para alcanzar el tamaño de salida especificado. Está diseñado para preparar imágenes para el modelo 3D TripoSplat, garantizando un encuadre cuadrado consistente y un erosionado opcional del matte alfa para evitar artefactos en los bordes.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `imagen` | La(s) imagen(es) de entrada a preprocesar | IMAGE | Sí | - |
| `mask` | Máscara alfa para la imagen, utilizada para determinar la región de recorte | MASK | Sí | - |
| `radio_de_erosión` | Erosiona el matte alfa en este radio de píxeles antes del recorte (evita sangrado de bordes). Valor predeterminado: 1 | INT | Sí | 0 a 16 |
| `tamaño` | Tamaño cuadrado de la imagen. El modelo está entrenado en 1024; otros tamaños funcionan pero están fuera de distribución. Valor predeterminado: 1024 | INT | Sí | 256 a 4096 (paso de 16) |

**Nota:** La entrada `mask` es requerida y debe proporcionarse. Si la máscara tiene un tamaño de lote diferente al de la imagen, se repite automáticamente para coincidir. Si las dimensiones de la máscara difieren de las dimensiones de la imagen, la máscara se redimensiona para coincidir con la imagen mediante interpolación bilineal.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|-----------|
| `imagen` | La(s) imagen(es) preprocesada(s) recortada(s) a un cuadrado centrado sobre fondo negro con relleno | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatPreprocessImage/es.md)

---
**Source fingerprint (SHA-256):** `3f33dbc3a99ccb23ede767915a28fabdfa388edb8d5782edea3f8d03e5965b2a`
