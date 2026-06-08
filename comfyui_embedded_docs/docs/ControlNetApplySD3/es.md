Este nodo aplica la guía de ControlNet al condicionamiento de Stable Diffusion 3. Toma entradas de condicionamiento positivo y negativo junto con un modelo ControlNet y una imagen, luego aplica la guía de control con parámetros ajustables de intensidad y temporización para influir en el proceso de generación.

**Nota:** Este nodo ha sido marcado como obsoleto y podría eliminarse en versiones futuras.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | El condicionamiento positivo al que se aplicará la guía de ControlNet | CONDITIONING | Sí | - |
| `negativo` | El condicionamiento negativo al que se aplicará la guía de ControlNet | CONDITIONING | Sí | - |
| `control_net` | El modelo ControlNet que se utilizará para la guía | CONTROL_NET | Sí | - |
| `vae` | El modelo VAE utilizado en el proceso | VAE | Sí | - |
| `imagen` | La imagen de entrada que ControlNet utilizará como guía | IMAGE | Sí | - |
| `fuerza` | La intensidad del efecto de ControlNet (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 10.0 |
| `porcentaje_inicio` | El punto de inicio en el proceso de generación donde ControlNet comienza a aplicarse (predeterminado: 0.0) | FLOAT | Sí | 0.0 - 1.0 |
| `porcentaje_final` | El punto final en el proceso de generación donde ControlNet deja de aplicarse (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `negativo` | El condicionamiento positivo modificado con la guía de ControlNet aplicada | CONDITIONING |
| `negativo` | El condicionamiento negativo modificado con la guía de ControlNet aplicada | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/es.md)

---
**Source fingerprint (SHA-256):** `7bd24b19c159374bc86a773be9b563760bfae7e10d3333596788dbc52ef2f294`
