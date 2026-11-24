# Meshy: Texture Model (N1)

Este nodo texturiza un modelo 3D creado previamente con el modelo de texturizado Meshy N1, utilizando de 1 a 4 vistas de referencia del mismo objeto. Conecte el ID de tarea del modelo original junto con las vistas; el nodo las envía a Meshy, espera a que finalice el trabajo y devuelve el modelo texturizado como archivos GLB y FBX junto con el nuevo ID de tarea.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | El modelo de IA utilizado para el trabajo de texturizado. Actualmente solo está disponible `"meshy-n1"`. | COMBO | Sí | `"meshy-n1"` |
| `meshy_task_id` | ID de tarea del modelo 3D creado previamente que debe texturizarse. | MESHY_TASK_ID | Sí | N/A |
| `front_view` | La vista que Meshy trata como frontal. Una imagen texturiza el frente y deja la parte posterior lisa; agregue vistas trasera y laterales en `extra_views` para una parte posterior fiel. | IMAGE | Sí | Imagen única |
| `extra_views` | Vistas adicionales del mismo objeto, en cualquier orden. Ranura ampliable: conecte de 0 a 3 imágenes (`view_1` ... `view_3`). Junto con `front_view`, como máximo 4 imágenes. | IMAGE | No | 0 a 3 imágenes |
| `enable_original_uv` | Utilice el UV original del modelo en lugar de generar nuevos UV. Cuando está habilitado, Meshy conserva las texturas existentes del modelo cargado. Si el modelo no tiene UV original, la calidad de la salida podría no ser tan buena. (predeterminado: True; opción avanzada) | BOOLEAN | No | True / False |

**Nota:** `front_view` y `extra_views` pueden contener como máximo 4 imágenes en conjunto; el nodo genera un error cuando se conectan más. Si una imagen conectada contiene un lote, cada imagen del lote cuenta para ese límite. La resolución de textura es fija de 2K y no se generan mapas PBR.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `meshy_task_id` | ID de tarea del trabajo de texturizado, utilizable por nodos Meshy posteriores. | MESHY_TASK_ID |
| `GLB` | El modelo 3D texturizado descargado en formato GLB. | FILE3DGLB |
| `FBX` | El modelo 3D texturizado descargado en formato FBX. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureN1Node/es.md)

---
**Source fingerprint (SHA-256):** `808df4f5a32b2d9ca6e74668051409836f2fcbc078d4ee3e85c07121d7a81f76`
