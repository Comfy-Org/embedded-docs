# RenderUVAtlas

Renderiza el diseño UV de una malla como imagen. Cada región UV conectada (chart) se rellena con un color distinto, y los límites de los charts se delinean en negro sobre un fondo gris oscuro.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `mesh` | La malla 3D cuyo diseño UV se renderizará. La malla debe tener coordenadas UV; de lo contrario, se genera un error. | MESH | Sí | - |
| `resolution` | El ancho y alto, en píxeles, de la imagen renderizada (valor por defecto: 1024). | INT | Sí | 64 a 4096 (step 64) |

Nota: Si la malla no tiene coordenadas UV, el nodo genera el error "mesh has no UVs to render. Run UnwrapMesh first." Si la malla contiene una dimensión de lote (UV 3D o matrices de caras), solo se renderiza el primer elemento del lote.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La imagen del atlas UV renderizada, con cada chart coloreado y los bordes de los límites de los charts delineados en negro. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderUVAtlas/es.md)

---
**Source fingerprint (SHA-256):** `b462101036418350390ffed621e583c6de14d5ea34d1e427342dc44ec3fd1922`
