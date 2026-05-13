> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlur/es.md)

El nodo `ImageBlur` aplica un desenfoque gaussiano a una imagen, permitiendo suavizar bordes y reducir detalles y ruido. Proporciona control sobre la intensidad y propagación del desenfoque mediante parámetros.

## Entradas

| Campo          | Tipo de Dato | Descripción                                                                   |
|----------------|--------------|-------------------------------------------------------------------------------|
| `imagen`        | `IMAGE`      | La imagen de entrada que se va a desenfocar. Este es el objetivo principal del efecto de desenfoque. |
| `radio_de_desenfoque`  | `INT`        | Determina el radio del efecto de desenfoque. Un radio mayor produce un desenfoque más pronunciado. |
| `sigma`        | `FLOAT`      | Controla la propagación del desenfoque. Un valor de sigma más alto significa que el desenfoque afectará un área más amplia alrededor de cada píxel. |

## Salidas

| Campo | Tipo de Dato | Descripción                                                              |
|-------|--------------|--------------------------------------------------------------------------|
| `imagen`| `IMAGE`      | La salida es la versión desenfocada de la imagen de entrada, con el grado de desenfoque determinado por los parámetros de entrada. |