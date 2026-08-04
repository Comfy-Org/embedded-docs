# Video de Avatar HeyGen

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `engine` | Motor de renderizado; cada opción muestra solo los avatares compatibles con él. `'auto'` ofrece todos los avatares y elige su mejor motor (preferiblemente Avatar IV). Avatar V es el de mayor fidelidad, Avatar III es el más económico. | COMBO | Sí | `"auto"`<br>`"avatar_iv"`<br>`"avatar_iii"`<br>`"avatar_v"` |
| `avatar` | Apariencia de avatar para presentar el video. Con el motor `"auto"`, se selecciona de la biblioteca pública de HeyGen y se elige automáticamente el mejor motor compatible con esa apariencia. Con los motores `"avatar_iv"`, `"avatar_iii"` o `"avatar_v"`, solo se muestran las apariencias de avatar compatibles con ese motor. | COMBO | Sí | Varía según la selección de `engine` |
| `custom_avatar_id` | ID de apariencia de avatar opcional de HeyGen. Cuando se establece, anula la apariencia seleccionada arriba. Se puede usar cualquiera de las más de 3000 apariencias públicas de HeyGen (o tus avatares privados). | STRING | No |  |
| `speech` | Controla el avatar con un guion de texto (texto a voz de HeyGen) o con tu propio audio. Cuando se elige `"script"`, consulta los subparámetros a continuación; cuando se elige `"audio"`, proporciona un archivo de audio para la sincronización de labios. | COMBO | Sí | `"script"`<br>`"audio"` |
| `resolution` | Resolución del video de salida (predeterminado: `"1080p"`). | COMBO | No | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Relación de aspecto de salida. `"auto"` sigue el metraje de origen del avatar (predeterminado: `"auto"`). | COMBO | No | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `background_color` | Color de fondo sólido opcional como código hexadecimal (p. ej. `'#00ff00'`). Déjalo vacío para usar el fondo propio del avatar. Si se proporciona, el valor debe comenzar con `#`. | STRING | No |  |
| `seed` | No se envía a HeyGen; cámbialo para forzar una nueva ejecución (predeterminado: `42`). | INT | No | Mín: 0<br>Máx: 2147483647 |

### Subparámetros cuando `speech` es `"script"`

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `text` | Texto que debe decir el avatar (hasta 5000 caracteres). El discurso generado debe tener al menos 1 segundo de duración. | STRING | Sí |  |
| `voice` | Voz para el guion. La opción predeterminada usa la voz que HeyGen asignó al avatar. | COMBO | Sí | Múltiples opciones disponibles (voz predeterminada más la biblioteca general de voces de HeyGen) |
| `custom_voice_id` | ID de voz opcional de HeyGen. Cuando se establece, anula la voz seleccionada arriba. Se puede usar cualquier voz de la biblioteca de HeyGen (más de 2000). | STRING | No |  |
| `voice_speed` | Multiplicador de velocidad del habla (predeterminado: `1.0`). | FLOAT | No | Mín: 0.5<br>Máx: 1.5<br>Paso: 0.05 |

### Subparámetros cuando `speech` es `"audio"`

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `audio` | Audio para que el avatar sincronice los labios, hasta 10 minutos. | AUDIO | Sí |  |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `VIDEO` | El video de presentador avatar generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatarVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `009bc72b841ca273af83fe6f80fb24d4b11c2efd96c011795b1ff1cf8e66ee61`
