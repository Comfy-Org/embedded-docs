> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetTemporalAttentionMultiply/es.md)

El nodo UNetTemporalAttentionMultiply aplica factores de multiplicación a diferentes tipos de mecanismos de atención en un modelo UNet temporal. Modifica el modelo ajustando los pesos de las capas de autoatención y atención cruzada, distinguiendo entre componentes estructurales y temporales. Esto permite ajustar con precisión cuánta influencia tiene cada tipo de atención en la salida del modelo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo de entrada a modificar con multiplicadores de atención |
| `auto_estructural` | FLOAT | No | 0.0 - 10.0 | Multiplicador para componentes estructurales de autoatención (predeterminado: 1.0) |
| `auto_temporal` | FLOAT | No | 0.0 - 10.0 | Multiplicador para componentes temporales de autoatención (predeterminado: 1.0) |
| `cruz_estructural` | FLOAT | No | 0.0 - 10.0 | Multiplicador para componentes estructurales de atención cruzada (predeterminado: 1.0) |
| `cruz_temporal` | FLOAT | No | 0.0 - 10.0 | Multiplicador para componentes temporales de atención cruzada (predeterminado: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `modelo` | MODEL | El modelo modificado con pesos de atención ajustados |

---
**Source fingerprint (SHA-256):** `98d62fb28a0cdf62154ae4e0b672b3a7bcb9ed61186a164a43992263c1f9439a`
