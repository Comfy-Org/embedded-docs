# MoGe Point Map a Malla

Este nodo convierte un mapa de puntos MoGe en una malla 3D. Toma los datos de geometría generados por un nodo de estimación de profundidad MoGe y los triangula en una malla con coordenadas UV y una textura opcional.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Los datos de geometría MoGe que contienen mapas de puntos, profundidad y, opcionalmente, la imagen de origen. | MOGE_GEOMETRY | Sí | N/D |
| `batch_index` | Qué imagen de una geometría MoGe por lotes se va a mallar. El número de vértices por imagen difiere, por lo que los lotes no se pueden apilar en una sola MESH (predeterminado: 0). | INT | Sí | 0 a 4096 |
| `decimation` | Paso de vértice; 1 = resolución completa (predeterminado: 1). | INT | Sí | 1 a 8 |
| `discontinuity_threshold` | Descarta píxeles cuyo rango de profundidad 3x3 supere esta fracción. 0 = desactivado (predeterminado: 0.04). | FLOAT | Sí | 0.0 a 1.0 |
| `texture` | Transmite la imagen de origen como textura baseColor (predeterminado: True). | BOOLEAN | Sí | True/False |

Nota: `batch_index` debe ser menor que el tamaño del lote de la `moge_geometry` de entrada; si se selecciona un índice fuera de rango, se genera un error. Si la triangulación produce una malla vacía, el nodo genera un error; establecer `discontinuity_threshold` en 0 desactiva el filtro de discontinuidad de profundidad. La malla de salida se convierte a coordenadas glTF: los datos MoGe en perspectiva (X derecha, Y abajo, Z hacia adelante) se invierten para coincidir con glTF (Y arriba, Z hacia atrás), y los datos panorámicos se rotan en consecuencia. Cuando `texture` está habilitado, la imagen de origen de `moge_geometry` se usa como textura baseColor.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `MESH` | Una malla 3D con vértices, caras, coordenadas UV y una textura baseColor opcional de la imagen de origen. | MESH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/es.md)

---
**Source fingerprint (SHA-256):** `626925866eed6805d2ce87529909fc76b9484cd2e8118fdd1669a237d44b9b0b`
