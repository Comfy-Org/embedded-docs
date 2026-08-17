# StableZero123_Conditioning_Batched

El nodo StableZero123_Conditioning_Batched prepara los datos de condicionamiento necesarios para generar vistas 3D de un objeto con el modelo Stable Zero123. Codifica una imagen de entrada con un modelo de visión CLIP y un VAE, combina las características de la imagen con los ángulos de elevación y acimut de la cámara para cada elemento de un lote, y genera el condicionamiento positivo y negativo junto con un latente vacío. Las entradas de incremento de lote aumentan o disminuyen el ángulo de cámara para cada elemento consecutivo del lote.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `clip_vision` | El modelo de visión CLIP utilizado para codificar la imagen de entrada en incrustaciones de imagen | CLIP_VISION | Sí | - |
| `init_image` | La imagen de entrada inicial que se procesará y codificará | IMAGE | Sí | - |
| `vae` | El modelo VAE utilizado para codificar los píxeles de la imagen en el espacio latente | VAE | Sí | - |
| `width` | Ancho objetivo de la imagen procesada (por defecto: 256) | INT | Sí | 16 a MAX_RESOLUTION (paso 8) |
| `height` | Alto objetivo de la imagen procesada (por defecto: 256) | INT | Sí | 16 a MAX_RESOLUTION (paso 8) |
| `batch_size` | Número de muestras de condicionamiento que se generarán en el lote (por defecto: 1) | INT | Sí | 1 a 4096 |
| `elevation` | Ángulo de elevación inicial de la cámara en grados (por defecto: 0.0) | FLOAT | Sí | -180.0 a 180.0 (paso 0.1) |
| `azimuth` | Ángulo de acimut inicial de la cámara en grados (por defecto: 0.0) | FLOAT | Sí | -180.0 a 180.0 (paso 0.1) |
| `elevation_batch_increment` | Cantidad que se añade al ángulo de elevación para cada elemento consecutivo del lote (por defecto: 0.0, parámetro avanzado) | FLOAT | Sí | -180.0 a 180.0 (paso 0.1) |
| `azimuth_batch_increment` | Cantidad que se añade al ángulo de acimut para cada elemento consecutivo del lote (por defecto: 0.0, parámetro avanzado) | FLOAT | Sí | -180.0 a 180.0 (paso 0.1) |

**Nota:** Los valores de `width` y `height` deben ser múltiplos de 8 (el paso de selección de 8 lo garantiza) porque el nodo los divide entre 8 para construir las dimensiones del latente. Para cada elemento del lote, los valores de `elevation` y `azimuth` se incrementan en `elevation_batch_increment` y `azimuth_batch_increment`, de modo que los elementos consecutivos del lote reciben ángulos de cámara paso a paso.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `positive` | Condicionamiento positivo que combina las incrustaciones de imagen, las incrustaciones de cámara y la imagen de entrada codificada para la concatenación durante la generación | CONDITIONING |
| `negative` | Condicionamiento negativo que utiliza incrustaciones de imagen inicializadas a cero y un latente cero para la concatenación | CONDITIONING |
| `latent` | Tensor latente vacío con dimensiones (batch_size, 4, height/8, width/8) e información del índice del lote | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/es.md)

---
**Source fingerprint (SHA-256):** `94fc53dace8f294a746c47f8aa0da145f3e7beeb77a95912a38f0037ac094292`
