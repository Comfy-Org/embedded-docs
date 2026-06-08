# Anulación de CFG

El nodo de Anulación de CFG permite establecer un valor fijo de escala CFG (Guía Libre de Clasificador) para un rango específico del proceso de muestreo, definido como un porcentaje del total de pasos. Cuando múltiples nodos de Anulación de CFG están conectados, el más cercano al muestreador en la cadena tiene prioridad para rangos superpuestos.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `modelo` | El modelo al que se aplicará la anulación de CFG | MODEL | Sí | |
| `cfg` | El valor fijo de escala CFG a utilizar durante el rango de anulación (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 100.0 |
| `porcentaje_inicio` | El punto de inicio del rango de anulación como porcentaje del proceso de muestreo (predeterminado: 0.0) | FLOAT | Sí | 0.0 a 1.0 |
| `porcentaje_fin` | El punto final del rango de anulación como porcentaje del proceso de muestreo (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|-------------|-------------|-----------|
| `MODEL` | El modelo con el envoltorio de anulación de CFG aplicado | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGOverride/es.md)

---
**Source fingerprint (SHA-256):** `1fe57a4e78a2f18c4e7da49fa7a6c473d64dc0ebf6662535dfb5379c37936662`
