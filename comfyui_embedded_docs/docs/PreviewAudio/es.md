# Vista previa de audio

El nodo Preview Audio crea una vista previa de audio temporal que se puede reproducir directamente en la interfaz, sin guardar el audio en el directorio de salida de ComfyUI. Toma datos de audio como entrada y genera un widget de vista previa, lo que permite a los usuarios escuchar las salidas de audio sin guardar archivos permanentes.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `audio` | Los datos de audio para previsualizar. Este nodo generará un error si el audio de entrada es None, lo que puede ocurrir cuando el video de origen no tiene pista de audio. | AUDIO | Sí | - |

**Nota:** Si el `audio` de entrada es None, el nodo genera un ValueError. Esto puede ocurrir cuando el video de origen no tiene pista de audio.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `audio` | Los datos de audio pasados desde la entrada, utilizados para la vista previa. | AUDIO |
| `ui` | Muestra un widget de reproducción de audio en la interfaz para previsualizar el audio. | UI |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/es.md)

---
**Source fingerprint (SHA-256):** `ccbf9873a16bf1578fe25d178454d782f4f9b37ad5721721bef0aee3ff374f9f`
