> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageUpscaleWithModel/es.md)

Este nodo está diseñado para escalar imágenes utilizando un modelo de escalado específico. Gestiona eficientemente el proceso de escalado ajustando la imagen al dispositivo adecuado, optimizando el uso de memoria y aplicando el modelo de escalado en mosaicos para evitar posibles errores de memoria insuficiente.

## Entradas

| Parámetro         | Tipo Comfy        | Descripción                                                                 |
|-------------------|-------------------|----------------------------------------------------------------------------|
| `modelo_ampliacion`   | `UPSCALE_MODEL`   | El modelo de escalado que se utilizará para escalar la imagen. Es fundamental para definir el algoritmo de escalado y sus parámetros. |
| `imagen`           | `IMAGE`           | La imagen que se va a escalar. Esta entrada es esencial para determinar el contenido de origen que se someterá al proceso de escalado. |

## Salidas

| Parámetro | Tipo de Dato | Descripción                                        |
|-----------|-------------|----------------------------------------------------|
| `imagen`   | `IMAGE`     | La imagen escalada, procesada por el modelo de escalado. Esta salida es el resultado de la operación de escalado, mostrando la resolución o calidad mejorada. |