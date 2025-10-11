> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncAudioToVideoNode/es.md)

El nodo Kling Lip Sync Audio to Video sincroniza los movimientos de la boca en un archivo de video para que coincidan con el contenido de audio de un archivo de audio. Este nodo analiza los patrones vocales en el audio y ajusta los movimientos faciales en el video para crear una sincronización labial realista. El proceso requiere tanto un video que contenga un rostro diferenciado como un archivo de audio con voces claramente distinguibles.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Sí | - | El archivo de video que contiene un rostro para sincronización labial |
| `audio` | AUDIO | Sí | - | El archivo de audio que contiene las voces para sincronizar con el video |
| `voice_language` | COMBO | No | `"en"`<br>`"zh"`<br>`"es"`<br>`"fr"`<br>`"de"`<br>`"it"`<br>`"pt"`<br>`"pl"`<br>`"tr"`<br>`"ru"`<br>`"nl"`<br>`"cs"`<br>`"ar"`<br>`"ja"`<br>`"hu"`<br>`"ko"` | El idioma de la voz en el archivo de audio (predeterminado: "en") |

**Restricciones Importantes:**
- El archivo de audio no debe ser mayor a 5MB
- El archivo de video no debe ser mayor a 100MB
- Las dimensiones del video deben estar entre 720px y 1920px de alto/ancho
- La duración del video debe estar entre 2 segundos y 10 segundos
- El audio debe contener voces claramente distinguibles
- El video debe contener un rostro diferenciado

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video procesado con movimientos de boca sincronizados |
| `video_id` | STRING | El identificador único para el video procesado |
| `duration` | STRING | La duración del video procesado |