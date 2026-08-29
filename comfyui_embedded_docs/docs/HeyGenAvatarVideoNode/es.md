# Video de Avatar HeyGen

Genera un vídeo de presentador parlante a partir de un avatar de HeyGen. Este nodo crea un vídeo de un avatar de IA que habla el texto proporcionado o sincroniza los labios con tu propio audio, utilizando los motores de renderizado de HeyGen.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `motor` | Motor de renderizado; cada opción lista solo los avatares que lo admiten. `"auto"` ofrece todos los avatares y elige su mejor motor (Avatar IV preferido). Avatar V es la mayor fidelidad, Avatar III es el más asequible. | DYNAMIC_COMBO | Sí | `"auto"`<br>`"avatar_iv"`<br>`"avatar_iii"`<br>`"avatar_v"` |
| `custom_avatar_id` | ID de aspecto de avatar de HeyGen opcional. Cuando se establece, anula el avatar seleccionado arriba. Se puede usar cualquiera de los más de 3000 aspectos públicos de HeyGen (o tus avatares privados). Por defecto: `""`. | STRING | No |  |
| `voz` | Impulsa el avatar con un guion de texto (texto a voz de HeyGen) o tu propio audio. Nombre mostrado: `"speech source"`. | DYNAMIC_COMBO | Sí | `"script"`<br>`"audio"` |
| `resolución` | Resolución de vídeo de salida. Por defecto: `"1080p"`. | COMBO | No | `"720p"`<br>`"1080p"` |
| `relación de aspecto` | Relación de aspecto de salida. `"auto"` sigue el metraje de origen del avatar. Por defecto: `"auto"`. | COMBO | No | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `color de fondo` | Color de fondo sólido opcional como código hexadecimal (p. ej. `"#00ff00"`). Déjalo vacío para usar el fondo propio del avatar. Si se proporciona, el valor debe comenzar con `#`. Por defecto: `""`. | STRING | No |  |
| `semilla` | No se envía a HeyGen; cámbialo para forzar una nueva ejecución. Por defecto: `42`. | INT | No | Mín: 0<br>Máx: 2147483647 |

### Entradas de `auto`

Cuando `engine` es `"auto"`, está disponible el siguiente subparámetro:

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Aspecto de avatar para presentar el vídeo (seleccionado de la biblioteca pública de HeyGen). El mejor motor que admite el aspecto se elige automáticamente. | COMBO | Sí | Hay múltiples opciones disponibles |

### Entradas de `avatar_iv`

Cuando `engine` es `"avatar_iv"`, está disponible el siguiente subparámetro:

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Aspectos de avatar que admiten el motor Avatar IV. | COMBO | Sí | Hay múltiples opciones disponibles |

### Entradas de `avatar_iii`

Cuando `engine` es `"avatar_iii"`, está disponible el siguiente subparámetro:

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Aspectos de avatar que admiten el motor Avatar III. | COMBO | Sí | Hay múltiples opciones disponibles |

### Entradas de `avatar_v`

Cuando `engine` es `"avatar_v"`, está disponible el siguiente subparámetro:

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Aspectos de avatar que admiten el motor Avatar V. | COMBO | Sí | Hay múltiples opciones disponibles |

### Entradas de `script`

Cuando `speech` es `"script"`, están disponibles los siguientes subparámetros:

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `text` | Texto que debe decir el avatar (hasta 5000 caracteres). El discurso generado debe durar al menos 1 segundo. Por defecto: `""`. | STRING | Sí | Mín: 1 carácter<br>Máx: 5000 caracteres |
| `voice` | Voz para el guion. La opción predeterminada usa la voz que HeyGen asignó al avatar. Se ignora si `custom_voice_id` está establecido. | COMBO | Sí | `"(avatar's default voice)"`<br>Hay varias opciones de voz generales disponibles |
| `custom_voice_id` | ID de voz de HeyGen opcional. Cuando se establece, anula la voz seleccionada arriba. Se puede usar cualquier voz de la biblioteca de HeyGen (más de 2000). Por defecto: `""`. | STRING | No |  |
| `voice_speed` | Multiplicador de velocidad del habla. Por defecto: `1.0`. | FLOAT | No | Mín: 0.5<br>Máx: 1.5<br>Paso: 0.05 |

### Entradas de `audio`

Cuando `speech` es `"audio"`, está disponible el siguiente subparámetro:

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `audio` | Audio para que el avatar sincronice los labios, hasta 10 minutos. | AUDIO | Sí |  |

Nota: `engine` y `speech` son selectores que muestran diferentes subparámetros según el valor elegido. El selector `speech` tiene dos modos mutuamente excluyentes: en el modo `"script"`, se requiere `text`; si se proporciona `custom_voice_id`, anula a `voice`. En el modo `"audio"`, el avatar sincroniza los labios con el clip de audio proporcionado. `background_color` debe ser un código de color hexadecimal que comience con `#` cuando se proporcione. Cuando se establece `custom_avatar_id`, este anula la selección de `avatar`, y el `engine` seleccionado debe ser compatible con ese aspecto de avatar; de lo contrario, se genera un error a menos que `engine` sea `"auto"`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `VIDEO` | El vídeo de presentador avatar generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatarVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `86dc799d3a8cf2666449b0d422853b12feffb81ce002f84594f9b925d58b522a`
