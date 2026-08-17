# Vista previa de audio

El nodo PreviewAudio te permite previsualizar audio directamente en la interfaz sin guardarlo en el directorio de salida de ComfyUI. Toma datos de audio como entrada y muestra un widget de reproductor de audio que puedes usar para escuchar el resultado. Si el audio de entrada es None, el nodo genera un error, lo que puede ocurrir cuando el video de origen no tiene pista de audio.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `audio` | Los datos de audio para previsualizar. El nodo genera un error si el audio es None, lo que puede ocurrir cuando el video de origen no tiene pista de audio. | AUDIO | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `audio` | Los datos de audio que se pasaron a través del nodo. Se muestra un widget de reproductor de audio en la interfaz para previsualizar el audio. | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/es.md)

---
**Source fingerprint (SHA-256):** `ccbf9873a16bf1578fe25d178454d782f4f9b37ad5721721bef0aee3ff374f9f`
