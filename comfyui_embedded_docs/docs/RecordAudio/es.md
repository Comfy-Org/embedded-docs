> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecordAudio/es.md)

El nodo `RecordAudio` carga archivos de audio que han sido grabados o seleccionados a través de la interfaz de grabación de audio. Procesa el archivo de audio y lo convierte en un formato de forma de onda que puede ser utilizado por otros nodos de procesamiento de audio en el flujo de trabajo. El nodo detecta automáticamente la frecuencia de muestreo y prepara los datos de audio para su posterior manipulación.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `audio` | AUDIO_RECORD | Sí | N/A | La entrada de grabación de audio proveniente de la interfaz de grabación de audio |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `AUDIO` | AUDIO | Los datos de audio procesados que contienen información de forma de onda y frecuencia de muestreo |

---
**Source fingerprint (SHA-256):** `3648f3c71f60f69e9ca117e25e9706187470866a1869ba9b8e5feceb42a7493a`
