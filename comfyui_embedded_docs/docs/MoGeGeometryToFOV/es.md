# MoGeGeometryToFOV

Este nodo calcula el campo de visión y la distancia focal a partir de los parámetros intrínsecos de la cámara almacenados en un objeto de geometría MoGe. Puede devolver el FOV vertical, horizontal o diagonal, en grados o radianes. La salida de FOV vertical puede usarse, por ejemplo, para alimentar el nodo SAM3DBody_Predict.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `moge_geometry` | El objeto de geometría MoGe. Debe contener una matriz de intrínsecos y al menos uno de los siguientes datos: imagen, puntos o profundidad, que se utiliza para leer la altura en píxeles y realizar la conversión de distancia focal. | MOGE_GEOMETRY | Sí | — |
| `eje` | El eje a lo largo del cual se calcula el FOV: "vertical" (fov_y), "horizontal" (fov_x) o "diagonal" (predeterminado: "vertical"). | COMBO | Sí | "vertical"<br>"horizontal"<br>"diagonal" |
| `unidad` | Unidad de salida para el FOV (predeterminado: "degrees"). | COMBO | Sí | "degrees"<br>"radians" |

Nota: El nodo genera un error si `moge_geometry` no contiene intrínsecos (la geometría panorámica no tiene) o si no contiene datos de imagen, puntos ni profundidad.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `fov` | El campo de visión a lo largo del eje seleccionado, en la unidad seleccionada (grados o radianes). | FLOAT |
| `focal_pixels` | La distancia focal del objetivo en píxeles, calculada a partir del intrínseco vertical y la altura en píxeles. | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeGeometryToFOV/es.md)

---
**Source fingerprint (SHA-256):** `983dc984847f93a8e002c73982571ecb38b7bae9c3dc4c201d9be17f785dcaed`
