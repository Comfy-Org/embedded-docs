> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/es.md)

El TripoConversionNode convierte modelos 3D entre diferentes formatos de archivo utilizando la API de Tripo. Toma un ID de tarea de una operación previa de Tripo (generación de modelo, rigging o retargeting) y convierte el modelo resultante al formato deseado con varias opciones de exportación.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-------------|-------------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID,RIG_TASK_ID,RETARGET_TASK_ID | Sí | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID | El ID de tarea de una operación previa de Tripo (generación de modelo, rigging o retargeting) |
| `format` | COMBO | Sí | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF | El formato de archivo de destino para el modelo 3D convertido |
| `quad` | BOOLEAN | No | True/False | Si convertir triángulos a cuadriláteros (predeterminado: False) |
| `face_limit` | INT | No | -1 a 2000000 | Número máximo de caras en el modelo de salida, use -1 para sin límite (predeterminado: -1) |
| `texture_size` | INT | No | 128 a 4096 | Tamaño de las texturas de salida en píxeles (predeterminado: 4096) |
| `texture_format` | COMBO | No | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP | Formato para las texturas exportadas (predeterminado: JPEG) |
| `force_symmetry` | BOOLEAN | No | True/False | Si forzar simetría en el modelo (predeterminado: False) |
| `flatten_bottom` | BOOLEAN | No | True/False | Si aplanar la parte inferior del modelo (predeterminado: False) |
| `flatten_bottom_threshold` | FLOAT | No | 0.0 a 1.0 | Umbral para el aplanamiento inferior (predeterminado: 0.0) |
| `pivot_to_center_bottom` | BOOLEAN | No | True/False | Si mover el punto de pivote al centro inferior del modelo (predeterminado: False) |
| `scale_factor` | FLOAT | No | 0.0 y superior | Factor de escala a aplicar al modelo (predeterminado: 1.0) |
| `with_animation` | BOOLEAN | No | True/False | Si incluir datos de animación en la exportación (predeterminado: False) |
| `pack_uv` | BOOLEAN | No | True/False | Si empaquetar coordenadas UV (predeterminado: False) |
| `bake` | BOOLEAN | No | True/False | Si hornear texturas (predeterminado: False) |
| `part_names` | STRING | No | Lista separada por comas | Lista separada por comas de nombres de partes a incluir en la exportación (predeterminado: "") |
| `fbx_preset` | COMBO | No | blender<br>mixamo<br>3dsmax | Preajuste de exportación FBX a utilizar (predeterminado: blender) |
| `export_vertex_colors` | BOOLEAN | No | True/False | Si exportar colores de vértices (predeterminado: False) |
| `export_orientation` | COMBO | No | align_image<br>default | Modo de orientación de exportación (predeterminado: default) |
| `animate_in_place` | BOOLEAN | No | True/False | Si animar el modelo en su lugar (predeterminado: False) |

**Nota:** El `original_model_task_id` debe ser un ID de tarea válido de una operación previa de Tripo (generación de modelo, rigging o retargeting). Los parámetros marcados como "avanzados" son opcionales y solo necesitan configurarse para requisitos de exportación específicos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|-------------|-------------|
| *Sin salidas nombradas* | - | Este nodo procesa la conversión de forma asíncrona y devuelve el resultado a través del sistema de API de Tripo |

---
**Source fingerprint (SHA-256):** `b11ecab98701b7153a350f5e4980ddc2f446c0a12be3402ca98a5e6de60bd7ce`
