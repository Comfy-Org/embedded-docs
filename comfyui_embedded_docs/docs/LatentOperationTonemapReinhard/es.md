# OperaciónTonemapReinhardLatente

LatentOperationTonemapReinhard aplica un mapeo tonal de Reinhard a los vectores latentes. Esta técnica normaliza los vectores latentes y ajusta su magnitud mediante un enfoque estadístico basado en la media y la desviación estándar de las magnitudes, con la intensidad controlada por un parámetro multiplicador.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `multiplier` | Controla la intensidad del efecto de mapeo tonal (por defecto: 1.0) | FLOAT | Sí | 0.0 to 100.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `operation` | Devuelve una operación de mapeo tonal que se puede aplicar a vectores latentes | LATENT_OPERATION |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/es.md)

---
**Source fingerprint (SHA-256):** `19d58c288967ab27eb1e84e60bc35a6d6c8b4e643168de689132396ae0ee3cbe`
