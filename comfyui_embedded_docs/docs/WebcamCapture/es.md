> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WebcamCapture/es.md)

El nodo WebcamCapture captura imágenes desde un dispositivo de cámara web y las convierte a un formato que puede utilizarse dentro de los flujos de trabajo de ComfyUI. Hereda del nodo LoadImage y proporciona opciones para controlar las dimensiones y el momento de la captura. Cuando está habilitado, el nodo puede capturar nuevas imágenes cada vez que se procesa la cola de trabajo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen` | WEBCAM | Sí | - | La fuente de entrada de la cámara web desde la cual capturar imágenes |
| `ancho` | INT | No | 0 a MAX_RESOLUTION | El ancho deseado para la imagen capturada (por defecto: 0, usa la resolución nativa de la cámara web) |
| `altura` | INT | No | 0 a MAX_RESOLUTION | La altura deseada para la imagen capturada (por defecto: 0, usa la resolución nativa de la cámara web) |
| `captura_en_cola` | BOOLEAN | No | - | Cuando está habilitado, captura una nueva imagen cada vez que se procesa la cola de trabajo (por defecto: True) |

**Nota:** Cuando tanto `width` como `height` están establecidos en 0, el nodo utiliza la resolución nativa de la cámara web. Establecer cualquier dimensión a un valor distinto de cero redimensionará la imagen capturada en consecuencia.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | La imagen de la cámara web capturada convertida al formato de imagen de ComfyUI |
