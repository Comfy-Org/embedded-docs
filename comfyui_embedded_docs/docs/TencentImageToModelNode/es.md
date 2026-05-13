> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentImageToModelNode/es.md)

Este nodo utiliza la API de Hunyuan3D Pro de Tencent para generar un modelo 3D a partir de una o más imágenes de entrada. Procesa las imágenes, las envía a la API y devuelve los archivos del modelo 3D generado en formatos GLB y OBJ, junto con mapas de textura opcionales.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `modelo` | COMBO | Sí | `"3.0"`<br>`"3.1"` | La versión del modelo Hunyuan3D a utilizar. La opción LowPoly no está disponible para el modelo `3.1`. |
| `imagen` | IMAGE | Sí | - | La imagen de entrada principal utilizada para generar el modelo 3D. Debe tener al menos 128x128 píxeles. |
| `imagen_izquierda` | IMAGE | No | - | Una imagen opcional del lado izquierdo del objeto para generación multivista. Debe tener al menos 128x128 píxeles. |
| `imagen_derecha` | IMAGE | No | - | Una imagen opcional del lado derecho del objeto para generación multivista. Debe tener al menos 128x128 píxeles. |
| `imagen_trasera` | IMAGE | No | - | Una imagen opcional de la parte trasera del objeto para generación multivista. Debe tener al menos 128x128 píxeles. |
| `número_de_caras` | INT | Sí | 3000 - 1500000 | El número objetivo de caras para el modelo 3D generado (predeterminado: 500000). |
| `tipo_de_generación` | DYNAMICCOMBO | Sí | `"Normal"`<br>`"LowPoly"`<br>`"Geometry"` | El tipo de modelo 3D a generar. Seleccionar una opción revela parámetros adicionales relacionados. |
| `generate_type.pbr` | BOOLEAN | No | - | Habilita la generación de materiales basados en renderizado físicamente realista (PBR). Este parámetro solo es visible cuando `tipo_de_generación` está configurado en "Normal" o "LowPoly" (predeterminado: False). |
| `generate_type.polygon_type` | COMBO | No | `"triangle"`<br>`"quadrilateral"` | El tipo de polígono a utilizar para la malla. Este parámetro solo es visible cuando `tipo_de_generación` está configurado en "LowPoly". |
| `semilla` | INT | Sí | 0 - 2147483647 | Un valor de semilla para el proceso de generación. La semilla controla si el nodo debe reejecutarse; los resultados no son deterministas independientemente de la semilla (predeterminado: 0). |

**Nota:** Todas las imágenes de entrada deben tener un ancho y alto mínimo de 128 píxeles. Las imágenes se reducen automáticamente si superan los 4900 píxeles en su lado más largo.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `GLB` | STRING | Una salida heredada para compatibilidad hacia atrás. |
| `OBJ` | FILE3DGLB | El modelo 3D generado en formato de archivo GLB (Formato Binario de Transmisión GL). |
| `texture_image` | FILE3DOBJ | El modelo 3D generado en formato de archivo OBJ (Wavefront). |
| `optional_metallic` | IMAGE | La imagen de textura para el modelo 3D generado. |
| `optional_normal` | IMAGE | El mapa metálico para materiales PBR. Devuelve una imagen negra si no está disponible. |
| `optional_roughness` | IMAGE | El mapa de normales para materiales PBR. Devuelve una imagen negra si no está disponible. |
| `optional_roughness` | IMAGE | El mapa de rugosidad para materiales PBR. Devuelve una imagen negra si no está disponible. |

---
**Source fingerprint (SHA-256):** `56ac9e55bd9bb3a5c7c46c2de1ea06921cf41c0971471f6d0b64166722705e4d`
