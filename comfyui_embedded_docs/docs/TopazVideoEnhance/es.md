# Topaz Video Enhance

El nodo Topaz Video Enhance utiliza una API externa para mejorar la calidad del video. Puede aumentar la resolución del video, incrementar la tasa de fotogramas mediante interpolación y aplicar compresión. El nodo procesa un video MP4 de entrada y devuelve una versión mejorada según la configuración seleccionada.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `video` | El archivo de video de entrada que se va a mejorar. | VIDEO | Sí | - |
| `upscaler_enabled` | Activa o desactiva la función de aumento de resolución del video (valor predeterminado: True). | BOOLEAN | Sí | - |
| `upscaler_model` | El modelo de IA utilizado para aumentar la resolución del video. | COMBO | Sí | `"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"` |
| `upscaler_resolution` | La resolución objetivo para el video con resolución aumentada. | COMBO | Sí | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_creativity` | Nivel de creatividad (solo aplica a Starlight (Astra) Creative). (valor predeterminado: "bajo") | COMBO | No | `"bajo"`<br>`"medio"`<br>`"alto"` |
| `interpolation_enabled` | Activa o desactiva la función de interpolación de fotogramas (valor predeterminado: False). | BOOLEAN | No | - |
| `interpolation_model` | El modelo utilizado para la interpolación de fotogramas (valor predeterminado: "apo-8"). | COMBO | No | `"apo-8"` |
| `interpolation_slowmo` | Factor de cámara lenta aplicado al video de entrada. Por ejemplo, 2 hace que la salida sea el doble de lenta y duplica la duración. (valor predeterminado: 1) | INT | No | 1 a 16 |
| `interpolation_frame_rate` | Tasa de fotogramas de salida. (valor predeterminado: 60) | INT | No | 15 a 240 |
| `interpolation_duplicate` | Analiza la entrada en busca de fotogramas duplicados y los elimina. (valor predeterminado: False) | BOOLEAN | No | - |
| `interpolation_duplicate_threshold` | Sensibilidad de detección para fotogramas duplicados. (valor predeterminado: 0.01) | FLOAT | No | 0.001 a 0.1 |
| `dynamic_compression_level` | Nivel CQP. (valor predeterminado: "Bajo") | COMBO | No | `"Bajo"`<br>`"Medio"`<br>`"Alto"` |

**Nota:** Al menos una función de mejora debe estar activada. El nodo generará un error si tanto `upscaler_enabled` como `interpolation_enabled` están configurados como `False`. El video de entrada debe estar en formato MP4.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `video` | El archivo de video de salida mejorado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/es.md)

---
**Source fingerprint (SHA-256):** `70e1a6e0d7bd250f58c43beefe070fd83af19d11ac08cb9a6ac9655a9bfa839f`
