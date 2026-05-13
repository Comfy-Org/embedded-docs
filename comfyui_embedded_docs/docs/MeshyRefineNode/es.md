> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRefineNode/es.md)

El nodo **Meshy: Refinar Modelo Borrador** toma un modelo 3D borrador generado previamente y mejora su calidad, añadiendo opcionalmente texturas. Envía una tarea de refinamiento a la API de Meshy y devuelve los archivos finales del modelo 3D una vez que el procesamiento esté completo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `modelo` | COMBO | Sí | `"latest"` | Especifica el modelo de IA a utilizar para el refinamiento. Actualmente, solo está disponible el modelo "latest". |
| `meshy_task_id` | MESHY_TASK_ID | Sí | - | El ID de tarea único del modelo borrador que deseas refinar. |
| `habilitar_pbr` | BOOLEAN | No | - | Generar mapas PBR (metálico, rugosidad, normal) además del color base. Nota: debe establecerse en falso al usar el estilo Escultura, ya que este estilo genera su propio conjunto de mapas PBR. (predeterminado: `False`) |
| `texto_de_textura` | STRING | No | - | Proporciona un prompt de texto para guiar el proceso de texturizado. Máximo 600 caracteres. No puede usarse al mismo tiempo que `imagen_de_textura`. (predeterminado: cadena vacía) |
| `imagen_de_textura` | IMAGE | No | - | Solo se puede usar uno de los dos: `imagen_de_textura` o `texto_de_textura` al mismo tiempo. |

**Nota:** Las entradas `texture_prompt` y `texture_image` son mutuamente excluyentes. No puedes proporcionar tanto un prompt de texto como una imagen para texturizar en la misma operación.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `meshy_task_id` | STRING | El nombre del archivo del modelo GLB generado. (Solo por compatibilidad hacia atrás) |
| `GLB` | MESHY_TASK_ID | El ID de tarea único para el trabajo de refinamiento enviado. |
| `FBX` | FILE3DGLB | El modelo 3D final refinado en formato GLB. |
| `FBX` | FILE3DFBX | El modelo 3D final refinado en formato FBX. |

---
**Source fingerprint (SHA-256):** `cdf620ead0a4504cbb5d5554e0fe40e4cadd08884726f147cd486e63ab37f278`
