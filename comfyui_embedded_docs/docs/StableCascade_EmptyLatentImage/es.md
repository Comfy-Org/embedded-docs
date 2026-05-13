> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/es.md)

El nodo `StableCascade_EmptyLatentImage` crea tensores latentes vacíos para los modelos Stable Cascade. Genera dos representaciones latentes separadas — una para la etapa C y otra para la etapa B — con dimensiones apropiadas según la resolución de entrada y la configuración de compresión. Este nodo proporciona el punto de partida para el pipeline de generación de Stable Cascade.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `ancho` | INT | Sí | 256 a MAX_RESOLUTION | El ancho de la imagen de salida en píxeles (predeterminado: 1024, incremento: 8) |
| `altura` | INT | Sí | 256 a MAX_RESOLUTION | La altura de la imagen de salida en píxeles (predeterminado: 1024, incremento: 8) |
| `compresión` | INT | Sí | 4 a 128 | El factor de compresión que determina las dimensiones latentes para la etapa C (predeterminado: 42, incremento: 1) |
| `tamaño_del_lote` | INT | No | 1 a 4096 | El número de muestras latentes a generar en un lote (predeterminado: 1) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `etapa_b` | LATENT | El tensor latente de la etapa C con dimensiones [batch_size, 16, altura//compresión, ancho//compresión] |
| `stage_b` | LATENT | El tensor latente de la etapa B con dimensiones [batch_size, 4, altura//4, ancho//4] |

---
**Source fingerprint (SHA-256):** `ba5347f522b661993e540bc5775737cae88bd5f7a87c1b91715f8c1858e8e81a`
