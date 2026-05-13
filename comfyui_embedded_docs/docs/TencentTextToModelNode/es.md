> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentTextToModelNode/es.md)

Este nodo utiliza la API de Hunyuan3D Pro de Tencent para generar un modelo 3D a partir de una descripción textual. Envía una solicitud para crear una tarea de generación, consulta el resultado y descarga los archivos finales del modelo en formatos GLB y OBJ.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | `"3.0"`<br>`"3.1"` | La versión del modelo Hunyuan3D a utilizar. La opción LowPoly no está disponible para el modelo `3.1`. |
| `prompt` | STRING | Sí | - | La descripción textual del modelo 3D a generar. Admite hasta 1024 caracteres. |
| `face_count` | INT | Sí | 3000 - 1500000 | El número objetivo de caras para el modelo 3D generado. Valor predeterminado: 500000. |
| `generate_type` | DYNAMICCOMBO | Sí | `"Normal"`<br>`"LowPoly"`<br>`"Geometry"` | El tipo de modelo 3D a generar. Las opciones disponibles y sus parámetros asociados son:<br>- **Normal**: Genera un modelo estándar. Incluye un parámetro `pbr` (valor predeterminado: `False`).<br>- **LowPoly**: Genera un modelo de baja poligonización. Incluye los parámetros `polygon_type` (`"triangle"` o `"quadrilateral"`) y `pbr` (valor predeterminado: `False`).<br>- **Geometry**: Genera un modelo solo de geometría. |
| `seed` | INT | No | 0 - 2147483647 | Un valor de semilla para la generación. Los resultados no son deterministas independientemente de la semilla. Establecer una nueva semilla controla si el nodo debe reejecutarse. Valor predeterminado: 0. |

**Nota:** El parámetro `generate_type` es dinámico. Seleccionar `"LowPoly"` revelará entradas adicionales para `polygon_type` y `pbr`. Seleccionar `"Normal"` revelará una entrada para `pbr`. Seleccionar `"Geometry"` no revelará ninguna entrada adicional.

**Restricción:** El tipo de generación `"LowPoly"` no se puede utilizar con el modelo `"3.1"`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model_file` | STRING | Una salida heredada para compatibilidad con versiones anteriores. |
| `GLB` | FILE3DGLB | El modelo 3D generado en formato de archivo GLB. |
| `OBJ` | FILE3DOBJ | El modelo 3D generado en formato de archivo OBJ. |
| `texture_image` | IMAGE | La imagen de textura extraída del archivo OBJ generado, si está disponible. |

---
**Source fingerprint (SHA-256):** `e35f5165941cc7761639dd72e78141326d37d5e169be9a0e326afcbcdc572b7d`
