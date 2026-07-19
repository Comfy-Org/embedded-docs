# LumaRay32VideoEditNode

Este nodo vuelve a renderizar un video existente bajo un nuevo prompt utilizando Luma Ray 3.2, permitiéndote cambiar el estilo, la iluminación, añadir o eliminar elementos mientras se conserva el movimiento original. El video fuente puede tener hasta 18 segundos, y el video editado mantiene la duración original del video fuente.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `video` | Video fuente a editar. Hasta 18 segundos. | VIDEO | Sí | - |
| `prompt` | Describe la edición deseada. | STRING | Sí | - |
| `resolution` | La resolución de salida para el video editado. | COMBO | Sí | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `strength` | Qué tan fuertemente preservar vs. reinventar la fuente. "auto" permite que Ray 3.2 elija; adhere_* preserva más, flex_* es equilibrado, reimagine_* cambia más. (por defecto: "auto") | COMBO | Sí | `"auto"`<br>`"adhere_1"`<br>`"adhere_2"`<br>`"adhere_3"`<br>`"flex_1"`<br>`"flex_2"`<br>`"flex_3"`<br>`"reimagine_1"`<br>`"reimagine_2"`<br>`"reimagine_3"` |
| `seed` | Semilla para reproducibilidad. | INT | Sí | - |

**Nota:** El `prompt` debe tener entre 1 y 6000 caracteres. El video fuente no debe exceder los 18 segundos de duración.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `generation_id` | El video editado de salida. | VIDEO |
| `generation_id` | El identificador único para la solicitud de generación. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32VideoEditNode/es.md)

---
**Source fingerprint (SHA-256):** `936d9d7da3fdee9b0b468781fd470751db01f772f3c5c20582da7fb1ff85e6e6`
