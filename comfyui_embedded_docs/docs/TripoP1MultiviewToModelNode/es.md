> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1MultiviewToModelNode/es.md)

# Descripción General

Este nodo genera un modelo 3D a partir de 2 a 4 imágenes de referencia de un objeto o personaje. Proporcionas imágenes desde diferentes ángulos (frontal, izquierdo, trasero, derecho), y el nodo crea una malla 3D en formato GLB. La vista frontal es obligatoria, y puedes agregar opcionalmente cualquier combinación de las otras tres vistas para obtener mejores resultados.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | - | Vista frontal (0°). Obligatoria. |
| `image_left` | IMAGE | No | - | Vista izquierda (90°), es decir, el lado izquierdo del sujeto. |
| `image_back` | IMAGE | No | - | Vista trasera (180°). |
| `image_right` | IMAGE | No | - | Vista derecha (270°), es decir, el lado derecho del sujeto. |
| `output_mode` | COMBO | Sí | `"geometry"`<br>`"textured"`<br>`"detailed"` | El modo de salida para el modelo generado. `"geometry"` produce una malla sin procesar, `"textured"` añade una textura estándar, y `"detailed"` crea un modelo texturizado de alto detalle (predeterminado: `"textured"`). |
| `face_limit` | INT | No | -1 a 100000 | Número máximo de caras para la malla de salida. Establecer en -1 para sin límite (predeterminado: -1). |
| `model_seed` | INT | No | 0 a 2147483647 | Semilla para generación reproducible del modelo. Establecer en 0 para aleatorio (predeterminado: 0). |
| `auto_size` | BOOLEAN | No | True / False | Ajustar automáticamente el tamaño del modelo para que quepa dentro de un cuadro delimitador estándar (predeterminado: False). |
| `export_uv` | BOOLEAN | No | True / False | Exportar coordenadas UV con el modelo (predeterminado: True). |
| `compress_geometry` | BOOLEAN | No | True / False | Comprimir los datos de geometría para reducir el tamaño del archivo (predeterminado: False). |

**Nota:** Debes proporcionar al menos 2 imágenes: la vista frontal (`image`) más al menos una de las otras vistas (`image_left`, `image_back` o `image_right`). Si se proporcionan menos de 2 imágenes, el nodo generará un error.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `model_file` | STRING | El nombre del archivo del modelo GLB generado (solo para compatibilidad hacia atrás). |
| `model_task_id` | MODEL_TASK_ID | El ID de tarea único para esta solicitud de generación de modelo. |
| `GLB` | FILE3DGLB | El modelo 3D generado en formato GLB. |

---
**Source fingerprint (SHA-256):** `29bb87cdc5d3eef891a653c622e8876a37d6e6dc1a43e5c248b184060ead9029`
