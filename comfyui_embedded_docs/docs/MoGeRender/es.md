# MoGe Renderizado

## Resumen

Este nodo toma un paquete MOGE_GEOMETRY (producido por un nodo de estimación de profundidad/normales MoGe) y lo renderiza a un formato de imagen estándar. Puede elegir generar un mapa de profundidad, un mapa de profundidad con color, un mapa de normales o una máscara.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `moge_geometry` | El paquete de datos geométricos de un nodo de estimación MoGe. | MOGE_GEOMETRY | Sí | N/A |
| `output` | El tipo de imagen a renderizar a partir de los datos geométricos. `depth` genera un mapa de profundidad en escala de grises, `depth_colored` genera un mapa de profundidad con color, `normal_opengl` y `normal_directx` generan mapas de normales, y `mask` genera una máscara. La diferencia entre DirectX y OpenGL controla la convención del canal verde del mapa de normales. DirectX: verde = -Y hacia abajo (Unreal). OpenGL: verde = +Y hacia arriba (Blender, Substance, Unity, glTF). (predeterminado: "depth") | COMBO | Sí | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` |

**Nota:** El paquete de geometría debe contener datos que coincidan con el modo `output` elegido. Los modos `depth` y `depth_colored` requieren datos de profundidad en el paquete. Los modos `normal_opengl` y `normal_directx` requieren datos de normales, o datos de puntos a partir de los cuales se derivan las normales. El modo `mask` requiere datos de máscara. Si faltan los datos requeridos, el nodo genera un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `IMAGE` | La imagen renderizada como un lote de tensores RGB. El contenido depende del modo `output`: un mapa de profundidad en escala de grises, un mapa de profundidad con color, un mapa de normales o una máscara convertida a RGB. El tamaño del lote de salida coincide con el tamaño del lote de geometría de entrada. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/es.md)

---
**Source fingerprint (SHA-256):** `ca602f7a7d6eb1b1d00986459621d94ecf9331266ff1d3ce7bb759d24448a346`
