# IncrustaciónCámaraWan

El nodo WanCameraEmbedding genera embeddings de trayectoria de cámara utilizando embeddings de Plücker basados en parámetros de movimiento de cámara. Crea una secuencia de poses de cámara que simulan diferentes movimientos de cámara y los convierte en tensores de embedding adecuados para pipelines de generación de video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `pose_cámara` | El tipo de movimiento de cámara a simular (predeterminado: "Static") | COMBO | Sí | "Static"<br>"Pan Up"<br>"Pan Down"<br>"Pan Left"<br>"Pan Right"<br>"Zoom In"<br>"Zoom Out"<br>"Anti Clockwise (ACW)"<br>"ClockWise (CW)" |
| `ancho` | El ancho de la salida en píxeles (predeterminado: 832, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `alto` | La altura de la salida en píxeles (predeterminado: 480, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `longitud` | La longitud de la secuencia de trayectoria de cámara (predeterminado: 81, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `velocidad` | La velocidad del movimiento de cámara (predeterminado: 1.0, paso: 0.1) | FLOAT | No | 0.0 a 10.0 |
| `fx` | El parámetro de distancia focal x (predeterminado: 0.5, paso: 0.000000001) | FLOAT | No | 0.0 a 1.0 |
| `fy` | El parámetro de distancia focal y (predeterminado: 0.5, paso: 0.000000001) | FLOAT | No | 0.0 a 1.0 |
| `cx` | La coordenada x del punto principal (predeterminado: 0.5, paso: 0.01) | FLOAT | No | 0.0 a 1.0 |
| `cy` | La coordenada y del punto principal (predeterminado: 0.5, paso: 0.01) | FLOAT | No | 0.0 a 1.0 |


| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `camera_embedding` | El tensor de embedding de cámara generado que contiene la secuencia de trayectoria | TENSOR |
| `width` | El valor de ancho que se utilizó para el procesamiento | INT |
| `height` | El valor de altura que se utilizó para el procesamiento | INT |
| `length` | El valor de longitud que se utilizó para el procesamiento | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/es.md)

---
**Source fingerprint (SHA-256):** `422c4a1fdfb6fd403afac26a609f80cbdbaa87f2c115068de9d7a33c756e71fd`
