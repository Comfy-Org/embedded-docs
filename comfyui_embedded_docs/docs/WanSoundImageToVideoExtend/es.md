> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/es.md)

El nodo WanSoundImageToVideoExtend extiende un latente de video existente generando fotogramas adicionales, guiado opcionalmente por audio, una imagen de referencia y un video de control. Toma un latente de video inicial y produce una secuencia de video más larga, utilizando las condiciones y señales de audio proporcionadas para influir en el nuevo contenido.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `positivo` | CONDITIONING | Sí | - | Condicionamientos positivos que guían lo que el video debe incluir |
| `negativo` | CONDITIONING | Sí | - | Condicionamientos negativos que especifican lo que el video debe evitar |
| `vae` | VAE | Sí | - | Autoencoder variacional utilizado para codificar y decodificar fotogramas de video |
| `longitud` | INT | Sí | 1 a MAX_RESOLUTION | Número total de fotogramas a generar para la secuencia de video (predeterminado: 77, paso: 4) |
| `video_latente` | LATENT | Sí | - | Representación latente de video inicial que sirve como punto de partida para la extensión |
| `salida_codificador_audio` | AUDIOENCODEROUTPUT | No | - | Incrustaciones de audio opcionales que pueden influir en la generación de video según las características del sonido |
| `imagen_ref` | IMAGE | No | - | Imagen de referencia opcional que proporciona guía visual para la generación del video |
| `video_control` | IMAGE | No | - | Video de control opcional que puede guiar el movimiento y el estilo del video generado |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `negativo` | CONDITIONING | Condicionamiento positivo procesado con contexto de video aplicado |
| `latente` | CONDITIONING | Condicionamiento negativo procesado con contexto de video aplicado |
| `latent` | LATENT | Representación latente de video generada que contiene la secuencia de video extendida |

---
**Source fingerprint (SHA-256):** `fc9aee5d51e96b864da7d75f592f07691be8b970346998b209b3ad8a72308ecb`
