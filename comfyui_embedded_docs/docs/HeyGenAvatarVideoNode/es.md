# Video de Avatar HeyGen

Genera un video con un presentador virtual que habla a partir de un avatar de HeyGen. Este nodo crea un video de un avatar de IA que pronuncia el texto proporcionado o sincroniza los labios con tu propio audio, utilizando los motores de renderizado de HeyGen.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `motor` | Motor de renderizado; cada opción muestra solo los avatares compatibles con él. `"auto"` ofrece todos los avatares y elige su mejor motor (se prefiere Avatar IV). Avatar V ofrece la mayor fidelidad, Avatar III es el más económico. | DYNAMIC_COMBO | Sí | `"auto"`<br>`"avatar_iv"`<br>`"avatar_iii"`<br>`"avatar_v"` |
| `custom_avatar_id` | ID de apariencia de avatar de HeyGen opcional. Cuando se establece, reemplaza el avatar seleccionado arriba. Se puede usar cualquiera de las más de 3000 apariencias públicas de HeyGen (o tus avatares privados). Valor predeterminado: cadena vacía. | STRING | No |  |
| `voz` | Controla el avatar mediante un guion de texto (texto a voz de HeyGen) o tu propio audio. | DYNAMIC_COMBO | Sí | `"script"`<br>`"audio"` |
| `resolución` | Resolución del video de salida. Valor predeterminado: `"1080p"`. | COMBO | No | `"720p"`<br>`"1080p"` |
| `relación de aspecto` | Relación de aspecto de salida. `"auto"` sigue el metraje de origen del avatar. Valor predeterminado: `"auto"`. | COMBO | No | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `color de fondo` | Color de fondo sólido opcional como código hexadecimal (p. ej. `"#00ff00"`). Déjalo vacío para usar el fondo propio del avatar. Si se proporciona, el valor debe comenzar con `#`. Valor predeterminado: cadena vacía. | STRING | No |  |
| `semilla` | No se envía a HeyGen; cámbialo para forzar una nueva ejecución. Valor predeterminado: `42`. | INT | No | Mín: 0<br>Máx: 2147483647 |

### Entradas de `auto`

Cuando `engine` es `"auto"`, se encuentra disponible el siguiente subparámetro:

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `avatar` | Apariencia de avatar para presentar el video (seleccionada de la biblioteca pública de HeyGen). El mejor motor compatible con la apariencia se elige automáticamente. | COMBO | Sí | Múltiples opciones disponibles |

### Entradas de `avatar_iv`

Cuando `engine` es `"avatar_iv"`, se encuentra disponible el siguiente subparámetro:

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `avatar` | Apariencias de avatar compatibles con el motor Avatar IV. | COMBO | Sí | Múltiples opciones disponibles |

### Entradas de `avatar_iii`

Cuando `engine` es `"avatar_iii"`, se encuentra disponible el siguiente subparámetro:

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `avatar` | Apariencias de avatar compatibles con el motor Avatar III. | COMBO | Sí | Múltiples opciones disponibles |

### Entradas de `avatar_v`

Cuando `engine` es `"avatar_v"`, se encuentra disponible el siguiente subparámetro:

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `avatar` | Apariencias de avatar compatibles con el motor Avatar V. | COMBO | Sí | Múltiples opciones disponibles |

### Entradas de `script`

Cuando `speech` es `"script"`, se encuentran disponibles los siguientes subparámetros:

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `text` | Texto que el avatar debe pronunciar (hasta 5000 caracteres). La voz generada debe durar al menos 1 segundo. Valor predeterminado: cadena vacía. | STRING | Sí | Mín: 1 carácter<br>Máx: 5000 caracteres |
| `voice` | Voz para el guion. La opción predeterminada usa la voz que HeyGen asignó al avatar. | COMBO | Sí | `"(avatar's default voice)"`<br>Múltiples opciones de voz general disponibles |
| `custom_voice_id` | ID de voz de HeyGen opcional. Cuando se establece, reemplaza la voz seleccionada arriba. Se puede usar cualquier voz de la biblioteca de HeyGen (más de 2000). Valor predeterminado: cadena vacía. | STRING | No |  |
| `voice_speed` | Multiplicador de velocidad del habla. Valor predeterminado: `1.0`. | FLOAT | No | Mín: 0.5<br>Máx: 1.5<br>Paso: 0.05 |

### Entradas de `audio`

Cuando `speech` es `"audio"`, se encuentra disponible el siguiente subparámetro:

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `audio` | Audio para que el avatar sincronice los labios, de hasta 10 minutos. | AUDIO | Sí |  |

Nota: `speech` es un selector de fuente con dos modos mutuamente excluyentes. En el modo `"script"`, `text` es obligatorio (de 1 a 5000 caracteres); si se proporciona `custom_voice_id`, este reemplaza a `voice`. En el modo `"audio"`, el avatar sincroniza los labios con el clip de audio proporcionado. `background_color` debe ser un código de color hexadecimal que comience con `#` cuando se proporcione. Cuando se establece `custom_avatar_id`, este reemplaza la selección de `avatar`, y el `engine` seleccionado debe ser compatible con esa apariencia de avatar; de lo contrario, se genera un error (a menos que `engine` sea `"auto"`).

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `VIDEO` | El video de presentador avatar generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatarVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `009bc72b841ca273af83fe6f80fb24d4b11c2efd96c011795b1ff1cf8e66ee61`
