# Tripo P1: Multivista a Modelo

Este nodo genera un modelo 3D a partir de 2 a 4 imágenes de referencia de un objeto o personaje. Proporcionas imágenes desde diferentes ángulos (frontal, izquierdo, trasero, derecho), y el nodo crea una malla 3D en formato GLB. La vista frontal es obligatoria, y puedes agregar opcionalmente cualquier combinación de las otras tres vistas para obtener mejores resultados.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imagen` | Vista frontal (0°). Obligatoria. | IMAGE | Sí | - |
| `imagen_izquierda` | Vista izquierda (90°), es decir, el lado izquierdo del sujeto. | IMAGE | No | - |
| `imagen_trasera` | Vista trasera (180°). | IMAGE | No | - |
| `imagen_derecha` | Vista derecha (270°), es decir, el lado derecho del sujeto. | IMAGE | No | - |
| `modo_de_salida` | El modo de salida para el modelo generado. `"geometry"` produce una malla sin procesar, `"textured"` añade una textura estándar, y `"detailed"` crea un modelo texturizado de alto detalle (predeterminado: `"textured"`). | COMBO | Sí | `"geometry"`<br>`"textured"`<br>`"detailed"` |
| `límite_de_caras` | Número máximo de caras para la malla de salida. Establecer en -1 para sin límite (predeterminado: -1). | INT | No | -1 a 100000 |
| `semilla_modelo` | Semilla para generación reproducible del modelo. Establecer en 0 para aleatorio (predeterminado: 0). | INT | No | 0 a 2147483647 |
| `auto_escala` | Ajustar automáticamente el tamaño del modelo para que quepa dentro de un cuadro delimitador estándar (predeterminado: False). | BOOLEAN | No | True / False |
| `exportar_uv` | Exportar coordenadas UV con el modelo (predeterminado: True). | BOOLEAN | No | True / False |
| `comprimir_geometría` | Comprimir los datos de geometría para reducir el tamaño del archivo (predeterminado: False). | BOOLEAN | No | True / False |

**Nota:** Debes proporcionar al menos 2 imágenes: la vista frontal (`image`) más al menos una de las otras vistas (`image_left`, `image_back` o `image_right`). Si se proporcionan menos de 2 imágenes, el nodo generará un error.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `archivo_modelo` | El nombre del archivo del modelo GLB generado (solo para compatibilidad hacia atrás). | STRING |
| `id_tarea_modelo` | El ID de tarea único para esta solicitud de generación de modelo. | MODEL_TASK_ID |
| `GLB` | El modelo 3D generado en formato GLB. | FILE3DGLB |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1MultiviewToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `29bb87cdc5d3eef891a653c622e8876a37d6e6dc1a43e5c248b184060ead9029`
