# HeyGenAvatarVideoNode

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

Genera un video de presentador parlante a partir de un avatar de HeyGen. Este nodo crea un video de un avatar de IA que habla el texto proporcionado o sincroniza los labios con tu propio audio, utilizando los motores de renderizado de HeyGen.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `engine` | Motor de renderizado; cada opción muestra solo los avatares que lo soportan. 'auto' ofrece todos los avatares y selecciona su mejor motor (Avatar IV preferido). Avatar V es la máxima fidelidad, Avatar III es el más económico. | COMBO | Sí | `"auto"`<br>`"avatar_iv"`<br>`"avatar_iii"`<br>`"avatar_v"` |
| `custom_avatar_id` | ID opcional de apariencia de avatar de HeyGen. Cuando se establece, anula el avatar seleccionado anteriormente. Se puede usar cualquiera de las más de 3000 apariencias públicas de HeyGen (o tus avatares privados). | STRING | No |  |
| `speech` | Controla el avatar con un guion de texto (texto a voz de HeyGen) o con tu propio audio. | COMBO | Sí | `"script"`<br>`"audio"` |
| `resolution` | Resolución del video de salida (predeterminado: "1080p"). | COMBO | No | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Relación de aspecto de salida. 'auto' sigue el metraje original del avatar (predeterminado: "auto"). | COMBO | No | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `background_color` | Color de fondo sólido opcional como código hexadecimal (ej. '#00ff00'). Déjalo vacío para usar el fondo propio del avatar. | STRING | No |  |
| `seed` | No se envía a HeyGen; cámbialo para forzar una nueva ejecución (predeterminado: 42). | INT | No | Mín: 0<br>Máx: 2147483647 |

Cuando `speech` está configurado como `"script"`, están disponibles los siguientes subparámetros:

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `text` | Texto que debe hablar el avatar (hasta 5000 caracteres). El discurso generado debe tener al menos 1 segundo de duración. | STRING | Sí |  |
| `voice` | Voz para el guion. La opción predeterminada usa la voz que HeyGen asignó al avatar. | COMBO | Sí | Múltiples opciones disponibles |
| `custom_voice_id` | ID de voz opcional de HeyGen. Cuando se establece, anula la voz seleccionada anteriormente. Se puede usar cualquier voz de la biblioteca de HeyGen (más de 2000). | STRING | No |  |
| `voice_speed` | Multiplicador de velocidad del habla (predeterminado: 1.0). | FLOAT | No | Mín: 0.5<br>Máx: 1.5<br>Paso: 0.05 |

Cuando `speech` está configurado como `"audio"`, está disponible el siguiente subparámetro:

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `audio` | Audio para que el avatar sincronice los labios, hasta 10 minutos. | AUDIO | Sí |  |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `VIDEO` | El video de presentador avatar generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatarVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `009bc72b841ca273af83fe6f80fb24d4b11c2efd96c011795b1ff1cf8e66ee61`
