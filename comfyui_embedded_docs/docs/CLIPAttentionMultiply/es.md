> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAttentionMultiply/es.md)

El nodo `CLIPAttentionMultiply` permite ajustar el mecanismo de atención en modelos CLIP aplicando factores de multiplicación a diferentes componentes de las capas de autoatención. Funciona modificando los pesos y sesgos de las proyecciones de consulta, clave, valor y salida en el mecanismo de atención del modelo CLIP. Este nodo experimental crea una copia modificada del modelo CLIP de entrada con los factores de escala especificados aplicados.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `clip` | CLIP | Sí | - | El modelo CLIP a modificar |
| `q` | FLOAT | Sí | 0.0 - 10.0 | Factor de multiplicación para los pesos y sesgos de la proyección de consulta (predeterminado: 1.0) |
| `k` | FLOAT | Sí | 0.0 - 10.0 | Factor de multiplicación para los pesos y sesgos de la proyección de clave (predeterminado: 1.0) |
| `v` | FLOAT | Sí | 0.0 - 10.0 | Factor de multiplicación para los pesos y sesgos de la proyección de valor (predeterminado: 1.0) |
| `out` | FLOAT | Sí | 0.0 - 10.0 | Factor de multiplicación para los pesos y sesgos de la proyección de salida (predeterminado: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `CLIP` | CLIP | Devuelve un modelo CLIP modificado con los factores de escala de atención especificados aplicados |

---
**Source fingerprint (SHA-256):** `43dab83ecfc928f3359eb7560658f43235bf3faa62c81084a2b4f482e3a4638f`
