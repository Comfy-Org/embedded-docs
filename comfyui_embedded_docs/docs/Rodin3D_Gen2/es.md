> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen2/es.md)

El nodo Rodin3D_Gen2 genera activos 3D utilizando la API de Rodin. Toma imágenes de entrada y las convierte en modelos 3D con varios tipos de material y recuentos de polígonos. El nodo maneja todo el proceso de generación, incluyendo la creación de tareas, el sondeo de estado y la descarga de archivos de forma automática.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | Sí | - | Imágenes de entrada para usar en la generación del modelo 3D |
| `Seed` | INT | No | 0-65535 | Valor de semilla aleatoria para la generación (predeterminado: 0) |
| `Material_Type` | COMBO | No | "PBR"<br>"Shaded" | Tipo de material a aplicar al modelo 3D (predeterminado: "PBR") |
| `Polygon_count` | COMBO | No | "4K-Quad"<br>"8K-Quad"<br>"18K-Quad"<br>"50K-Quad"<br>"2K-Triangle"<br>"20K-Triangle"<br>"150K-Triangle"<br>"500K-Triangle" | Recuento de polígonos objetivo para el modelo 3D generado (predeterminado: "500K-Triangle") |
| `TAPose` | BOOLEAN | No | - | Si se debe aplicar el procesamiento TAPose (predeterminado: False) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | Ruta de archivo al modelo 3D generado (para compatibilidad hacia atrás) |
| `GLB` | FILE3DGLB | El modelo 3D generado en formato GLB |

---
**Source fingerprint (SHA-256):** `940712a9a40f4cb07050f3ed7ac502469b30bd364f86bb42b9dd8bf63eb912a2`
