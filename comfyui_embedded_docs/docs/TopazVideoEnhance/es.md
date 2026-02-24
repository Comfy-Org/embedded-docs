> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/es.md)

El nodo Topaz Video Enhance utiliza una API externa para mejorar la calidad del video. Puede aumentar la resolución del video, incrementar la tasa de cuadros mediante interpolación y aplicar compresión. El nodo procesa un video MP4 de entrada y devuelve una versión mejorada basada en la configuración seleccionada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Sí | - | El archivo de video de entrada que se va a mejorar. |
| `upscaler_enabled` | BOOLEAN | Sí | - | Habilita o deshabilita la función de aumento de resolución del video (valor por defecto: True). |
| `upscaler_model` | COMBO | Sí | `"Proteus v3"`<br>`"Artemis v13"`<br>`"Artemis v14"`<br>`"Artemis v15"`<br>`"Gaia v6"`<br>`"Theia v3"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight (Astra) Optimized"`<br>`"Starlight (Astra) Balanced"`<br>`"Starlight (Astra) Quality"`<br>`"Starlight (Astra) Speed"` | El modelo de IA utilizado para aumentar la resolución del video. |
| `upscaler_resolution` | COMBO | Sí | `"FullHD (1080p)"`<br>`"4K (2160p)"` | La resolución objetivo para el video con aumento de resolución. |
| `upscaler_creativity` | COMBO | No | `"low"`<br>`"middle"`<br>`"high"` | Nivel de creatividad (solo se aplica a Starlight (Astra) Creative). (valor por defecto: "low") |
| `interpolation_enabled` | BOOLEAN | No | - | Habilita o deshabilita la función de interpolación de cuadros (valor por defecto: False). |
| `interpolation_model` | COMBO | No | `"apo-8"` | El modelo utilizado para la interpolación de cuadros (valor por defecto: "apo-8"). |
| `interpolation_slowmo` | INT | No | 1 a 16 | Factor de cámara lenta aplicado al video de entrada. Por ejemplo, 2 hace que la salida sea el doble de lenta y duplica la duración. (valor por defecto: 1) |
| `interpolation_frame_rate` | INT | No | 15 a 240 | Tasa de cuadros de salida. (valor por defecto: 60) |
| `interpolation_duplicate` | BOOLEAN | No | - | Analiza la entrada en busca de cuadros duplicados y los elimina. (valor por defecto: False) |
| `interpolation_duplicate_threshold` | FLOAT | No | 0.001 a 0.1 | Sensibilidad de detección para cuadros duplicados. (valor por defecto: 0.01) |
| `dynamic_compression_level` | COMBO | No | `"Low"`<br>`"Mid"`<br>`"High"` | Nivel CQP. (valor por defecto: "Low") |

**Nota:** Debe estar habilitada al menos una función de mejora. El nodo generará un error si tanto `upscaler_enabled` como `interpolation_enabled` están configurados en `False`. El video de entrada debe estar en formato MP4.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `video` | VIDEO | El archivo de video mejorado de salida. |
