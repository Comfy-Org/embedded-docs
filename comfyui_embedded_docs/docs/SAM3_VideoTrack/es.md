# SAM3 Video Track

Rastrea objetos a través de fotogramas de video utilizando el rastreador basado en memoria de SAM3. Este nodo procesa una secuencia de fotogramas de video y mantiene identidades de objetos a lo largo de los fotogramas, usando máscaras iniciales o indicaciones de texto para definir qué rastrear.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `imágenes` | Fotogramas de video como imágenes por lotes | IMAGE | Sí | Fotogramas de video por lotes |
| `modelo` | El modelo SAM3 a utilizar para el seguimiento | MODEL | Sí | Modelo SAM3 |
| `máscara_inicial` | Máscara(s) del primer fotograma para rastrear (una por objeto) | MASK | No | Una máscara por objeto |
| `condicionamiento` | Condicionamiento de texto para detectar nuevos objetos durante el seguimiento | CONDITIONING | No | Condicionamiento de texto |
| `umbral_de_detección` | Umbral de puntuación para la detección mediante indicaciones de texto (predeterminado: 0.5) | FLOAT | No | 0.0 a 1.0 |
| `máx_objetos` | Máximo de objetos rastreados. Las máscaras iniciales cuentan para este límite. 0 usa el límite interno de 64. (predeterminado: 4) | INT | No | 0 a 64 |
| `intervalo_de_detección` | Ejecutar la detección cada N fotogramas (1=todos los fotogramas). Los valores más altos ahorran cómputo. (predeterminado: 1) | INT | No | 1 o superior |

**Nota:** Debe proporcionarse `initial_mask` o `conditioning`. Si se omiten ambos, el nodo genera un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `datos_de_rastreo` | Datos de seguimiento que contienen máscaras de objetos y metadatos de todos los fotogramas del video | SAM3TrackData |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/es.md)

---
**Source fingerprint (SHA-256):** `ef584628b334997a001a857a7deffb7eda34db8fa50e3d734a07b5e92566d48d`
