# PixVerse V6 de imagen a vídeo

Este nodo anima una imagen de entrada con el modelo PixVerse V6 y devuelve un video, opcionalmente con una pista de audio nativa. El video de salida mantiene la proporción de aspecto de la imagen de entrada.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `modelo` | Configuración del modelo y de la generación. | DYNAMIC_COMBO | Sí | "PixVerse V6" |
| `imagen` | La imagen de entrada que se va a animar. | IMAGE | Sí | Imagen única |

### Entradas de PixVerse V6

Estos ajustes aparecen cuando se selecciona el modelo «PixVerse V6».

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | Prompt para la generación del video (por defecto: vacío). | STRING | Sí | De 1 a 5000 caracteres |
| `quality` | Resolución de salida. Define el borde largo: 360p es 640px, 540p 1024px, 720p 1280px, 1080p 1920px (por defecto: «720p»). | COMBO | Sí | «360p»<br>«540p»<br>«720p»<br>«1080p» |
| `duration_seconds` | Duración del video generado en segundos (por defecto: 5). | INT | Sí | De 1 a 15 |
| `generate_audio` | Generar una pista de audio nativa junto con el video (por defecto: true). | BOOLEAN | Sí | true o false |
| `multi_clip` | Permitir que el modelo corte el video en varias tomas en lugar de una toma continua (por defecto: false). | BOOLEAN | Sí | true o false |
| `seed` | Semilla para la generación del video. PixVerse la registra, pero no reproduce una ejecución a partir de ella (por defecto: 42, control después de generar está habilitado). | INT | Sí | De 0 a 2147483647 |
| `negative_prompt` | Descripción textual opcional de elementos no deseados en el video (por defecto: vacío). | STRING | No | Hasta 2048 caracteres |
| `style` | Estilo visual opcional aplicado a todo el video (por defecto: ninguno). | COMBO | No | Múltiples opciones disponibles (ajustes preestablecidos de estilo de PixVerse V6) |

Nota: El prompt debe contener al menos un carácter que no sea un espacio en blanco y como máximo 5000 caracteres; el negative prompt, si se proporciona, debe tener como máximo 2048 caracteres. El video de salida siempre coincide con la proporción de aspecto de la imagen de entrada, por lo que no se necesita ningún ajuste de proporción de aspecto. Solo se acepta una única imagen de entrada. PixVerse puede rechazar una solicitud cuando falla la moderación de contenido, cuando la cuenta del proveedor no tiene créditos o cuando ya se está ejecutando el número máximo de generaciones simultáneas.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El video generado, incluida la pista de audio nativa cuando `generate_audio` está habilitado. La proporción de aspecto coincide con la de la imagen de entrada. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6ImageToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `6ecf958e510e7afc43f5f0e4e5dfd2b789aea02bec882d928326732501cee7b3`
