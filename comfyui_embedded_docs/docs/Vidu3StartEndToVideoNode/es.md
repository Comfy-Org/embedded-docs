# Generación de video de inicio/fin de Vidu Q3

Este nodo genera un video interpolando entre un fotograma inicial y un fotograma final proporcionados, guiado por una descripción de texto. Utiliza el modelo Vidu Q3 para crear una transición fluida entre las dos imágenes, produciendo un video de duración y resolución especificadas.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `modelo` | El modelo a utilizar para la generación de video. Al seleccionar una opción se revelan parámetros de configuración adicionales para `resolution`, `duration` y `audio`. | DYNAMIC_COMBO | Sí | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `fotograma inicial` | La imagen inicial para la secuencia de video. | IMAGE | Sí | - |
| `fotograma final` | La imagen final para la secuencia de video. | IMAGE | Sí | - |
| `prompt` | Descripción del prompt (máximo 2000 caracteres). | STRING | Sí | - |
| `semilla` | Un valor de semilla para controlar la aleatoriedad de la generación (predeterminado: 1). | INT | Sí | 0 a 2147483647 |

### Entradas de viduq3-pro y viduq3-turbo

Los siguientes parámetros son compartidos por ambas opciones de modelo (`viduq3-pro` y `viduq3-turbo`). Se revelan después de seleccionar un modelo.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `resolution` | Resolución del video de salida. Este parámetro se revela después de seleccionar un `model`. | COMBO | Sí | `"720p"`<br>`"1080p"` |
| `duration` | Duración del video de salida en segundos (predeterminado: 5). Este parámetro se revela después de seleccionar un `model`. | INT | Sí | 1 a 16 |
| `audio` | Cuando está habilitado, genera video con sonido (incluyendo diálogo y efectos de sonido) (predeterminado: False). Este parámetro se revela después de seleccionar un `model`. | BOOLEAN | Sí | `True`<br>`False` |

**Nota:** Las imágenes `first_frame` y `end_frame` deben tener relaciones de aspecto similares. La relación de aspecto de las dos imágenes debe estar entre el 80% y el 125% entre sí (una cercanía relativa entre 0.8 y 1.25).

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `c917867c5a7b68a1286f445025070f9a55d8d10091d9562960e0428cbedf25e4`
