# OrientaciónTriangularCFGVideo

El nodo VideoTriangleCFGGuidance aplica un patrón de escalado de guía sin clasificador triangular a los modelos de video. Modifica la escala de condicionamiento a lo largo del tiempo mediante una función de onda triangular que oscila entre el valor mínimo de CFG y la escala de condicionamiento original. Esto crea un patrón de guía dinámico que puede ayudar a mejorar la consistencia y la calidad de la generación de video.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de video al que se aplicará la guía CFG triangular | MODEL | Sí | - |
| `min_cfg` | El valor mínimo de escala CFG para el patrón triangular (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 100.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo modificado con la guía CFG triangular aplicada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/es.md)

---
**Source fingerprint (SHA-256):** `412d84d402f8c9a4852ee7b3f0ca0ab5650658fc26a37d10333a653e92e0294e`
