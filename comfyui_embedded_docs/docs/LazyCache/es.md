# CachéPerezoso

LazyCache es una versión casera de EasyCache que ofrece una implementación aún más sencilla. Funciona con cualquier modelo en ComfyUI y añade funcionalidad de caché para reducir el cómputo durante el muestreo. Aunque generalmente rinde peor que EasyCache, puede ser más efectivo en algunos casos raros y ofrece compatibilidad universal.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo al que se le añade LazyCache. | MODEL | Sí | - |
| `reuse_threshold` | El umbral para reutilizar pasos almacenados en caché (predeterminado: 0.2). | FLOAT | No | 0.0 - 3.0 |
| `start_percent` | El paso de muestreo relativo para comenzar el uso de LazyCache (predeterminado: 0.15). | FLOAT | No | 0.0 - 1.0 |
| `end_percent` | El paso de muestreo relativo para finalizar el uso de LazyCache (predeterminado: 0.95). | FLOAT | No | 0.0 - 1.0 |
| `verbose` | Si se debe registrar información detallada (predeterminado: False). | BOOLEAN | No | - |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `model` | El modelo con la funcionalidad LazyCache añadida. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/es.md)

---
**Source fingerprint (SHA-256):** `78f9c13473567e068fc2be35b2f8f5aa459d43d3f13300a6ea858af98d3e2a44`
