# Aplicar Controlnet con VAE

Este nodo aplica la guía de ControlNet al condicionamiento de Stable Diffusion 3. Toma entradas de condicionamiento positivo y negativo junto con un modelo ControlNet y una imagen, y luego aplica la guía de control con parámetros ajustables de intensidad y temporización para influir en el proceso de generación.

**Nota:** Este nodo ha sido marcado como obsoleto y podría eliminarse en versiones futuras.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positive` | El condicionamiento positivo al que se aplicará la guía de ControlNet | CONDITIONING | Sí | - |
| `negative` | El condicionamiento negativo al que se aplicará la guía de ControlNet | CONDITIONING | Sí | - |
| `control_net` | El modelo ControlNet que se usará para la guía | CONTROL_NET | Sí | - |
| `vae` | El modelo VAE utilizado en el proceso | VAE | Sí | - |
| `image` | La imagen de entrada que ControlNet usará como guía | IMAGE | Sí | - |
| `strength` | La intensidad del efecto de ControlNet (por defecto: 1.0) | FLOAT | Sí | 0.0 - 10.0 |
| `start_percent` | El punto de inicio en el proceso de generación donde ControlNet comienza a aplicarse (por defecto: 0.0) | FLOAT | Sí | 0.0 - 1.0 |
| `end_percent` | El punto final en el proceso de generación donde ControlNet deja de aplicarse (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

**Nota:** Cuando `strength` se establece en 0, el nodo devuelve el condicionamiento positivo y negativo sin cambios, sin aplicar ControlNet.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `positive` | El condicionamiento positivo modificado con la guía de ControlNet aplicada | CONDITIONING |
| `negative` | El condicionamiento negativo modificado con la guía de ControlNet aplicada | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/es.md)

---
**Source fingerprint (SHA-256):** `b76b0683c05e38102280ca8b0bd23f39a9b9b1b4f52125c77c95686c0a06f398`
