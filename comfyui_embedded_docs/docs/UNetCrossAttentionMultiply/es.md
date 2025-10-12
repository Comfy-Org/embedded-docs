> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetCrossAttentionMultiply/es.md)

El nodo UNetCrossAttentionMultiply aplica factores de multiplicación al mecanismo de atención cruzada en un modelo UNet. Permite escalar los componentes de consulta, clave, valor y salida de las capas de atención cruzada para experimentar con diferentes comportamientos y efectos de atención.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo UNet a modificar con factores de escalado de atención |
| `q` | FLOAT | No | 0.0 - 10.0 | Factor de escalado para componentes de consulta en atención cruzada (valor por defecto: 1.0) |
| `k` | FLOAT | No | 0.0 - 10.0 | Factor de escalado para componentes de clave en atención cruzada (valor por defecto: 1.0) |
| `v` | FLOAT | No | 0.0 - 10.0 | Factor de escalado para componentes de valor en atención cruzada (valor por defecto: 1.0) |
| `salida` | FLOAT | No | 0.0 - 10.0 | Factor de escalado para componentes de salida en atención cruzada (valor por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `modelo` | MODEL | El modelo UNet modificado con componentes de atención cruzada escalados |
