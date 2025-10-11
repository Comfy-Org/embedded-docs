> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAttentionMultiply/es.md)

El nodo CLIPAttentionMultiply permite ajustar el mecanismo de atención en los modelos CLIP aplicando factores de multiplicación a diferentes componentes de las capas de auto-atención. Funciona modificando los pesos y sesgos de proyección de consulta, clave, valor y salida en el mecanismo de atención del modelo CLIP. Este nodo experimental crea una copia modificada del modelo CLIP de entrada con los factores de escala especificados aplicados.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | requerido | - | - | El modelo CLIP a modificar |
| `q` | FLOAT | requerido | 1.0 | 0.0 - 10.0 | Factor de multiplicación para pesos y sesgos de proyección de consulta |
| `k` | FLOAT | requerido | 1.0 | 0.0 - 10.0 | Factor de multiplicación para pesos y sesgos de proyección de clave |
| `v` | FLOAT | requerido | 1.0 | 0.0 - 10.0 | Factor de multiplicación para pesos y sesgos de proyección de valor |
| `out` | FLOAT | requerido | 1.0 | 0.0 - 10.0 | Factor de multiplicación para pesos y sesgos de proyección de salida |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `CLIP` | CLIP | Devuelve un modelo CLIP modificado con los factores de escala de atención especificados aplicados |