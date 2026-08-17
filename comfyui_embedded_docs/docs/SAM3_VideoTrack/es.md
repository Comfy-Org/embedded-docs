# SAM3 Video Track

Realiza un seguimiento de objetos a través de los fotogramas de un vídeo utilizando el rastreador basado en memoria de SAM3. Este nodo procesa una secuencia de fotogramas de vídeo y mantiene las identidades de los objetos entre fotogramas, utilizando máscaras iniciales o indicaciones de texto para definir qué rastrear.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `images` | Fotogramas de vídeo como imágenes en lote | IMAGE | Sí | Fotogramas de vídeo en lote |
| `model` | El modelo SAM3 que se utilizará para el seguimiento | MODEL | Sí | Modelo SAM3 |
| `initial_mask` | Máscara(s) para el primer fotograma a rastrear (una por objeto). Obligatorio si no se proporciona `conditioning`. | MASK | No | Una máscara por objeto |
| `conditioning` | Condicionamiento de texto para detectar nuevos objetos durante el seguimiento. Obligatorio si no se proporciona `initial_mask`. | CONDITIONING | No | Condicionamiento de texto |
| `detection_threshold` | Umbral de puntuación para la detección mediante indicaciones de texto (predeterminado: 0.5). | FLOAT | Sí | 0.0 a 1.0 |
| `max_objects` | Número máximo de objetos rastreados. Las máscaras iniciales cuentan para este límite. 0 usa el límite interno de 64 (predeterminado: 4). | INT | Sí | 0 a 64 |
| `detect_interval` | Ejecutar la detección cada N fotogramas (1=cada fotograma). Los valores más altos ahorran cómputo (predeterminado: 1). | INT | Sí | 1 o superior |

**Nota:** Debe proporcionarse `initial_mask` o `conditioning`. Si se omiten ambos, el nodo generará un error. Cuando se proporcionan ambos, las máscaras iniciales definen los objetos a rastrear desde el primer fotograma y las indicaciones de texto detectan objetos adicionales durante el seguimiento.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `track_data` | Datos de seguimiento que contienen máscaras de objetos y metadatos en todos los fotogramas de vídeo, incluidas las dimensiones originales del fotograma. | SAM3_TRACK_DATA |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/es.md)

---
**Source fingerprint (SHA-256):** `ef584628b334997a001a857a7deffb7eda34db8fa50e3d734a07b5e92566d48d`
