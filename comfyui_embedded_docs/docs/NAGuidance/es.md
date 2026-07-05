# Guía de Atención Normalizada

El nodo NAGuidance aplica Guía de Atención Normalizada a un modelo. Esta técnica permite el uso de indicaciones negativas con modelos destilados o rápidos modificando el mecanismo de atención del modelo durante el proceso de muestreo para dirigir la generación lejos de conceptos no deseados.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo al que se aplicará la Guía de Atención Normalizada. | MODEL | Sí | - |
| `escala_nag` | Factor de escala de la guía. Valores más altos alejan más la generación de la indicación negativa. (predeterminado: 5.0) | FLOAT | Sí | 0.0 - 50.0 |
| `nag_alpha` | Factor de mezcla para la atención normalizada. Un valor de 1.0 reemplaza completamente la atención original, mientras que 0.0 no tiene efecto. (predeterminado: 0.5) | FLOAT | Sí | 0.0 - 1.0 |
| `nag_tau` | Factor de escala utilizado para limitar la relación de normalización. (predeterminado: 1.5) | FLOAT | Sí | 1.0 - 10.0 |


| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model` | El modelo modificado con la Guía de Atención Normalizada habilitada. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NAGuidance/es.md)

---
**Source fingerprint (SHA-256):** `ea3d7fea94e62c8a0784887f3df9d8a503c3dbaa552bf860bd4dde1ae576fa9c`
