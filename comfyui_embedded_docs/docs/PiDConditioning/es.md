> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/es.md)

## Descripción general

Adjunta una imagen latente y un valor sigma de degradación a los datos de CONDITIONING. Se utiliza para la decodificación o ampliación PiD (Pixel-in-Detail), permitiendo controlar cuánto se degrada el latente antes del procesamiento.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `positivo` | CONDITIONING | Sí | - | Los datos de condicionamiento a los que se adjuntarán el latente y el sigma de degradación. |
| `latent` | LATENT | Sí | - | La imagen latente (de VAEEncode o un KSampler) que se adjuntará al condicionamiento. |
| `formato_latent` | COMBO | Sí | `"flux"`<br>`"sd3"` | El formato del latente. Los latentes Flux1 y Flux2 se detectan automáticamente según la dimensión del canal. SD3 debe seleccionarse manualmente (predeterminado: "flux"). |
| `degrade_sigma` | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) | La cantidad de degradación a aplicar. 0 significa un latente limpio. Aumente este valor para eliminar el ruido de salidas latentes corruptas (predeterminado: 0.0). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Los datos de condicionamiento originales con los valores de latente y sigma de degradación adjuntos. |

---
**Source fingerprint (SHA-256):** `7c8de543629c2299fc2c1e035e433dfc249af594773a77e65c69dde67eb104d7`
