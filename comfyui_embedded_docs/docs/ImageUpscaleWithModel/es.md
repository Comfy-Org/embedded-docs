Este nodo está diseñado para ampliar imágenes utilizando un modelo de ampliación especificado. Maneja el proceso de ampliación ajustando la imagen al dispositivo adecuado, gestionando la memoria de manera eficiente y aplicando el modelo de ampliación de manera segmentada para evitar posibles errores de falta de memoria.

## Entradas

| Parámetro         | Comfy dtype       | Descripción                                                                 |
|-------------------|-------------------|----------------------------------------------------------------------------|
| `upscale_model`   | `UPSCALE_MODEL`   | El modelo de ampliación que se utilizará para ampliar la imagen. Es crucial para definir el algoritmo de ampliación y sus parámetros. |
| `image`           | `IMAGE`           | La imagen que se va a ampliar. Esta entrada es esencial para determinar el contenido fuente que se someterá al proceso de ampliación. |

## Salidas

| Parámetro | Data Type | Descripción                                        |
|-----------|-------------|----------------------------------------------------|
| `image`   | `IMAGE`     | La imagen ampliada, procesada por el modelo de ampliación. Esta salida es el resultado de la operación de ampliación, mostrando la resolución o calidad mejorada. |
