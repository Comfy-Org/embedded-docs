# ElevenLabs Texto a Efectos de Sonido

El nodo ElevenLabs Text to Sound Effects genera audio de efectos de sonido a partir de una descripción de texto mediante la API de ElevenLabs. Envía tu indicación escrita al servicio de generación de sonidos de ElevenLabs y devuelve el audio resultante, con controles para la duración, el comportamiento de bucle y la fidelidad con la que el sonido sigue el texto.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `modelo` | Modelo a utilizar para la generación de efectos de sonido. El modelo seleccionado determina los parámetros de generación disponibles que se enumeran a continuación. | DYNAMIC_COMBO | Sí | `"eleven_sfx_v2"` |
| `texto` | Descripción de texto del efecto de sonido a generar. Debe contener al menos 1 carácter. (predeterminado: vacío) | STRING | Sí | N/A |
| `formato_de_salida` | Formato de salida de audio. | COMBO | Sí | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Eleven SFX v2 Entradas

Subparámetros que se muestran cuando `model` está configurado en `"eleven_sfx_v2"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `duration` | Duración del sonido generado en segundos. (predeterminado: 5.0) | FLOAT | Sí | 0.5 a 30.0 (paso: 0.1) |
| `loop` | Crea un efecto de sonido con bucle suave. (predeterminado: False) | BOOLEAN | No | True o False |
| `prompt_influence` | Qué tan de cerca sigue la generación la indicación. Los valores más altos hacen que el sonido siga el texto más de cerca. (predeterminado: 0.3) | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `audio` | El archivo de audio del efecto de sonido generado. | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/es.md)

---
**Source fingerprint (SHA-256):** `218ff617256cea33f310c1bcfc6407c46aaadc59201a0324b0ec64583166ce58`
