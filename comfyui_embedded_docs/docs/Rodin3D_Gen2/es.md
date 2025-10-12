> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen2/es.md)

El nodo Rodin3D_Gen2 genera activos 3D utilizando la API de Rodin. Toma imágenes de entrada y las convierte en modelos 3D con varios tipos de materiales y recuentos de polígonos. El nodo maneja automáticamente todo el proceso de generación, incluyendo la creación de tareas, la verificación de estado y la descarga de archivos.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | Sí | - | Imágenes de entrada para usar en la generación del modelo 3D |
| `Seed` | INT | No | 0-65535 | Valor de semilla aleatoria para la generación (por defecto: 0) |
| `Material_Type` | COMBO | No | "PBR"<br>"Shaded" | Tipo de material a aplicar al modelo 3D (por defecto: "PBR") |
| `Polygon_count` | COMBO | No | "4K-Quad"<br>"8K-Quad"<br>"18K-Quad"<br>"50K-Quad"<br>"2K-Triangle"<br>"20K-Triangle"<br>"150K-Triangle"<br>"500K-Triangle" | Recuento objetivo de polígonos para el modelo 3D generado (por defecto: "500K-Triangle") |
| `TAPose` | BOOLEAN | No | - | Si aplicar procesamiento TAPose (por defecto: False) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | Ruta del archivo al modelo 3D generado |
