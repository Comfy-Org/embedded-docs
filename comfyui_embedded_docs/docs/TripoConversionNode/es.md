> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/es.md)

El TripoConversionNode convierte modelos 3D entre diferentes formatos de archivo utilizando la API de Tripo. Toma un ID de tarea de una operación previa de Tripo y convierte el modelo resultante al formato deseado con varias opciones de exportación.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID,RIG_TASK_ID,RETARGET_TASK_ID | Sí | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID | El ID de tarea de una operación previa de Tripo (generación de modelo, rigging o retargeting) |
| `format` | COMBO | Sí | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF | El formato de archivo objetivo para el modelo 3D convertido |
| `quad` | BOOLEAN | No | Verdadero/Falso | Si convertir triángulos a cuadrángulos (predeterminado: Falso) |
| `face_limit` | INT | No | -1 a 500000 | Número máximo de caras en el modelo de salida, usar -1 para sin límite (predeterminado: -1) |
| `texture_size` | INT | No | 128 a 4096 | Tamaño de las texturas de salida en píxeles (predeterminado: 4096) |
| `texture_format` | COMBO | No | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP | Formato para las texturas exportadas (predeterminado: JPEG) |

**Nota:** El `original_model_task_id` debe ser un ID de tarea válido de una operación previa de Tripo (generación de modelo, rigging o retargeting).

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| *Sin salidas nombradas* | - | Este nodo procesa la conversión de forma asíncrona y devuelve el resultado a través del sistema de API de Tripo |