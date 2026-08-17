# WanSoundImageToVideoExtend

El nodo WanSoundImageToVideoExtend extiende un latent de video existente generando fotogramas adicionales, guiado opcionalmente por audio, una imagen de referencia y un video de control. Toma un latent de video inicial y produce una secuencia de video más larga, utilizando las señales de condicionamiento y audio proporcionadas para influir en el nuevo contenido.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `positive` | Indicaciones de condicionamiento positivo que guían lo que debe incluir el video | CONDITIONING | Sí | - |
| `negative` | Indicaciones de condicionamiento negativo que especifican lo que el video debe evitar | CONDITIONING | Sí | - |
| `vae` | Autoencoder variacional utilizado para codificar y decodificar fotogramas de video | VAE | Sí | - |
| `length` | Número total de fotogramas a generar para la secuencia de video (predeterminado: 77, paso: 4) | INT | Sí | 1 to MAX_RESOLUTION |
| `video_latent` | Representación latent de video inicial que sirve como punto de partida para la extensión. El ancho, alto, tamaño de lote y desplazamiento de fotogramas se derivan de este latent. Los últimos 19 fotogramas de este latent también se utilizan como movimiento de referencia para la nueva secuencia. | LATENT | Sí | - |
| `audio_encoder_output` | Embeddings de audio opcionales que pueden influir en la generación de video según las características del sonido. Cuando se proporcionan, el audio se interpola y se utiliza para crear un conjunto de embeddings de audio que se añade al condicionamiento. | AUDIO_ENCODER_OUTPUT | No | - |
| `ref_image` | Imagen de referencia opcional que proporciona guía visual para la generación de video. La imagen se amplía para ajustarse a las dimensiones objetivo y se codifica en un latent, que luego se añade tanto al condicionamiento positivo como al negativo. Solo se utiliza la primera imagen del lote. | IMAGE | No | - |
| `control_video` | Video de control opcional que puede guiar el movimiento y el estilo del video generado. El video se amplía, se codifica y se añade tanto al condicionamiento positivo como al negativo. El video de control se trunca a la `length` especificada. | IMAGE | No | - |

Nota: Cuando se proporciona `audio_encoder_output`, los embeddings de audio se añaden al condicionamiento positivo, mientras que el condicionamiento negativo recibe los mismos embeddings puestos a cero. El desplazamiento de fotogramas derivado de `video_latent` determina dónde comienzan los nuevos fotogramas en la secuencia de audio. Si la secuencia de audio no contiene suficientes fotogramas para cubrir la extensión solicitada, no se aplica condicionamiento de audio.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `positive` | Condicionamiento positivo procesado con contexto de video aplicado, incluyendo embeddings de audio, latents de referencia, movimiento de referencia y video de control si se proporciona | CONDITIONING |
| `negative` | Condicionamiento negativo procesado con contexto de video aplicado, incluyendo embeddings de audio (puestos a cero), latents de referencia, movimiento de referencia y video de control si se proporciona | CONDITIONING |
| `latent` | Representación latent de video generada que contiene la secuencia de video extendida, inicializada como ceros con dimensiones derivadas del `video_latent` de entrada y la `length` objetivo | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/es.md)

---
**Source fingerprint (SHA-256):** `32b58aaba566f346a0388ba804fc92e7ad426bf2e9e7039e5fdb0bf6a746e972`
