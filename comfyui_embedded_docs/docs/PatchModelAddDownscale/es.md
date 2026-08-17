# PatchModelAddDownscale (Kohya Deep Shrink)

El nodo `PatchModelAddDownscale` implementa la funcionalidad Kohya Deep Shrink al aplicar operaciones de reducción y ampliación de escala a bloques específicos de un modelo. Reduce la resolución de las características intermedias durante el procesamiento y luego las restaura a su tamaño original, lo que puede mejorar el rendimiento mientras se mantiene la calidad. El nodo permite un control preciso sobre cuándo y cómo ocurren estas operaciones de escala durante la ejecución del modelo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo al que se aplica el parche de reducción de escala | MODEL | Sí | - |
| `block_number` | El número de bloque específico donde se aplicará la reducción de escala (por defecto: 3) | INT | No | 1-32 |
| `downscale_factor` | El factor por el cual se reducirá la escala de las características (por defecto: 2.0) | FLOAT | No | 0.1-9.0 |
| `start_percent` | El punto inicial en el proceso de denoising donde comienza la reducción de escala (por defecto: 0.0) | FLOAT | No | 0.0-1.0 |
| `end_percent` | El punto final en el proceso de denoising donde se detiene la reducción de escala (por defecto: 0.35) | FLOAT | No | 0.0-1.0 |
| `downscale_after_skip` | Si se aplica la reducción de escala después de las conexiones de salto (por defecto: True) | BOOLEAN | No | - |
| `downscale_method` | El método de interpolación utilizado para las operaciones de reducción de escala | COMBO | No | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |
| `upscale_method` | El método de interpolación utilizado para las operaciones de ampliación de escala | COMBO | No | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo modificado con el parche de reducción de escala aplicado | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/es.md)

---
**Source fingerprint (SHA-256):** `aa9434a521ab585b290a3bd8db804469bd3bb02103a0d830b6be6eb8e8c26a5e`
