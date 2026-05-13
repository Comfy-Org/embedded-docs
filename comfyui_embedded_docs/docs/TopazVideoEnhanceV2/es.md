> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhanceV2/es.md)

# Topaz Video Enhance V2

El nodo **Topaz Video Enhance V2** permite mejorar la resolución y calidad de videos utilizando los modelos de IA de Topaz Labs. Puede aumentar la resolución, ajustar la frecuencia de cuadros mediante interpolación y aplicar mejoras creativas o realistas para dar nueva vida a tus secuencias de video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `video` | VIDEO | Sí | - | El video de entrada a procesar. Debe estar en formato contenedor MP4. |
| `upscaler_model` | COMBO | Sí | `"Astra 2"`<br>`"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"`<br>`"Disabled"` | El modelo de IA utilizado para mejorar la resolución del video. Seleccionar "Disabled" significa que no se aplicará mejora de resolución. |
| `upscaler_model.upscaler_resolution` | COMBO | Condicional | `"FullHD (1080p)"`<br>`"4K (2160p)"` | La resolución de salida objetivo para el mejorador de resolución. Este parámetro es obligatorio cuando se selecciona un modelo de mejora (no "Disabled"). |
| `upscaler_model.creativity` | FLOAT / COMBO | Condicional | Astra 2: 0.0 a 1.0 (paso 0.1)<br>Starlight Creative: `"low"`<br>`"middle"`<br>`"high"` | Intensidad creativa de la mejora. Disponible solo para los modelos "Astra 2" y "Starlight (Astra) Creative". Para Astra 2, es un control deslizante (predeterminado: 0.5). Para Starlight Creative, es un combo (predeterminado: "low"). |
| `upscaler_model.prompt` | STRING | No | - | Indicación opcional descriptiva (no instructiva) de la escena. Solo disponible para el modelo "Astra 2". Limitado a 500 cuadros de entrada (~15s a 30fps) cuando se establece. Predeterminado: vacío. |
| `upscaler_model.sharp` | FLOAT | No | 0.0 a 1.0 (paso 0.01) | Nitidez previa a la mejora: 0.0=desenfoque gaussiano, 0.5=paso directo (predeterminado), 1.0=enfocado USM. Solo disponible para el modelo "Astra 2". Predeterminado: 0.5. |
| `upscaler_model.realism` | FLOAT | No | 0.0 a 1.0 (paso 0.01) | Inclina la salida hacia el realismo fotográfico. Déjalo en 0 para el valor predeterminado del modelo. Solo disponible para el modelo "Astra 2". Predeterminado: 0.0. |
| `interpolation_model` | COMBO | Sí | `"Disabled"`<br>`"apo-8"` | El modelo de IA utilizado para la interpolación de cuadros. Seleccionar "Disabled" significa que no se aplicará interpolación. |
| `interpolation_model.interpolation_frame_rate` | INT | Condicional | 15 a 240 | Frecuencia de cuadros de salida. Obligatorio cuando el modelo de interpolación es "apo-8". Predeterminado: 60. |
| `interpolation_model.interpolation_slowmo` | INT | No | 1 a 16 | Factor de cámara lenta aplicado al video de entrada. Por ejemplo, 2 hace que la salida sea el doble de lenta y duplica la duración. Predeterminado: 1. |
| `interpolation_model.interpolation_duplicate` | BOOLEAN | No | True/False | Analizar la entrada en busca de cuadros duplicados y eliminarlos. Predeterminado: False. |
| `interpolation_model.interpolation_duplicate_threshold` | FLOAT | No | 0.001 a 0.1 (paso 0.001) | Sensibilidad de detección para cuadros duplicados. Predeterminado: 0.01. |
| `dynamic_compression_level` | COMBO | No | `"Low"`<br>`"Mid"`<br>`"High"` | Nivel CQP para compresión de video. Predeterminado: "Low". |

**Restricciones importantes:**
- Al menos uno de `upscaler_model` o `interpolation_model` debe estar habilitado (no "Disabled"), de lo contrario se genera un error.
- El video de entrada debe estar en formato contenedor MP4.
- El modelo "Astra 2" con una indicación está limitado a 500 cuadros de entrada (~15 segundos a 30fps). Sin indicación, está limitado a un número mayor de cuadros.
- Cuando `upscaler_model` no es "Disabled", el subparámetro `upscaler_resolution` es obligatorio.
- Cuando `interpolation_model` no es "Disabled", el subparámetro `interpolation_frame_rate` es obligatorio.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `video` | VIDEO | El video mejorado después de aplicar los filtros seleccionados de mejora de resolución y/o interpolación. |

---
**Source fingerprint (SHA-256):** `29b7538206327c35866126c1862c1d1ccea872ba84fbb9c84126114a06e2b00f`
