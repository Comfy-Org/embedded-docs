# LTX 2.5 Audio a Video

Este nodo genera un video que sigue una pista de audio utilizando el modelo LTX 2.5. El audio determina la duración del video (entre 2 y 20 segundos), y opcionalmente puedes proporcionar una imagen para usarla como primer fotograma. El video se genera a través del servicio de API de LTX 2.5.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `audio` | Pista de audio que guía el video. Su duración (2-20 segundos) establece la duración del video. | AUDIO | Sí | 2-20 segundos |
| `modelo` | Versión del modelo LTX 2.5 a utilizar. La resolución del video (1920x1080 o 1080x1920) se selecciona junto con el modelo; ambos modelos ofrecen las mismas opciones de resolución. | COMBO | Sí | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `prompt` | Una descripción de texto que guía el contenido del video generado (por defecto: ""). Debe contener al menos 1 carácter y como máximo 10000 caracteres. | STRING | Sí | 1-10000 caracteres |
| `semilla` | Un número que controla la aleatoriedad de la generación. La misma semilla produce el mismo resultado (por defecto: 42). | INT | Sí | Cualquier entero |
| `imagen` | Primer fotograma opcional que se utilizará para el video. Solo se admite una imagen. | IMAGE | No | Una sola imagen |

Notas sobre las restricciones:
- La duración del audio debe estar entre 2 y 20 segundos; el nodo genera un error si está fuera de este rango.
- El prompt es obligatorio y no puede estar vacío; debe tener entre 1 y 10000 caracteres.
- Solo se acepta una única imagen de entrada cuando se proporciona `image`.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `video` | El video generado guiado por la pista de audio proporcionada. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25AudioToVideo/es.md)

---
**Source fingerprint (SHA-256):** `ae0d0123c0421f645448496d30a53a21aba1728310180719a4c4599eca8351c5`
