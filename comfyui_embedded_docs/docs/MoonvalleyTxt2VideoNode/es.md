El nodo Moonvalley Marey de Texto a Video genera contenido de video a partir de descripciones textuales utilizando la API de Moonvalley. Toma un mensaje de texto y lo convierte en un video con configuraciones personalizables para resolución, calidad y estilo. El nodo maneja todo el proceso, desde el envío de la solicitud de generación hasta la descarga del video final.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Descripción textual del contenido del video a generar | STRING | Sí | - |
| `negative_prompt` | Texto de prompt negativo (predeterminado: lista extensa de elementos excluidos como sintético, corte de escena, artefactos, ruido, etc.) | STRING | No | - |
| `resolution` | Resolución del video de salida (predeterminado: "16:9 (1920 x 1080)") | STRING | No | "16:9 (1920 x 1080)"<br>"9:16 (1080 x 1920)"<br>"1:1 (1152 x 1152)"<br>"4:3 (1536 x 1152)"<br>"3:4 (1152 x 1536)"<br>"21:9 (2560 x 1080)" |
| `prompt_adherence` | Escala de guía para el control de generación (predeterminado: 4.0) | FLOAT | No | 1.0-20.0 |
| `seed` | Valor de semilla aleatoria (predeterminado: 9) | INT | No | 0-4294967295 |
| `steps` | Pasos de inferencia (predeterminado: 33) | INT | No | 1-100 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `video` | El video generado a partir del prompt de texto | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyTxt2VideoNode/es.md)

---
**Source fingerprint (SHA-256):** `3654043567d7aca3af741d706ee07a8d2e28dbeb4b5b8755514b790aa7c1bd41`
