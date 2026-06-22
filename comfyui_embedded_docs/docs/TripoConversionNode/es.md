# Tripo: Convertir modelo

El TripoConversionNode convierte modelos 3D entre diferentes formatos de archivo utilizando la API de Tripo. Toma un ID de tarea de una operación previa de Tripo (generación de modelo, rigging o retargeting) y convierte el modelo resultante al formato deseado con varias opciones de exportación.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `id_tarea_modelo_original` | El ID de tarea de una operación previa de Tripo (generación de modelo, rigging o retargeting) | MODEL_TASK_ID,RIG_TASK_ID,RETARGET_TASK_ID | Sí | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID |
| `formato` | El formato de archivo de destino para el modelo 3D convertido | COMBO | Sí | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF |
| `cuadrangular` | Si convertir triángulos a cuadriláteros (predeterminado: False) | BOOLEAN | No | True/False |
| `límite_caras` | Número máximo de caras en el modelo de salida, use -1 para sin límite (predeterminado: -1) | INT | No | -1 a 2000000 |
| `tamaño_textura` | Tamaño de las texturas de salida en píxeles (predeterminado: 4096) | INT | No | 128 a 4096 |
| `formato_textura` | Formato para las texturas exportadas (predeterminado: JPEG) | COMBO | No | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP |
| `force_symmetry` | Si forzar simetría en el modelo (predeterminado: False) | BOOLEAN | No | True/False |
| `flatten_bottom` | Si aplanar la parte inferior del modelo (predeterminado: False) | BOOLEAN | No | True/False |
| `flatten_bottom_threshold` | Umbral para el aplanamiento inferior (predeterminado: 0.0) | FLOAT | No | 0.0 a 1.0 |
| `pivot_to_center_bottom` | Si mover el punto de pivote al centro inferior del modelo (predeterminado: False) | BOOLEAN | No | True/False |
| `scale_factor` | Factor de escala a aplicar al modelo (predeterminado: 1.0) | FLOAT | No | 0.0 y superior |
| `with_animation` | Si incluir datos de animación en la exportación (predeterminado: False) | BOOLEAN | No | True/False |
| `pack_uv` | Si empaquetar coordenadas UV (predeterminado: False) | BOOLEAN | No | True/False |
| `bake` | Si hornear texturas (predeterminado: False) | BOOLEAN | No | True/False |
| `part_names` | Lista separada por comas de nombres de partes a incluir en la exportación (predeterminado: "") | STRING | No | Lista separada por comas |
| `fbx_preset` | Preajuste de exportación FBX a utilizar (predeterminado: blender) | COMBO | No | blender<br>mixamo<br>3dsmax |
| `export_vertex_colors` | Si exportar colores de vértices (predeterminado: False) | BOOLEAN | No | True/False |
| `export_orientation` | Modo de orientación de exportación (predeterminado: default) | COMBO | No | align_image<br>default |
| `animate_in_place` | Si animar el modelo en su lugar (predeterminado: False) | BOOLEAN | No | True/False |

**Nota:** El `original_model_task_id` debe ser un ID de tarea válido de una operación previa de Tripo (generación de modelo, rigging o retargeting). Los parámetros marcados como "avanzados" son opcionales y solo necesitan configurarse para requisitos de exportación específicos.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| *Sin salidas nombradas* | Este nodo procesa la conversión de forma asíncrona y devuelve el resultado a través del sistema de API de Tripo | - |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/es.md)

---
**Source fingerprint (SHA-256):** `b11ecab98701b7153a350f5e4980ddc2f446c0a12be3402ca98a5e6de60bd7ce`
