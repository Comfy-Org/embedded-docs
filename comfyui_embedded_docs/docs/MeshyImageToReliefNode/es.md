# Meshy: Image to Relief

Este nodo convierte una foto en un modelo de bajorrelieve además de un mapa de profundidad de 16 bits para impresión 3D, grabado láser y tallado CNC. Las ilustraciones oscuras sobre un fondo claro se elevan y las zonas claras permanecen bajas. Solo se generan y descargan las salidas que conectes, así que, si no hay ninguna salida de modelo conectada, la tarea devuelve únicamente el mapa de profundidad.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `image` | Foto que se convertirá en un relieve. Las ilustraciones oscuras sobre un fondo claro se elevan. La transparencia se elimina antes de la carga, así que primero aplana un logotipo transparente sobre un fondo blanco. | IMAGE | Sí | Imagen única |
| `relief_type` | Preajuste de tallado. `"low"` es un tallado poco profundo para grabado láser, trabajo CNC y placas; `"high"` es más profundo para piezas impresas en 3D. El preajuste selecciona el valor de `carving_depth_mm`. | DYNAMIC_COMBO | Sí | `"low"`<br>`"high"` |
| `carving_depth_mm` | Profundidad del tallado en milímetros. Disponible cuando `relief_type` está establecido (predeterminado: 3.0 para `"low"`, 6.0 para `"high"`). | FLOAT | Sí | 0.1 a 60.0 (paso: 0.1) |
| `size_mm` | Longitud del lado más largo de la foto sobre el modelo, en milímetros, medida en plano antes de cualquier curvatura (predeterminado: 60.0). | FLOAT | Sí | 20.0 a 250.0 (paso: 1.0) |
| `carving_mode` | `"emboss"` eleva las partes más cercanas de la foto; `"engrave"` las incide hacia dentro. | COMBO | Sí | `"emboss"`<br>`"engrave"` |
| `base` | `"plate"` mantiene una placa base debajo del relieve; `"none"` recorta el fondo y no construye ninguna placa. Al seleccionar una opción se revela su parámetro. | DYNAMIC_COMBO | Sí | `"plate"`<br>`"none"` |
| `base_thickness_mm` | Grosor de la placa base en milímetros. Disponible cuando `base` es `"plate"` (predeterminado: 1.0). | FLOAT | Sí | 0.1 a 10.0 (paso: 0.1) |
| `removal_threshold` | Profundidad por debajo de la cual se recorta el fondo, en el mapa de profundidad de 0 a 1. 0.3 mantiene un busto entero; 0.8 lo fragmenta. Disponible cuando `base` es `"none"` (predeterminado: 0.01). | FLOAT | Sí | 0.01 a 1.0 (paso: 0.01) |
| `bend` | `"convex"` abomba el frente hacia fuera; `"concave"` lo curva hacia dentro; `"off"` mantiene el relieve plano. Al seleccionar una curvatura se revelan `bend_axis` y `bend_angle`. | DYNAMIC_COMBO | Sí | `"off"`<br>`"convex"`<br>`"concave"` |
| `bend_axis` | `"xz"` curva los bordes izquierdo y derecho; `"yz"`, los bordes superior e inferior. Disponible cuando `bend` es `"convex"` o `"concave"`. | COMBO | Sí | `"xz"`<br>`"yz"` |
| `bend_angle` | Arco que abarca la curvatura, en grados; 360 cierra el relieve formando un cilindro. Disponible cuando `bend` es `"convex"` o `"concave"` (predeterminado: 60.0). | FLOAT | Sí | 1.0 a 360.0 (paso: 1.0) |
| `seed` | Semilla que controla si el nodo se vuelve a ejecutar; el resultado no es determinista independientemente de la semilla. Cámbiala para solicitar una salida que se conectó después de la última ejecución (predeterminado: 42). | INT | Sí | 0 a 2147483647 |
| `mesh_resolution` | Puntos de malla a lo largo del lado más largo de la foto. Con 1024, el GLB ocupa unos 50 MB y el STL unos 105 MB; con 2048, unos 200 MB y 420 MB; una curvatura los duplica. (predeterminado: 1024; opción avanzada) | INT | Sí | 512 a 2048 |
| `color_mapping` | Colorea los archivos GLB, OBJ, FBX y USDZ con la foto. STL y 3MF permanecen blancos. (predeterminado: False; opción avanzada) | BOOLEAN | Sí | True / False |

**Nota:** Un formato de modelo solo se genera y se descarga cuando su salida está conectada. Si no hay ninguna salida de modelo conectada, la tarea devuelve únicamente el mapa de profundidad, y `preview` por sí sola aún hace que se genere el modelo para la miniatura, pero no devuelve ningún archivo de modelo. `depth_map` conserva el rango completo de 16 bits; Save Image (Advanced) lo escribe como PNG de 16 bits.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `GLB` | El modelo de relieve descargado en formato GLB. | FILE3DGLB |
| `STL` | El modelo de relieve descargado en formato STL. | FILE3DSTL |
| `OBJ` | El modelo de relieve descargado en formato OBJ. | FILE3DOBJ |
| `FBX` | El modelo de relieve descargado en formato FBX. | FILE3DFBX |
| `USDZ` | El modelo de relieve descargado en formato USDZ. | FILE3DUSDZ |
| `3MF` | El modelo de relieve descargado en formato 3MF. | FILE3D |
| `depth_map` | Mapa de profundidad con el rango completo de 16 bits; Save Image (Advanced) lo escribe como PNG de 16 bits. | IMAGE |
| `preview` | Miniatura renderizada por Meshy para el relieve terminado. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToReliefNode/es.md)

---
**Source fingerprint (SHA-256):** `6f2f0eb49074281b99d7ee10daf3bcc5616c6596c1c4d8491c72739550395f52`
