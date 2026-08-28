# Anulación de CFG

El nodo CFG Override permite establecer un valor fijo de escala CFG (Classifier-Free Guidance) para un rango específico del proceso de muestreo, definido como un porcentaje del total de pasos. Cuando se conectan varios nodos CFG Override, el más cercano al muestreador en la cadena tiene prioridad para los rangos superpuestos.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `modelo` | El modelo al que se aplica la anulación de CFG | MODEL | Sí | |
| `cfg` | El valor fijo de escala CFG que se usará durante el rango de anulación (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 100.0 |
| `porcentaje_inicio` | El punto de inicio del rango de anulación como porcentaje del proceso de muestreo (predeterminado: 0.0) | FLOAT | Sí | 0.0 a 1.0 |
| `porcentaje_fin` | El punto de finalización del rango de anulación como porcentaje del proceso de muestreo (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `MODEL` | El modelo con el envoltorio de anulación de CFG aplicado | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGOverride/es.md)

---
**Source fingerprint (SHA-256):** `94c7d3751d90b42479f9cec4bdb3c95eeda405f51224f85d313ff12ec071ec58`
