> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/es.md)

El nodo `LatentOperationTonemapReinhard` aplica el mapeo de tonos Reinhard a vectores latentes. Esta técnica normaliza los vectores latentes y ajusta su magnitud mediante un enfoque estadístico basado en la media y la desviación estándar, con la intensidad controlada por un parámetro multiplicador.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `multiplier` | FLOAT | No | 0.0 a 100.0 | Controla la intensidad del efecto de mapeo de tonos (predeterminado: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `operation` | LATENT_OPERATION | Devuelve una operación de mapeo de tonos que puede aplicarse a vectores latentes |

---
**Source fingerprint (SHA-256):** `70c04eaef06b749392a0c65f3d1267e52484f7cf956f87173d10ad935afcf98c`
