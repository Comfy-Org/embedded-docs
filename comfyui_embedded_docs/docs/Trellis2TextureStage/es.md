# Trellis2TextureStage

Este nodo configura la pasada de muestreo de la etapa de textura para la generación de Trellis2. Lee la disposición de coordenadas y el latente de forma por vóxel del latente de forma entrante, construye un latente disperso vacío con 32 canales en la misma disposición de coordenadas y adjunta los metadatos requeridos de la etapa de textura al condicionamiento.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `positivo` | El condicionamiento positivo utilizado para la pasada de generación de texturas. Se le adjuntan los metadatos de la etapa de textura. | CONDITIONING | Sí | - |
| `negativo` | El condicionamiento negativo utilizado para la pasada de generación de texturas. Se le adjuntan los metadatos de la etapa de textura. | CONDITIONING | Sí | - |
| `latent de forma` | El dict latente producido por Trellis2ShapeStage o Trellis2UpsampleStage. Debe contener `coords` (la disposición de coordenadas, forma [N, 4]) y `samples` (el latente de forma por vóxel); `coord_resolution` y `model_frame` son opcionales. | LATENT | Sí | - |

Notas:
- `shape_latent` debe ser la salida de Trellis2ShapeStage o Trellis2UpsampleStage; proporciona la disposición de coordenadas y el latente de forma por vóxel utilizados por la pasada de textura.
- La disposición de coordenadas se valida: los ids de lote en la primera columna de `coords` deben ser no negativos y contiguos, y el número total de filas debe coincidir con los recuentos de coordenadas.
- Cuando `positive` incluye un paquete de características de proyección (condicionamiento Pixal3D) y `shape_latent` incluye `coord_resolution`, se calculan las características de proyección a resolución de textura 1024 y se adjuntan al condicionamiento.
- El marco del modelo se lee de `shape_latent`; cuando está ausente, se define por defecto como `"y_up"` si hay características de proyección y `"z_up"` en caso contrario.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `positivo` | El condicionamiento positivo con los metadatos de la etapa de textura adjuntos (modo de generación, coordenadas, recuentos de coordenadas, latente de forma, marco del modelo y características de proyección cuando corresponda). | CONDITIONING |
| `negativo` | El condicionamiento negativo con los mismos metadatos de la etapa de textura adjuntos. | CONDITIONING |
| `latent` | Un nuevo latente disperso vacío con 32 canales en la misma disposición de coordenadas que el latente de forma entrante. Su dict incluye `samples`, `type` ("trellis2"), `coords`, `coord_counts` y `model_frame`; `coord_resolution` se incluye cuando está disponible. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2TextureStage/es.md)

---
**Source fingerprint (SHA-256):** `ae612021af7c74cd09206d905e7b800fa48367a22daf9b0335b444c854a78b1e`
