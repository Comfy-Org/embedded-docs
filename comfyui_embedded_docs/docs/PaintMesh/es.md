# PaintMesh

PaintMesh toma una malla 3D y un campo de color de vóxeles. Asigna a cada vértice el color del vóxel más cercano en el campo, escribiendo el resultado como colores de vértice en la malla de salida. Si el campo de vóxeles está vacío, la malla se pinta con colores de vértice por defecto en cero (negro).

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `malla` | La malla que se va a pintar. | MESH | Sí | N/A |
| `voxel_colors` | Campo de vóxeles que contiene los datos de color utilizados para pintar. Solo se usan los canales RGB del color base del campo. | VOXEL | Sí | N/A |

Nota: Cuando las coordenadas del campo de vóxeles incluyen un canal de índice de lote y la malla de entrada contiene varios elementos de malla, el nodo aplica los colores por separado a cada elemento de malla del lote. Los colores muestreados se convierten de sRGB a RGB lineal para la malla de salida.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `malla` | La malla pintada con los colores de vértice aplicados. | MESH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PaintMesh/es.md)

---
**Source fingerprint (SHA-256):** `55683bef55b18487ba660fe619d6ec176f786de346be12724751b71901c14116`
