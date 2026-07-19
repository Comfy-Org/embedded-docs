# Topaz Video Enhance

El nodo **Topaz Video Enhance V2** permite mejorar la resolución y calidad de videos utilizando los modelos de IA de Topaz Labs. Puede aumentar la resolución, ajustar la frecuencia de cuadros mediante interpolación y aplicar mejoras creativas o realistas para dar nueva vida a tus secuencias de video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `video` | El video de entrada a procesar. Debe estar en formato contenedor MP4. | VIDEO | Sí | - |
| `upscaler_model` | El modelo de IA utilizado para mejorar la resolución del video. Seleccionar "Disabled" significa que no se aplicará mejora de resolución. | COMBO | Sí | `"Astra 2"`<br>`"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"`<br>`"Disabled"` |
| `upscaler_model.upscaler_resolution` | La resolución de salida objetivo para el mejorador de resolución. Este parámetro es obligatorio cuando se selecciona un modelo de mejora (no "Disabled"). | COMBO | Condicional | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_model.creativity` | Intensidad creativa de la mejora. Disponible solo para los modelos "Astra 2" y "Starlight (Astra) Creative". Para Astra 2, es un control deslizante (predeterminado: 0.5). Para Starlight Creative, es un combo (predeterminado: "low"). | FLOAT / COMBO | Condicional | Astra 2: 0.0 a 1.0 (paso 0.1)<br>Starlight Creative: `"low"`<br>`"middle"`<br>`"high"` |
| `upscaler_model.prompt` | Indicación opcional descriptiva (no instructiva) de la escena. Solo disponible para el modelo "Astra 2". Limitado a 500 cuadros de entrada (~15s a 30fps) cuando se establece. Predeterminado: vacío. | STRING | No | - |
| `upscaler_model.sharp` | Nitidez previa a la mejora: 0.0=desenfoque gaussiano, 0.5=paso directo (predeterminado), 1.0=enfocado USM. Solo disponible para el modelo "Astra 2". Predeterminado: 0.5. | FLOAT | No | 0.0 a 1.0 (paso 0.01) |
| `upscaler_model.realism` | Inclina la salida hacia el realismo fotográfico. Déjalo en 0 para el valor predeterminado del modelo. Solo disponible para el modelo "Astra 2". Predeterminado: 0.0. | FLOAT | No | 0.0 a 1.0 (paso 0.01) |
| `interpolation_model` | El modelo de IA utilizado para la interpolación de cuadros. Seleccionar "Disabled" significa que no se aplicará interpolación. | COMBO | Sí | `"Disabled"`<br>`"apo-8"` |
| `interpolation_model.interpolation_frame_rate` | Frecuencia de cuadros de salida. Obligatorio cuando el modelo de interpolación es "apo-8". Predeterminado: 60. | INT | Condicional | 15 a 240 |
| `interpolation_model.interpolation_slowmo` | Factor de cámara lenta aplicado al video de entrada. Por ejemplo, 2 hace que la salida sea el doble de lenta y duplica la duración. Predeterminado: 1. | INT | No | 1 a 16 |
| `interpolation_model.interpolation_duplicate` | Analizar la entrada en busca de cuadros duplicados y eliminarlos. Predeterminado: False. | BOOLEAN | No | True/False |
| `interpolation_model.interpolation_duplicate_threshold` | Sensibilidad de detección para cuadros duplicados. Predeterminado: 0.01. | FLOAT | No | 0.001 a 0.1 (paso 0.001) |
| `dynamic_compression_level` | Nivel CQP para compresión de video. Predeterminado: "Low". | COMBO | No | `"Low"`<br>`"Mid"`<br>`"High"` |

**Restricciones importantes:**
- Al menos uno de `upscaler_model` o `interpolation_model` debe estar habilitado (no "Disabled"), de lo contrario se genera un error.
- El video de entrada debe estar en formato contenedor MP4.
- El modelo "Astra 2" con una indicación está limitado a 500 cuadros de entrada (~15 segundos a 30fps). Sin indicación, está limitado a un número mayor de cuadros.
- Cuando `upscaler_model` no es "Disabled", el subparámetro `upscaler_resolution` es obligatorio.
- Cuando `interpolation_model` no es "Disabled", el subparámetro `interpolation_frame_rate` es obligatorio.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `video` | El video mejorado después de aplicar los filtros seleccionados de mejora de resolución y/o interpolación. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhanceV2/es.md)

---
**Source fingerprint (SHA-256):** `29b7538206327c35866126c1862c1d1ccea872ba84fbb9c84126114a06e2b00f`
