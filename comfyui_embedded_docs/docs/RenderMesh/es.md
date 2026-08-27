# RenderMesh

Este nodo renderiza una malla 3D en una imagen 2D mediante el trazado de rayos de una sola vista. Puede generar la malla texturizada, colores de vértices, una superficie sombreada sólida, normales de superficie o profundidad. La cámara y la transformación opcional del modelo pueden provenir de un visor Load3D / Preview3D; si no hay ninguna cámara conectada, se encuadra automáticamente una vista frontal predeterminada.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `mesh` | La malla 3D a renderizar. | MESH | Sí | — |
| `mode` | Qué renderizar. auto: textura si está presente; si no, colores de vértices; si no, arcilla sombreada. (por defecto: "auto") | COMBO | Sí | `"auto"`<br>`"texture"`<br>`"vertex colors"`<br>`"solid"`<br>`"normal"`<br>`"depth"` |
| `width` | Ancho de la imagen renderizada en píxeles. (por defecto: 1024) | INT | Sí | 64 a 4096 (paso 8) |
| `height` | Alto de la imagen renderizada en píxeles. (por defecto: 1024) | INT | Sí | 64 a 4096 (paso 8) |
| `background` | Color de fondo usado para los píxeles que la malla no cubre. (por defecto: "#000000") | COLOR | Sí | — |
| `model_3d_info` | Transformación del modelo desde el mismo visor Load3D / Preview3D. Conéctalo con `camera_info` para que coincida con el encuadre del visor. | LOAD3D_MODEL_INFO | No | — |
| `camera_info` | Cámara de un visor Load3D / Preview3D o de un nodo Create Camera Info. Si no se conecta ninguna, se encuadra automáticamente una vista frontal predeterminada. | LOAD3D_CAMERA | No | — |

Nota: Solo se renderiza el primer elemento de una malla en lote; si el lote de mallas contiene más de un elemento, el nodo registra una advertencia y usa el primero. El modo `texture` requiere que la malla tenga tanto textura como UVs, y el modo `vertex colors` requiere colores de vértices; si los datos del modo seleccionado no están disponibles, el nodo recurre al renderizado sombreado sólido. `model_3d_info` y `camera_info` están pensados para conectarse juntos desde el mismo visor Load3D / Preview3D para que el renderizado coincida con el encuadre del visor.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La imagen renderizada de la malla. | IMAGE |
| `mask` | Una máscara que es 1.0 donde se renderizó la malla y 0.0 en el resto. | MASK |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderMesh/es.md)

---
**Source fingerprint (SHA-256):** `d23e85a904520eb2dfed899eb3e6a9cf45c980df00c034503687ac4eccc66ac4`
