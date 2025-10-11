> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadAudio/es.md)

El nodo LoadAudio carga archivos de audio desde el directorio de entrada y los convierte a un formato que puede ser procesado por otros nodos de audio en ComfyUI. Lee archivos de audio y extrae tanto los datos de la forma de onda como la frecuencia de muestreo, haciéndolos disponibles para tareas posteriores de procesamiento de audio.

## Entradas

| Parámetro | Tipo de Datos | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Sí | Todos los archivos de audio/video compatibles en el directorio de entrada | El archivo de audio a cargar desde el directorio de entrada |

**Nota:** El nodo solo acepta archivos de audio y video que estén presentes en el directorio de entrada de ComfyUI. El archivo debe existir y ser accesible para una carga exitosa.

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | Datos de audio que contienen información de la forma de onda y frecuencia de muestreo |