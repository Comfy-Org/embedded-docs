# Acondicionamiento Audio Estable

El nodo ConditioningStableAudio añade información de sincronización temporal a las entradas de condicionamiento positivo y negativo para la generación de audio. Establece los parámetros de tiempo de inicio y duración total que ayudan a controlar cuándo y durante cuánto tiempo debe generarse el contenido de audio. Este nodo modifica los datos de condicionamiento existentes añadiendo metadatos de sincronización específicos de audio.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positive` | La entrada de condicionamiento positivo que se modificará con la información de sincronización temporal de audio | CONDITIONING | Sí | - |
| `negative` | La entrada de condicionamiento negativo que se modificará con la información de sincronización temporal de audio | CONDITIONING | Sí | - |
| `seconds_start` | El tiempo de inicio en segundos para la generación de audio (por defecto: 0.0) | FLOAT | Sí | 0.0 to 1000.0 |
| `seconds_total` | La duración total en segundos para la generación de audio (por defecto: 47.0) | FLOAT | Sí | 0.0 to 1000.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | El condicionamiento positivo modificado con la información de sincronización temporal de audio aplicada | CONDITIONING |
| `negative` | El condicionamiento negativo modificado con la información de sincronización temporal de audio aplicada | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/es.md)

---
**Source fingerprint (SHA-256):** `8bdf29514002837090c549b9921e8cb19c07d385881fe09a58885fcbfe968261`
