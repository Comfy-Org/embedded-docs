# Concatenar AV Latent

El nodo LTXVConcatAVLatent fusiona un latente de video y un latente de audio en un único latente conjunto para su uso con modelos audiovisuales como LTXV o MiniMax H3. Agrupa los `samples` de ambas entradas y, si alguna de las entradas incluye un `noise_mask`, también se agrupan esas máscaras. Si el latente de video ya es un latente AV, el nodo conserva su flujo de video y reemplaza su flujo de audio con el latente de audio proporcionado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `video_latent` | Representación latente de los datos de video. | LATENT | Sí |  |
| `audio_latent` | Representación latente de los datos de audio que se combinarán con el latente de video. | LATENT | Sí |  |

**Nota sobre la longitud del audio:** Cuando `video_latent` ya es un latente AV, `audio_latent` debe coincidir con el flujo de audio incrustado en todas las dimensiones excepto una. El nodo recorta o rellena con ceros el audio a lo largo de esa dimensión para ajustarse a la longitud del flujo existente. La cola rellenada se deja sin máscara para que el modelo pueda generarla.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `latent` | Un latente que contiene los `samples` de video y audio emparejados. Si cualquiera de las entradas proporciona un `noise_mask`, la salida también contiene un `noise_mask` emparejado; una máscara faltante se reemplaza por unos. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/es.md)

---
**Source fingerprint (SHA-256):** `0231f9db2ce73132d8555fbb33f295b68aa68a0c1c54e4a0c5d2e1f67b5611cb`
