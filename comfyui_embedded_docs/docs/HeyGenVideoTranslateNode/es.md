# HeyGenVideoTranslateNode

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

Por favor traduce la siguiente documentación al español, sin incluir la aviso de IA:

5. **CRÍTICO - Nombres de salida:** La primera columna de la tabla de Salidas contiene nombres de salida (ej. `positive`, `negative`, `latent`, `image`, `model`, `conditioning`) que DEBEN permanecer en inglés. Traducir estos nombres crea entradas duplicadas y rompe la estructura del documento.

Traduce un video hablado a otro idioma con clonación de voz y sincronización de labios. Este nodo clona la voz del hablante original y reanima la boca para que coincida con el discurso traducido, produciendo un resultado de apariencia natural.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `video` | Video con discurso a traducir. | VIDEO | Sí | - |
| `output_language` | Idioma de destino para el video traducido. | STRING | Sí | "Arabic"<br>"Bengali"<br>"Chinese"<br>"Danish"<br>"Dutch"<br>"English"<br>"French"<br>"German"<br>"Greek"<br>"Hindi"<br>"Indonesian"<br>"Italian"<br>"Japanese"<br>"Korean"<br>"Malay"<br>"Polish"<br>"Portuguese"<br>"Russian"<br>"Spanish"<br>"Swedish"<br>"Tamil"<br>"Telugu"<br>"Thai"<br>"Turkish"<br>"Ukrainian"<br>"Vietnamese" |
| `mode` | 'speed' es más rápido; 'precision' produce sincronización de labios de mayor calidad al doble de costo. | STRING | Sí | "speed"<br>"precision" |
| `translate_audio_only` | Solo reemplazar la pista de audio, manteniendo los movimientos originales de la boca (sin sincronización de labios). (predeterminado: False) | BOOLEAN | No | True<br>False |
| `speaker_count` | Número de hablantes en el video. 0 = detectar automáticamente. (predeterminado: 0) | INT | No | 0 a 10 |
| `seed` | No se envía a HeyGen; cámbielo para forzar una re-ejecución. (predeterminado: 42) | INT | No | 0 a 2147483647 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|-------------|-------------|-----------|
| `video` | El video traducido con clonación de voz y sincronización de labios aplicada. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVideoTranslateNode/es.md)

---
**Source fingerprint (SHA-256):** `31056060b6309b8ec28b37b353322403e173fd2862b56021392dba24e7a15f69`
