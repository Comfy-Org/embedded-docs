> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/es.md)

Este nodo aplica la guía de ControlNet al condicionamiento de Stable Diffusion 3. Toma entradas de condicionamiento positivo y negativo junto con un modelo ControlNet y una imagen, luego aplica la guía de control con parámetros ajustables de intensidad y temporización para influir en el proceso de generación.

**Nota:** Este nodo ha sido marcado como obsoleto y podría eliminarse en versiones futuras.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | El condicionamiento positivo al que se aplicará la guía de ControlNet |
| `negative` | CONDITIONING | Sí | - | El condicionamiento negativo al que se aplicará la guía de ControlNet |
| `control_net` | CONTROL_NET | Sí | - | El modelo ControlNet que se utilizará para la guía |
| `vae` | VAE | Sí | - | El modelo VAE utilizado en el proceso |
| `image` | IMAGE | Sí | - | La imagen de entrada que ControlNet utilizará como guía |
| `strength` | FLOAT | Sí | 0.0 - 10.0 | La intensidad del efecto de ControlNet (predeterminado: 1.0) |
| `start_percent` | FLOAT | Sí | 0.0 - 1.0 | El punto de inicio en el proceso de generación donde ControlNet comienza a aplicarse (predeterminado: 0.0) |
| `end_percent` | FLOAT | Sí | 0.0 - 1.0 | El punto final en el proceso de generación donde ControlNet deja de aplicarse (predeterminado: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `positive` | CONDITIONING | El condicionamiento positivo modificado con la guía de ControlNet aplicada |
| `negative` | CONDITIONING | El condicionamiento negativo modificado con la guía de ControlNet aplicada |

---
**Source fingerprint (SHA-256):** `7bd24b19c159374bc86a773be9b563760bfae7e10d3333596788dbc52ef2f294`
