LazyCache es una versión casera de EasyCache que ofrece una implementación aún más sencilla. Funciona con cualquier modelo en ComfyUI y añade funcionalidad de caché para reducir el cómputo durante el muestreo. Aunque generalmente tiene un rendimiento inferior al de EasyCache, puede ser más efectivo en algunos casos poco comunes y ofrece compatibilidad universal.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo al que se le añadirá LazyCache. | MODEL | Sí | - |
| `umbral_reutilización` | El umbral para reutilizar pasos almacenados en caché (predeterminado: 0.2). | FLOAT | No | 0.0 - 3.0 |
| `porcentaje_inicio` | El paso de muestreo relativo para comenzar a usar LazyCache (predeterminado: 0.15). | FLOAT | No | 0.0 - 1.0 |
| `porcentaje_fin` | El paso de muestreo relativo para finalizar el uso de LazyCache (predeterminado: 0.95). | FLOAT | No | 0.0 - 1.0 |
| `detallado` | Si se debe registrar información detallada (predeterminado: False). | BOOLEAN | No | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `modelo` | El modelo con la funcionalidad LazyCache añadida. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/es.md)

---
**Source fingerprint (SHA-256):** `72a5e85b7cf517e88583fc1b75d3ab4a5d40fe8604d50c34f555e677d2ea9e51`
