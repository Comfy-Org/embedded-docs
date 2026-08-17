# Condicionamiento PiD

Adjunta una imagen latente y un valor de sigma de degradación a un dato CONDITIONING. Esto se utiliza para la decodificación PiD (Pixel-in-Detail) o el escalado, permitiéndote controlar cuánto se degrada el latente antes del procesamiento.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `positive` | Los datos de conditioning a los que se adjuntan el latente y el sigma de degradación. | CONDITIONING | Sí | - |
| `latent` | La imagen latente (de VAEEncode o un KSampler) que se adjunta al conditioning. | LATENT | Sí | - |
| `latent_format` | El formato del latente. Los latentes Flux1 (16 canales) y Flux2 (128 canales) se detectan automáticamente a partir de la dimensión de canales bajo "flux". Para SD3 (16 canales), SDXL (4 canales) o QwenImage (16 canales), seleccione manualmente (por defecto: "flux"). | COMBO | Sí | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | 0 = latente limpio. Aumente este valor para eliminar el ruido de salidas latentes corruptas (por defecto: 0.0). | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |

Nota: cuando `latent_format` es "flux", el nodo detecta automáticamente si el latente es Flux1 (16 canales) o Flux2 (128 canales) según su dimensión de canales. Si el latente procesado tiene 5 dimensiones, solo se utiliza el primer corte a lo largo de la última dimensión.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `CONDITIONING` | Los datos de conditioning originales con el latente y los valores de sigma de degradación adjuntos. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/es.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
