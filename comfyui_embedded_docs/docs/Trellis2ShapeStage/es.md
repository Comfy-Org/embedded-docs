# Trellis2ShapeStage

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `positive` | El condicionamiento positivo que se preparará para la etapa de formas. Puede ser un condicionamiento estándar de Trellis2 o un condicionamiento Pixal3D que suministre un paquete de características de proyección; cuando las características de proyección están presentes, se calculan para la etapa seleccionada y se adjuntan al condicionamiento de salida. | CONDITIONING | Sí | Cualquier condicionamiento Trellis2 o Pixal3D |
| `negative` | El condicionamiento negativo que se preparará para la etapa de formas. Se le adjuntan los mismos metadatos de la etapa de formas que al condicionamiento positivo. | CONDITIONING | Sí | Cualquier condicionamiento Trellis2 o Pixal3D |
| `voxel` | Voxel de estructura densa procedente de VaeDecodeStructureTrellis2. | VOXEL | Sí | Cualquier rejilla de voxeles; la resolución de la rejilla (voxeles por eje) selecciona la etapa del pipeline |

### Notas

- La resolución de la rejilla de voxeles selecciona la etapa del pipeline: una resolución de 32 o inferior utiliza el modo `shape_generation_512` con la etapa `shape_512`; una resolución mayor que 32 utiliza el modo `shape_generation` con la etapa `shape_1024`.
- El voxel debe contener al menos un voxel relleno; un voxel vacío genera un error. Los índices de lote derivados del voxel deben ser no negativos y contiguos.
- Cuando el condicionamiento `positive` contiene un `proj_feat_pack` (como el suministrado por el condicionamiento Pixal3D), se calculan las características de proyección para la etapa seleccionada y el marco del modelo del latente de salida se establece en `y_up`. De lo contrario, no se adjuntan características de proyección y el marco del modelo se establece en `z_up`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `positive` | El condicionamiento positivo con los metadatos de la etapa de formas adjuntos: modo de generación, coordenadas dispersas, recuentos de coordenadas por lote y características de proyección cuando el condicionamiento de origen las proporciona. | CONDITIONING |
| `negative` | El condicionamiento negativo con los mismos metadatos de la etapa de formas adjuntos. | CONDITIONING |
| `latent` | Un tensor latente disperso vacío (forma: tamaño de lote, 32, recuento de tokens, 1) junto con las coordenadas dispersas extraídas, los recuentos de coordenadas por lote, la resolución de coordenadas, el marcador de tipo `trellis2` y la orientación del marco del modelo. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2ShapeStage/es.md)

---
**Source fingerprint (SHA-256):** `7dbee8a5b6ef7111f07def4dbe1cc4908533e00ffcb775f5a284099360c7eed3`
