# Anulación de CFG

El nodo **CFG Override** permite establecer un valor fijo de CFG (*Classifier-Free Guidance*) para un rango específico del proceso de muestreo, definido como un porcentaje del total de pasos. Cuando se conectan varios nodos CFG Override, el que esté más cerca del muestreador en la cadena tendrá prioridad para los rangos superpuestos.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | El modelo al que se aplicará la anulación de CFG | MODEL | Sí | |
| `cfg` | El valor fijo de CFG que se usará durante el rango de anulación (por defecto: 1.0) | FLOAT | Sí | 0.0 a 100.0 |
| `start_percent` | El punto de inicio del rango de anulación como porcentaje del proceso de muestreo (por defecto: 0.0) | FLOAT | Sí | 0.0 a 1.0 |
| `end_percent` | El punto final del rango de anulación como porcentaje del proceso de muestreo (por defecto: 1.0) | FLOAT | Sí | 0.0 a 1.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `MODEL` | El modelo con la envoltura de anulación de CFG aplicada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGOverride/es.md)

---
**Source fingerprint (SHA-256):** `94c7d3751d90b42479f9cec4bdb3c95eeda405f51224f85d313ff12ec071ec58`
