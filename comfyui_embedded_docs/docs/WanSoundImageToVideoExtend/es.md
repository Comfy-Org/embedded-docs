El nodo WanSoundImageToVideoExtend extiende un latente de video existente generando fotogramas adicionales, guiado opcionalmente por audio, una imagen de referencia y un video de control. Toma un latente de video inicial y produce una secuencia de video más larga, utilizando las condiciones y señales de audio proporcionadas para influir en el nuevo contenido.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Condicionamientos positivos que guían lo que el video debe incluir | CONDITIONING | Sí | - |
| `negativo` | Condicionamientos negativos que especifican lo que el video debe evitar | CONDITIONING | Sí | - |
| `vae` | Autoencoder variacional utilizado para codificar y decodificar fotogramas de video | VAE | Sí | - |
| `longitud` | Número total de fotogramas a generar para la secuencia de video (predeterminado: 77, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `video_latente` | Representación latente de video inicial que sirve como punto de partida para la extensión | LATENT | Sí | - |
| `salida_codificador_audio` | Incrustaciones de audio opcionales que pueden influir en la generación de video según las características del sonido | AUDIOENCODEROUTPUT | No | - |
| `imagen_ref` | Imagen de referencia opcional que proporciona guía visual para la generación del video | IMAGE | No | - |
| `video_control` | Video de control opcional que puede guiar el movimiento y el estilo del video generado | IMAGE | No | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `positivo` | Condicionamiento positivo procesado con contexto de video aplicado | CONDITIONING |
| `negativo` | Condicionamiento negativo procesado con contexto de video aplicado | CONDITIONING |
| `latente` | Representación latente de video generada que contiene la secuencia de video extendida | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/es.md)

---
**Source fingerprint (SHA-256):** `fc9aee5d51e96b864da7d75f592f07691be8b970346998b209b3ad8a72308ecb`
