# MoGe Renderizado

## Descripción general

Este nodo toma un paquete `MOGE_GEOMETRY` (producido por un nodo de estimación de profundidad/normales MoGe) y lo renderiza en un formato de imagen estándar. Puedes elegir generar un mapa de profundidad, un mapa de profundidad coloreado, un mapa de normales o una máscara.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `moge_geometry` | El paquete de datos de geometría de un nodo de estimación MoGe. | `MOGE_GEOMETRY` | Sí | N/A |
| `output` | El tipo de imagen a renderizar a partir de los datos de geometría. DirectX vs OpenGL controla la convención del canal verde del mapa de normales. DirectX: verde = -Y hacia abajo (Unreal). OpenGL: verde = +Y hacia arriba (Blender, Substance, Unity, glTF). (valor predeterminado: "depth") | `COMBO` | Sí | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` |

**Nota:** El modo `output` seleccionado determina qué datos deben estar presentes en `moge_geometry`:
- `depth` y `depth_colored` requieren datos de profundidad. La profundidad se convierte en un mapa de disparidad normalizada (1/profundidad) mediante recorte por percentiles 0.1/99.9.
- `normal_opengl` y `normal_directx` requieren datos de normales, o datos de puntos a partir de los cuales se puedan derivar las normales. El nodo genera un error si no hay ninguno de los dos.
- `mask` requiere datos de máscara.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `IMAGE` | La imagen renderizada como un lote de tensores RGB. El contenido depende del modo `output`: un mapa de profundidad en escala de grises, un mapa de profundidad coloreado, un mapa de normales o una máscara. | `IMAGE` |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/es.md)

---
**Source fingerprint (SHA-256):** `ca602f7a7d6eb1b1d00986459621d94ecf9331266ff1d3ce7bb759d24448a346`
