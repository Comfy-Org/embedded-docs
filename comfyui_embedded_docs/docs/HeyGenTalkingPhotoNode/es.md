# HeyGenTalkingPhotoNode

Transforma una imagen estática de una persona en un video parlante con sincronización labial utilizando la tecnología Avatar IV de HeyGen. Puedes controlar la animación con un guion de texto que HeyGen convierte en voz, o proporcionar tu propio audio para que el avatar sincronice los labios.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `image` | Imagen de una persona para animar. Se reduce automáticamente si es mayor a 2K. | IMAGE | Sí | - |
| `speech` | Controla el avatar con un guion de texto (texto a voz de HeyGen) o tu propio audio. | COMBO | Sí | `"script"`<br>`"audio"` |
| `text` | Texto que el avatar debe decir (hasta 5000 caracteres). El discurso generado debe tener al menos 1 segundo de duración. | STRING | Sí (cuando speech es "script") | - |
| `voice` | Voz para el guion (las voces más populares de HeyGen). | COMBO | Sí (cuando speech es "script") | Múltiples opciones disponibles |
| `custom_voice_id` | ID de voz opcional de HeyGen. Cuando se establece, anula la voz seleccionada anteriormente. Se puede usar cualquier voz de la biblioteca de HeyGen (más de 2000). | STRING | No | - |
| `voice_speed` | Multiplicador de velocidad del habla (predeterminado: 1.0). | FLOAT | No | 0.5 a 1.5 |
| `audio` | Audio para que el avatar sincronice los labios, hasta 10 minutos. | AUDIO | Sí (cuando speech es "audio") | - |
| `resolution` | Resolución del video de salida (predeterminado: "1080p"). | COMBO | No | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Relación de aspecto de salida. 'auto' sigue la imagen de entrada (predeterminado: "auto"). | COMBO | No | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `expressiveness` | Qué tan expresivos son el rostro y los gestos animados (predeterminado: "low"). | COMBO | No | `"low"`<br>`"medium"`<br>`"high"` |
| `seed` | No se envía a HeyGen; cámbialo para forzar una nueva ejecución (predeterminado: 42). | INT | No | 0 a 2147483647 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `video` | Video generado de la foto parlante animada con discurso sincronizado con los labios. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenTalkingPhotoNode/es.md)

---
**Source fingerprint (SHA-256):** `2181066a8c6191cfcaa15ece4f89a16c37e76aa22763d6df4007baa20336f05a`
