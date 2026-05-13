> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/es.md)

El nodo Topaz Video Enhance utiliza una API externa para mejorar la calidad del video. Puede aumentar la resolución del video, incrementar la tasa de fotogramas mediante interpolación y aplicar compresión. El nodo procesa un video MP4 de entrada y devuelve una versión mejorada según la configuración seleccionada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `video` | VIDEO | Sí | - | El archivo de video de entrada que se va a mejorar. |
| `upscaler_enabled` | BOOLEAN | Sí | - | Activa o desactiva la función de aumento de resolución del video (valor predeterminado: True). |
| `upscaler_model` | COMBO | Sí | `"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"` | El modelo de IA utilizado para aumentar la resolución del video. |
| `upscaler_resolution` | COMBO | Sí | `"FullHD (1080p)"`<br>`"4K (2160p)"` | La resolución objetivo para el video con resolución aumentada. |
| `upscaler_creativity` | COMBO | No | `"bajo"`<br>`"medio"`<br>`"alto"` | Nivel de creatividad (solo aplica a Starlight (Astra) Creative). (valor predeterminado: "bajo") |
| `interpolation_enabled` | BOOLEAN | No | - | Activa o desactiva la función de interpolación de fotogramas (valor predeterminado: False). |
| `interpolation_model` | COMBO | No | `"apo-8"` | El modelo utilizado para la interpolación de fotogramas (valor predeterminado: "apo-8"). |
| `interpolation_slowmo` | INT | No | 1 a 16 | Factor de cámara lenta aplicado al video de entrada. Por ejemplo, 2 hace que la salida sea el doble de lenta y duplica la duración. (valor predeterminado: 1) |
| `interpolation_frame_rate` | INT | No | 15 a 240 | Tasa de fotogramas de salida. (valor predeterminado: 60) |
| `interpolation_duplicate` | BOOLEAN | No | - | Analiza la entrada en busca de fotogramas duplicados y los elimina. (valor predeterminado: False) |
| `interpolation_duplicate_threshold` | FLOAT | No | 0.001 a 0.1 | Sensibilidad de detección para fotogramas duplicados. (valor predeterminado: 0.01) |
| `dynamic_compression_level` | COMBO | No | `"Bajo"`<br>`"Medio"`<br>`"Alto"` | Nivel CQP. (valor predeterminado: "Bajo") |

**Nota:** Al menos una función de mejora debe estar activada. El nodo generará un error si tanto `upscaler_enabled` como `interpolation_enabled` están configurados como `False`. El video de entrada debe estar en formato MP4.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `video` | VIDEO | El archivo de video de salida mejorado. |

---
**Source fingerprint (SHA-256):** `70e1a6e0d7bd250f58c43beefe070fd83af19d11ac08cb9a6ac9655a9bfa839f`
