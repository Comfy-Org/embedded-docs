> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyVideo2VideoNode/es.md)

El nodo Moonvalley Marey Video a Video transforma un video de entrada en un nuevo video basado en una descripción textual. Utiliza la API de Moonvalley para generar videos que coincidan con tu indicación, preservando las características de movimiento o pose del video original. Puedes controlar el estilo y contenido del video de salida mediante indicaciones de texto y diversos parámetros de generación.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `prompt` | STRING | Sí | - | Describe el video a generar (entrada multilínea) |
| `negative_prompt` | STRING | No | - | Texto de indicación negativa (valor predeterminado: lista extensa de descriptores negativos) |
| `seed` | INT | Sí | 0 a 4294967295 | Valor de semilla aleatoria (valor predeterminado: 9) |
| `video` | VIDEO | Sí | - | El video de referencia utilizado para generar el video de salida. Debe tener al menos 5 segundos de duración. Los videos de más de 5 segundos se recortarán automáticamente. Solo se admite formato MP4. |
| `control_type` | COMBO | No | "Transferencia de Movimiento"<br>"Transferencia de Pose" | Selección del tipo de control (valor predeterminado: "Transferencia de Movimiento") |
| `motion_intensity` | INT | No | 0 a 100 | Solo se utiliza si `control_type` es "Transferencia de Movimiento" (valor predeterminado: 100) |
| `steps` | INT | Sí | 1 a 100 | Número de pasos de inferencia (valor predeterminado: 33) |

**Nota:** El parámetro `motion_intensity` solo se aplica cuando `control_type` está configurado como "Transferencia de Movimiento". Al usar "Transferencia de Pose", este parámetro se ignora.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `output` | VIDEO | El video generado como resultado |

---
**Source fingerprint (SHA-256):** `8202a4be469afa16d77b9e0287c290b9c3f390347fc60f23878f50fd95a758e0`
