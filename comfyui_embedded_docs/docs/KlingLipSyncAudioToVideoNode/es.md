Eres un experto en traducción técnica especializado en documentación de nodos ComfyUI del inglés al español.

## Reglas de Traducción

1. **Contenido que NO debe traducirse:**
   - Nombres de parámetros entre comillas invertidas: `image`, `seed`, `model`
   - Tipos de datos en MAYÚSCULAS: IMAGE, STRING, INT, FLOAT, MODEL, CONDITIONING, etc.
   - Valores en columna Range: números, "auto", nombres de opciones
   - Código, rutas de archivos

2. **Contenido que SÍ debe traducirse:**
   - Títulos de secciones: ## Descripción general, ## Entradas, ## Salidas
   - Todo el texto descriptivo y explicativo
   - Descripciones de parámetros

3. **Calidad de traducción:**
   - Usar español estándar y neutral
   - Mantener tono profesional pero accesible
   - Asegurar precisión técnica
   - Usar terminología técnica estándar en español

4. **Formato:**
   - Mantener todo el formato Markdown
   - Preservar estructura de tablas
   - No agregar ninguna nota o enlace al inicio del documento (será agregado automáticamente)

Por favor traduce la siguiente documentación al español, sin incluir la nota inicial del documento:

Nodo de Sincronización Labial Kling Audio a Video sincroniza los movimientos de la boca en un archivo de video para que coincidan con el contenido de audio de un archivo de audio. Este nodo analiza los patrones vocales en el audio y ajusta los movimientos faciales en el video para crear una sincronización labial realista. El proceso requiere tanto un video que contenga un rostro claramente visible como un archivo de audio con voces claramente distinguibles.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `video` | El archivo de video que contiene un rostro para sincronizar los labios | VIDEO | Sí | - |
| `audio` | El archivo de audio que contiene la voz para sincronizar con el video | AUDIO | Sí | - |
| `idioma_de_voz` | El idioma de la voz en el archivo de audio (predeterminado: "en") | COMBO | Sí | `"en"`<br>`"zh"`<br>`"es"`<br>`"fr"`<br>`"de"`<br>`"it"`<br>`"pt"`<br>`"pl"`<br>`"tr"`<br>`"ru"`<br>`"nl"`<br>`"cs"`<br>`"ar"`<br>`"ja"`<br>`"hu"`<br>`"ko"` |

**Restricciones importantes:**

- El archivo de audio no debe superar los 5 MB
- El archivo de video no debe superar los 100 MB
- Las dimensiones del video deben estar entre 720 px y 1920 px de alto/ancho
- La duración del video debe estar entre 2 segundos y 10 segundos
- El audio debe contener voces claramente distinguibles
- El video debe contener un rostro claramente visible

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `id_de_video` | El video procesado con movimientos de boca sincronizados con los labios | VIDEO |
| `id_de_video` | El identificador único del video procesado | STRING |
| `duración` | La duración del video procesado | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncAudioToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `92b8a7a4f9508632155a5f69707ffc4a14f2f44c04e4d01bf46476a972465592`
