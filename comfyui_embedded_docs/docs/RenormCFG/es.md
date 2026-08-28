# RenormCFG

El nodo RenormCFG modifica el proceso de guía sin clasificador (CFG) en modelos de difusión aplicando escalado condicional y normalización. Ajusta el proceso de eliminación de ruido basándose en umbrales de paso de tiempo especificados y factores de renomalización para controlar la influencia de las predicciones condicionales frente a las incondicionales durante la generación de imágenes.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de difusión al que se le aplica la CFG renomalizada | MODEL | Sí | - |
| `cfg_trunc` | Umbral de paso de tiempo para aplicar el escalado de CFG. Cuando el paso de tiempo actual está por debajo de este valor, se aplica el escalado de CFG; de lo contrario, solo se usa la predicción condicional (por defecto: 100.0) | FLOAT | No | 0.0 - 100.0 |
| `renorm_cfg` | Factor de renomalización que limita la norma máxima de la predicción escalada por CFG en relación con la predicción condicional original. Un valor de 0.0 desactiva la renomalización (por defecto: 1.0) | FLOAT | No | 0.0 - 100.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo modificado con la función de CFG renomalizada aplicada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/es.md)

---
**Source fingerprint (SHA-256):** `5925bdfe2d62ef7261d73cda661834102ae6600b1afe53f4093568a6e83ec2ab`
