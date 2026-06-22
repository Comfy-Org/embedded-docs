# ByteDance Seedance 2.0 Primer-Último Fotograma a Video

Este nodo utiliza el modelo Seedance 2.0 de ByteDance para generar un video. Crea el video basándose en un prompt de texto y una imagen de primer fotograma obligatoria. Opcionalmente, puedes proporcionar una imagen de último fotograma para guiar el final de la secuencia del video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo a utilizar para la generación de video. Seedance 2.0 es para máxima calidad, mientras que Seedance 2.0 Fast está optimizado para velocidad. Seleccionar un modelo revelará entradas adicionales para `prompt`, `resolution`, `ratio`, `duration` y `generate_audio`. | COMBO | Sí | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` |
| `primer_fotograma` | La imagen que se usará como primer fotograma del video. | IMAGE | No | - |
| `último_fotograma` | La imagen que se usará como último fotograma del video. | IMAGE | No | - |
| `first_frame_asset_id` | Un asset_id de Seedance para usar como primer fotograma. No se puede usar al mismo tiempo que la entrada de imagen `primer_fotograma`. El valor predeterminado es una cadena vacía. | STRING | No | - |
| `last_frame_asset_id` | Un asset_id de Seedance para usar como último fotograma. No se puede usar al mismo tiempo que la entrada de imagen `último_fotograma`. El valor predeterminado es una cadena vacía. | STRING | No | - |
| `semilla` | Un valor de semilla. Cambiar esta semilla hará que el nodo se ejecute nuevamente, pero los resultados no son deterministas. El valor predeterminado es 0. | INT | No | 0 a 2147483647 |
| `marca_de_agua` | Si se debe agregar una marca de agua al video generado. El valor predeterminado es Falso. | BOOLEAN | No | - |

**Restricciones de Parámetros:**
*   Debes proporcionar **ya sea** una imagen `first_frame` **o** un `first_frame_asset_id`. Proporcionar ambos causará un error.
*   No puedes proporcionar tanto una imagen `last_frame` como un `last_frame_asset_id` para el mismo fotograma.
*   La entrada `model` es un combo dinámico. Después de seleccionar un modelo, también debes completar el campo `prompt` revelado (una descripción de texto) y configurar los otros parámetros revelados (`resolution`, `ratio`, `duration`, `generate_audio`).

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/es.md)

---
**Source fingerprint (SHA-256):** `2c9c1fe8fddd0c3e1c356d2b93a06a07f83db8f7a0380e94629a91ce1ff1e29a`
