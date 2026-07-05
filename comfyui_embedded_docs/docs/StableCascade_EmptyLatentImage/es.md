# StableCascade_EmptyLatentImage

El nodo `StableCascade_EmptyLatentImage` crea tensores latentes vacíos para los modelos Stable Cascade. Genera dos representaciones latentes separadas — una para la etapa C y otra para la etapa B — con dimensiones apropiadas según la resolución de entrada y la configuración de compresión. Este nodo proporciona el punto de partida para el pipeline de generación de Stable Cascade.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `ancho` | El ancho de la imagen de salida en píxeles (predeterminado: 1024, incremento: 8) | INT | Sí | 256 a MAX_RESOLUTION |
| `altura` | La altura de la imagen de salida en píxeles (predeterminado: 1024, incremento: 8) | INT | Sí | 256 a MAX_RESOLUTION |
| `compresión` | El factor de compresión que determina las dimensiones latentes para la etapa C (predeterminado: 42, incremento: 1) | INT | Sí | 4 a 128 |
| `tamaño_del_lote` | El número de muestras latentes a generar en un lote (predeterminado: 1) | INT | No | 1 a 4096 |


| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `stage_c` | El tensor latente de la etapa C con dimensiones [batch_size, 16, altura//compresión, ancho//compresión] | LATENT |
| `stage_b` | El tensor latente de la etapa B con dimensiones [batch_size, 4, altura//4, ancho//4] | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/es.md)

---
**Source fingerprint (SHA-256):** `ba5347f522b661993e540bc5775737cae88bd5f7a87c1b91715f8c1858e8e81a`
