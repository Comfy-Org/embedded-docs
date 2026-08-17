# IncrustaciónCámaraWan

El nodo WanCameraEmbedding genera embeddings de trayectoria de cámara utilizando embeddings de Plücker basados en parámetros de movimiento de cámara. Crea una secuencia de poses de cámara que simulan diferentes movimientos de cámara y convierte dicha secuencia en tensores de embedding adecuados para pipelines de generación de video.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `camera_pose` | El tipo de movimiento de cámara a simular (predeterminado: "Static") | COMBO | Sí | "Static"<br>"Pan Up"<br>"Pan Down"<br>"Pan Left"<br>"Pan Right"<br>"Zoom In"<br>"Zoom Out"<br>"Anti Clockwise (ACW)"<br>"ClockWise (CW)" |
| `width` | El ancho de la salida en píxeles (predeterminado: 832, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `height` | El alto de la salida en píxeles (predeterminado: 480, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `length` | La longitud de la secuencia de trayectoria de cámara (predeterminado: 81, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `speed` | La velocidad del movimiento de cámara (predeterminado: 1.0, paso: 0.1) | FLOAT | No | 0.0 a 10.0 |
| `fx` | El parámetro de distancia focal x (predeterminado: 0.5, paso: 0.000000001) | FLOAT | No | 0.0 a 1.0 |
| `fy` | El parámetro de distancia focal y (predeterminado: 0.5, paso: 0.000000001) | FLOAT | No | 0.0 a 1.0 |
| `cx` | La coordenada x del punto principal (predeterminado: 0.5, paso: 0.01) | FLOAT | No | 0.0 a 1.0 |
| `cy` | La coordenada y del punto principal (predeterminado: 0.5, paso: 0.01) | FLOAT | No | 0.0 a 1.0 |

Nota: `fx`, `fy`, `cx` y `cy` son parámetros avanzados. El parámetro `length` usa un paso de 4 porque el primer fotograma de cámara se repite internamente, por lo que la longitud efectiva de la secuencia procesada se convierte en `length + 3`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `camera_embedding` | El tensor de embedding de cámara generado que contiene la secuencia de trayectoria | TENSOR |
| `width` | El valor de ancho que se usó para el procesamiento | INT |
| `height` | El valor de alto que se usó para el procesamiento | INT |
| `length` | El valor de longitud que se usó para el procesamiento | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/es.md)

---
**Source fingerprint (SHA-256):** `1a2f98d83d18033581823dee61b5a3686d560c749c55223f81febca89654a29f`
