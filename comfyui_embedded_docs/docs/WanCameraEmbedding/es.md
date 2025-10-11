> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/es.md)

El nodo WanCameraEmbedding genera incrustaciones de trayectoria de cámara utilizando incrustaciones de Plücker basadas en parámetros de movimiento de cámara. Crea una secuencia de poses de cámara que simulan diferentes movimientos de cámara y los convierte en tensores de incrustación adecuados para pipelines de generación de video.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `camera_pose` | COMBO | Sí | "Static"<br>"Pan Up"<br>"Pan Down"<br>"Pan Left"<br>"Pan Right"<br>"Zoom In"<br>"Zoom Out"<br>"Anti Clockwise (ACW)"<br>"ClockWise (CW)" | El tipo de movimiento de cámara a simular (por defecto: "Static") |
| `width` | INT | Sí | 16 a MAX_RESOLUTION | El ancho de la salida en píxeles (por defecto: 832, paso: 16) |
| `height` | INT | Sí | 16 a MAX_RESOLUTION | La altura de la salida en píxeles (por defecto: 480, paso: 16) |
| `length` | INT | Sí | 1 a MAX_RESOLUTION | La longitud de la secuencia de trayectoria de cámara (por defecto: 81, paso: 4) |
| `speed` | FLOAT | No | 0.0 a 10.0 | La velocidad del movimiento de cámara (por defecto: 1.0, paso: 0.1) |
| `fx` | FLOAT | No | 0.0 a 1.0 | El parámetro de distancia focal x (por defecto: 0.5, paso: 0.000000001) |
| `fy` | FLOAT | No | 0.0 a 1.0 | El parámetro de distancia focal y (por defecto: 0.5, paso: 0.000000001) |
| `cx` | FLOAT | No | 0.0 a 1.0 | La coordenada x del punto principal (por defecto: 0.5, paso: 0.01) |
| `cy` | FLOAT | No | 0.0 a 1.0 | La coordenada y del punto principal (por defecto: 0.5, paso: 0.01) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `camera_embedding` | TENSOR | El tensor de incrustación de cámara generado que contiene la secuencia de trayectoria |
| `width` | INT | El valor de ancho que se utilizó para el procesamiento |
| `height` | INT | El valor de altura que se utilizó para el procesamiento |
| `length` | INT | El valor de longitud que se utilizó para el procesamiento |