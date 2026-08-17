# RenormCFG

The RenormCFG node modifies the classifier-free guidance (CFG) process in diffusion models by applying conditional scaling and normalization. It adjusts the denoising process based on specified timestep thresholds and renormalization factors to control the influence of conditional versus unconditional predictions during image generation.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de difusión al que se le aplica el CFG renormalizado | MODEL | Sí | - |
| `cfg_trunc` | Umbral de paso de tiempo para aplicar el escalado de CFG. Cuando el paso de tiempo actual está por debajo de este valor, se aplica el escalado de CFG; de lo contrario, solo se usa la predicción condicional (valor por defecto: 100.0) | FLOAT | No | 0.0 - 100.0 |
| `renorm_cfg` | Factor de renormalización que limita la norma máxima de la predicción escalada por CFG en relación con la predicción condicional original. Un valor de 0.0 desactiva la renormalización (valor por defecto: 1.0) | FLOAT | No | 0.0 - 100.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `model` | El modelo modificado con la función de CFG renormalizada aplicada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/es.md)

---
**Source fingerprint (SHA-256):** `5925bdfe2d62ef7261d73cda661834102ae6600b1afe53f4093568a6e83ec2ab`
