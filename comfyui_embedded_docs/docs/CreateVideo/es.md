# Crear video

El nodo Create Video genera un archivo de video a partir de una secuencia de imágenes. Puedes ajustar la velocidad de reproducción en fotogramas por segundo, agregar audio opcionalmente y elegir la profundidad de bits y el espacio de color del video resultante.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `imágenes` | Las imágenes a partir de las cuales se crea el video. | IMAGE | Sí | - |
| `fps` | Los fotogramas por segundo para la velocidad de reproducción del video (predeterminado: 30.0). | FLOAT | Sí | 1.0 - 120.0 |
| `audio` | El audio que se agregará al video. | AUDIO | No | - |
| `bit_depth` | Auto usa 8 bits para sRGB y 10 bits para HDR. Las opciones explícitas de 8 bits y 10 bits son independientes del espacio de color. (predeterminado: "auto") | COMBO | No | `"auto"`<br>8<br>10 |
| `color_space` | Espacio de color de las imágenes de entrada. HDR selecciona BT.2020/HLG y HDR PQ selecciona BT.2020/PQ. (predeterminado: "sRGB") | COMBO | No | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

Nota: Cuando `bit_depth` se establece en "auto", el nodo usa 10 bits para los espacios de color HDR y HDR PQ, y 8 bits para sRGB.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | El video generado que contiene las imágenes de entrada y el audio opcional. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/es.md)

---
**Source fingerprint (SHA-256):** `2fa73f38b0609de4159e557b6abe73652c5bebab9d34ffdda743b0eac6049f13`
