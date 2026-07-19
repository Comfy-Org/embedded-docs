# MoonvalleyVideo2VideoNode

El nodo Moonvalley Marey Video a Video transforma un video de entrada en un nuevo video basado en una descripción textual. Utiliza la API de Moonvalley para generar videos que coincidan con tu indicación, preservando las características de movimiento o pose del video original. Puedes controlar el estilo y contenido del video de salida mediante indicaciones de texto y diversos parámetros de generación.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Describe el video a generar (entrada multilínea) | STRING | Sí | - |
| `negative_prompt` | Texto de indicación negativa (valor predeterminado: lista extensa de descriptores negativos) | STRING | No | - |
| `seed` | Valor de semilla aleatoria (valor predeterminado: 9) | INT | Sí | 0 a 4294967295 |
| `video` | El video de referencia utilizado para generar el video de salida. Debe tener al menos 5 segundos de duración. Los videos de más de 5 segundos se recortarán automáticamente. Solo se admite formato MP4. | VIDEO | Sí | - |
| `control_type` | Selección del tipo de control (valor predeterminado: "Transferencia de Movimiento") | COMBO | No | "Transferencia de Movimiento"<br>"Transferencia de Pose" |
| `motion_intensity` | Solo se utiliza si `control_type` es "Transferencia de Movimiento" (valor predeterminado: 100) | INT | No | 0 a 100 |
| `steps` | Número de pasos de inferencia (valor predeterminado: 33) | INT | Sí | 1 a 100 |

**Nota:** El parámetro `motion_intensity` solo se aplica cuando `control_type` está configurado como "Transferencia de Movimiento". Al usar "Transferencia de Pose", este parámetro se ignora.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El video generado como resultado | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyVideo2VideoNode/es.md)

---
**Source fingerprint (SHA-256):** `8202a4be469afa16d77b9e0287c290b9c3f390347fc60f23878f50fd95a758e0`
