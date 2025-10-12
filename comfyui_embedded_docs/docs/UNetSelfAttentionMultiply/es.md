> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetSelfAttentionMultiply/es.md)

El nodo UNetSelfAttentionMultiply aplica factores de multiplicación a los componentes de consulta, clave, valor y salida del mecanismo de autoatención en un modelo UNet. Permite escalar diferentes partes del cálculo de atención para experimentar con cómo los pesos de atención afectan el comportamiento del modelo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo UNet a modificar con factores de escalado de atención |
| `q` | FLOAT | No | 0.0 - 10.0 | Factor de multiplicación para el componente de consulta (predeterminado: 1.0) |
| `k` | FLOAT | No | 0.0 - 10.0 | Factor de multiplicación para el componente de clave (predeterminado: 1.0) |
| `v` | FLOAT | No | 0.0 - 10.0 | Factor de multiplicación para el componente de valor (predeterminado: 1.0) |
| `salida` | FLOAT | No | 0.0 - 10.0 | Factor de multiplicación para el componente de salida (predeterminado: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `MODEL` | MODEL | El modelo UNet modificado con componentes de atención escalados |
