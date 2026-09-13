# CachéPerezoso

LazyCache es una versión experimental y casera de EasyCache que agrega almacenamiento en caché durante el muestreo para reducir el cómputo. Está diseñada para tener compatibilidad universal con los modelos en ComfyUI, aunque generalmente funciona peor que EasyCache y puede funcionar mejor solo en casos raros.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo al que se le agregará LazyCache. | MODEL | Sí | - |
| `reuse_threshold` | El umbral para reutilizar pasos en caché. Predeterminado: 0.2. | FLOAT | Sí | 0.0 - 3.0 (paso 0.01) |
| `start_percent` | El paso de muestreo relativo para comenzar a usar LazyCache. Predeterminado: 0.15. | FLOAT | Sí | 0.0 - 1.0 (paso 0.01) |
| `end_percent` | El paso de muestreo relativo para finalizar el uso de LazyCache. Predeterminado: 0.95. | FLOAT | Sí | 0.0 - 1.0 (paso 0.01) |
| `verbose` | Si se debe registrar información detallada. Predeterminado: False. | BOOLEAN | Sí | - |

Nota: `reuse_threshold`, `start_percent`, `end_percent` y `verbose` están marcados como entradas avanzadas.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo con la funcionalidad LazyCache agregada. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/es.md)

---
**Source fingerprint (SHA-256):** `78f9c13473567e068fc2be35b2f8f5aa459d43d3f13300a6ea858af98d3e2a44`
