# SAM3 Video Track

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/en.md)

## Resumen

Rastrea objetos a través de fotogramas de video utilizando el rastreador basado en memoria de SAM3. Este nodo procesa una secuencia de fotogramas de video y mantiene las identidades de los objetos a lo largo de los fotogramas, utilizando máscaras iniciales o indicaciones de texto para definir qué rastrear.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imágenes` | Fotogramas de video como imágenes por lotes | IMAGE | Sí | Fotogramas de video por lotes |
| `modelo` | El modelo SAM3 a utilizar para el rastreo | MODEL | Sí | Modelo SAM3 |
| `máscara_inicial` | Máscara(s) para el primer fotograma a rastrear (una por objeto). Obligatorio si no se proporciona `condicionamiento`. | MASK | No | Una máscara por objeto |
| `condicionamiento` | Condicionamiento de texto para detectar nuevos objetos durante el rastreo. Obligatorio si no se proporciona `máscara_inicial`. | CONDITIONING | No | Condicionamiento de texto |
| `umbral_de_detección` | Umbral de puntuación para la detección mediante indicaciones de texto | FLOAT | No | 0.0 a 1.0 (predeterminado: 0.5) |
| `máx_objetos` | Máximo de objetos rastreados. Las máscaras iniciales cuentan para este límite. 0 usa el límite interno de 64. | INT | No | 0 a 64 (predeterminado: 0) |
| `intervalo_de_detección` | Ejecutar detección cada N fotogramas (1=cada fotograma). Los valores más altos ahorran cómputo. | INT | No | 1 a ilimitado (predeterminado: 1) |

**Nota:** Se debe proporcionar `initial_mask` o `conditioning`. Si se omiten ambos, el nodo generará un error.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `track_data` | Datos de rastreo que contienen las máscaras de objetos y metadatos en todos los fotogramas de video | SAM3TrackData |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/es.md)

---
**Source fingerprint (SHA-256):** `30768bdf5839c1d7b984675e68a127a27f21b17724a2dc885e27f00c272db3cb`
