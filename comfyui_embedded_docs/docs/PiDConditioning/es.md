# Condicionamiento PiD

Adjunta una imagen latente y un valor de sigma de degradación a un dato de CONDITIONING. Esto se utiliza para la decodificación o ampliación PiD (Pixel-in-Detail), permitiéndote controlar cuánto se degrada el latente antes del procesamiento.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `positivo` | Los datos de condicionamiento a los que se adjuntan el latente y el sigma de degradación. | CONDITIONING | Sí | - |
| `latent` | El latente (de VAEEncode o un KSampler) que se adjunta al condicionamiento. | LATENT | Sí | - |
| `formato_latent` | El formato del latente. Los latentes Flux1 (16 canales) y Flux2 (128 canales) se detectan automáticamente a partir de la dimensión de canales bajo "flux". Para SD3 (16 canales), SDXL (4 canales) o QwenImage (16 canales), selecciona manualmente (predeterminado: "flux"). | COMBO | Sí | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | La cantidad de degradación a aplicar. 0 significa un latente limpio. Aumenta este valor para eliminar el ruido de salidas latentes corruptas (predeterminado: 0.0). | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |

Nota: Cuando `latent_format` está establecido en `"flux"`, el nodo detecta automáticamente el tipo de latente a partir de la dimensión de canales: 128 canales se tratan como latentes Flux2, mientras que 16 canales se tratan como latentes Flux1.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `CONDITIONING` | Los datos de condicionamiento originales con los valores de latente y sigma de degradación adjuntos. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/es.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
