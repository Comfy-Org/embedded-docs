# BerniniConditioning

El nodo BerniniConditioning prepara datos de condicionamiento de video e imagen para el modelo Wan2.2-A14B. Codifica videos fuente, videos de referencia e imágenes de referencia utilizando el VAE proporcionado, y luego los adjunta a los datos de condicionamiento para tareas de generación en contexto.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `positivo` | Datos de condicionamiento positivo | CONDITIONING | Sí | - |
| `negativo` | Datos de condicionamiento negativo | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar entradas de video e imagen | VAE | Sí | - |
| `ancho` | Ancho del latente de salida (predeterminado: 832) | INT | Sí | 16 a 8192 (paso: 16) |
| `alto` | Alto del latente de salida (predeterminado: 480) | INT | Sí | 16 a 8192 (paso: 16) |
| `longitud` | Número de fotogramas en el latente de salida (predeterminado: 81) | INT | Sí | 1 a 8192 (paso: 4) |
| `tamaño_lote` | Número de videos a generar en un solo lote (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `video_fuente` | Video fuente para editar o cambiar el estilo (v2v, rv2v). Redimensionado al ancho/alto y recortado a la longitud especificada. | IMAGE | No | - |
| `video_referencia` | Video para insertar en el video fuente (ads2v). | IMAGE | No | - |
| `imágenes_referencia` | Imágenes de referencia inyectadas como tokens de contexto (r2v, rv2v). Se pueden proporcionar hasta 8 imágenes. | IMAGE | No | 0 a 8 imágenes |
| `ref_max_size` | Tamaño máximo para el borde largo de reference_video y reference_images. Redimensionado manteniendo la relación de aspecto y ajustado a 16px (predeterminado: 848). | INT | No | 16 a 8192 (paso: 16) |

**Nota:** La tarea se infiere según qué entradas están conectadas:
- Sin entradas conectadas → texto a video (t2v)
- Solo `source_video` → video a video (v2v)
- `source_video` + `reference_images` → edición de video guiada por referencia (rv2v)
- Solo `reference_images` → referencia a video (r2v)
- `source_video` + `reference_video` → insertar imagen/video en video (ads2v)

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `negativo` | Condicionamiento positivo con latentes de contexto adjuntos | CONDITIONING |
| `latente` | Condicionamiento negativo con latentes de contexto adjuntos | CONDITIONING |
| `latent` | Tensor latente vacío con dimensiones que coinciden con el ancho, alto, longitud y tamaño de lote especificados | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BerniniConditioning/es.md)

---
**Source fingerprint (SHA-256):** `3535bbe9a1ae007dc579242b44787ab315479a820eb0da680eab9b870ab60699`
