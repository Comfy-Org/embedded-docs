# OrientaciónTriangularCFGVideo

El nodo `VideoTriangleCFGGuidance` aplica un patrón de escala de guía sin clasificador triangular a modelos de video. Modifica la escala de condicionamiento a lo largo del tiempo utilizando una función de onda triangular que oscila entre el valor mínimo de CFG y la escala de condicionamiento original. Esto crea un patrón de guía dinámico que puede ayudar a mejorar la consistencia y calidad de la generación de video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de video al que se aplicará la guía CFG triangular | MODEL | Sí | - |
| `min_cfg` | El valor mínimo de escala CFG para el patrón triangular (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 100.0 |


| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model` | El modelo modificado con la guía CFG triangular aplicada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/es.md)

---
**Source fingerprint (SHA-256):** `0b854d78f32e265b1a4322cb11b231df33e6072611142537e0c8cff4e93db49a`
