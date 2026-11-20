# Model Merge MiniMax H3

Fusiona dos modelos MiniMax H3 compatibles por componente, con una proporción independiente para cada parte de la arquitectura. Aumentar una proporción toma más de ese componente de `model2`, de modo que puedes conservar las proyecciones de parches y los bloques de refinamiento de un modelo mientras reemplazas los bloques transformer con los de otro.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model1` | Primer modelo MiniMax H3, la base de la que se toma cada componente (el peso predeterminado se aplica donde no se usa `model2`). | MODEL | Sí | - |
| `model2` | Segundo modelo MiniMax H3 que proporciona los componentes que combinas. | MODEL | Sí | - |
| `video_patch_proj.` | Proporción de `model2` para la proyección de parches de video (predeterminado: 1.0). | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |
| `audio_patch_proj.` | Proporción de `model2` para la proyección de parches de audio (predeterminado: 1.0). | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |
| `condition_proj.` | Proporción de `model2` para la proyección de condicionamiento (predeterminado: 1.0). | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |
| `time_embedder.` | Proporción de `model2` para el embedder de tiempo (predeterminado: 1.0). | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |
| `token_refiner.blocks.0.` | Proporción de `model2` para el primer bloque refinador de tokens (predeterminado: 1.0). | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |
| `token_refiner.blocks.1.` | Proporción de `model2` para el segundo bloque refinador de tokens (predeterminado: 1.0). | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |
| `token_refiner.final_norm.` | Proporción de `model2` para la normalización final del refinador de tokens (predeterminado: 1.0). | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |
| `blocks.0.` a `blocks.49.` | Proporción de `model2` para cada uno de los 50 bloques transformer, un widget por bloque (predeterminado: 1.0). | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |
| `final_layer.norm.` | Proporción de `model2` para la normalización de la capa final (predeterminado: 1.0). | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |
| `final_layer.adaln_proj.` | Proporción de `model2` para la proyección de normalización adaptativa final (predeterminado: 1.0). | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |
| `final_layer.video_out.` | Proporción de `model2` para la capa de salida de video (predeterminado: 1.0). | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |
| `final_layer.audio_out.` | Proporción de `model2` para la capa de salida de audio (predeterminado: 1.0). | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |

Una proporción de 0.0 mantiene ese componente completamente de `model1` y 1.0 lo toma completamente de `model2`; los valores intermedios mezclan ambos. Los tensores que no llevan proporción, como las estadísticas de normalización, siempre provienen de `model1`. Ambas entradas deben ser modelos MiniMax H3 con la misma arquitectura; de lo contrario, la fusión produce un modelo que no se ejecuta.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `MODEL` | El modelo MiniMax H3 fusionado. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMiniMaxH3/es.md)

---
**Source fingerprint (SHA-256):** `4fea4e588d16a8396c68aa071a59e671a2a0c645734606be6d7e221986ba88bd`
