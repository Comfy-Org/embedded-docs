# VideoCrop

Este nodo recorta un video a una región rectangular seleccionada, conservando solo la parte dentro de ese rectángulo. También crea una vista previa del video recortado para que puedas ver el resultado. Si el ancho y el alto del recorte son cero, se conserva el video completo sin cambios.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `video` | El video fuente que se recortará. | VIDEO | Sí | Cualquier video |
| `crop` | Región de recorte en píxeles. Un ancho/alto de cero conserva el fotograma completo. El rectángulo de recorte proporciona los valores `x`, `y`, `width` y `height`, todos con un valor predeterminado de 0. | VIDEO_EDIT | Sí | `x` ≥ 0<br>`y` ≥ 0<br>`width` ≥ 0<br>`height` ≥ 0<br>Todos los valores tienen un valor predeterminado de 0 |

Nota: La región de recorte se describe en coordenadas de píxeles. Cuando el ancho y el alto son 0, no se aplica ningún recorte y el nodo emite el video de entrada completo.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `video` | El video recortado a la región rectangular seleccionada. Cuando el ancho y el alto del recorte son 0, la salida es el video de entrada completo. El resultado recortado también se guarda como un archivo MP4 temporal y se muestra como una vista previa de video. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoCrop/es.md)

---
**Source fingerprint (SHA-256):** `0c4ebd51027669fc232fe42a5e8840b5e4e95083b6794cd7b4c43123ddc0341b`
