# Descripción General

Este nodo toma un paquete MOGE_GEOMETRY (generado por un nodo de estimación de profundidad/normales MoGe) y lo renderiza en un formato de imagen estándar. Puedes elegir generar un mapa de profundidad, un mapa de profundidad coloreado, un mapa de normales o una máscara.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `moge_geometry` | El paquete de datos geométricos proveniente de un nodo de estimación MoGe. | MOGE_GEOMETRY | Sí | N/A |
| `output` | El tipo de imagen a renderizar a partir de los datos geométricos. DirectX vs OpenGL controla la convención del canal verde del mapa de normales. DirectX: verde = -Y hacia abajo (Unreal). OpenGL: verde = +Y hacia arriba (Blender, Substance, Unity, glTF). (valor predeterminado: "depth") | COMBO | Sí | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `IMAGE` | La imagen renderizada como un lote de tensores RGB. El contenido depende del modo de `output`: un mapa de profundidad en escala de grises, un mapa de profundidad coloreado, un mapa de normales o una máscara. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/es.md)

---
**Source fingerprint (SHA-256):** `45ba499e746ce46f9b6f7773e3218bcf80ad2e8d65940b38e248cc2f20c8b2fe`
