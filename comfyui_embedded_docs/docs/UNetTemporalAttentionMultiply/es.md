> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetTemporalAttentionMultiply/es.md)

El nodo UNetTemporalAttentionMultiply aplica factores de multiplicación a diferentes tipos de mecanismos de atención en un modelo UNet temporal. Modifica el modelo ajustando los pesos de las capas de auto-atención y atención cruzada, distinguiendo entre componentes estructurales y temporales. Esto permite un ajuste fino de cuánta influencia tiene cada tipo de atención en la salida del modelo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo de entrada a modificar con multiplicadores de atención |
| `self_structural` | FLOAT | No | 0.0 - 10.0 | Multiplicador para componentes estructurales de auto-atención (valor por defecto: 1.0) |
| `self_temporal` | FLOAT | No | 0.0 - 10.0 | Multiplicador para componentes temporales de auto-atención (valor por defecto: 1.0) |
| `cross_structural` | FLOAT | No | 0.0 - 10.0 | Multiplicador para componentes estructurales de atención cruzada (valor por defecto: 1.0) |
| `cross_temporal` | FLOAT | No | 0.0 - 10.0 | Multiplicador para componentes temporales de atención cruzada (valor por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo modificado con los pesos de atención ajustados |