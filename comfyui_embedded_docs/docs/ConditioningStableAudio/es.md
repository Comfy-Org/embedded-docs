# Acondicionamiento Audio Estable

El nodo ConditioningStableAudio agrega información de temporización a las entradas de condicionamiento tanto positivas como negativas para la generación de audio. Establece los parámetros de tiempo de inicio y duración total que ayudan a controlar cuándo y durante cuánto tiempo se debe generar el contenido de audio. Este nodo modifica los datos de condicionamiento existentes añadiendo metadatos de temporización específicos de audio.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | La entrada de condicionamiento positivo que se modificará con información de temporización de audio | CONDITIONING | Sí | - |
| `negativo` | La entrada de condicionamiento negativo que se modificará con información de temporización de audio | CONDITIONING | Sí | - |
| `segundos_inicio` | El tiempo de inicio en segundos para la generación de audio (predeterminado: 0.0) | FLOAT | Sí | 0.0 a 1000.0 |
| `segundos_total` | La duración total en segundos para la generación de audio (predeterminado: 47.0) | FLOAT | Sí | 0.0 a 1000.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `positivo` | El condicionamiento positivo modificado con información de temporización de audio aplicada | CONDITIONING |
| `negativo` | El condicionamiento negativo modificado con información de temporización de audio aplicada | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/es.md)

---
**Source fingerprint (SHA-256):** `ad4fdb2ac536e4f9cc23c044a7a63333e3f3530cc782937eaedc1565cc7c5d0e`
