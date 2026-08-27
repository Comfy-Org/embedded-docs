# CachéPerezoso

LazyCache es una versión casera de EasyCache que ofrece una implementación aún más fácil. Funciona con cualquier modelo en ComfyUI y añade funcionalidad de caché para reducir el cómputo durante el muestreo. Aunque generalmente rinde peor que EasyCache, puede ser más eficaz en algunos casos raros y ofrece compatibilidad universal.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo al que añadir LazyCache. | MODEL | Sí | - |
| `umbral_reutilización` | El umbral para reutilizar pasos almacenados en caché (predeterminado: 0.2). | FLOAT | No | 0.0 - 3.0 |
| `porcentaje_inicio` | El paso de muestreo relativo para comenzar a usar LazyCache (predeterminado: 0.15). | FLOAT | No | 0.0 - 1.0 |
| `porcentaje_fin` | El paso de muestreo relativo para finalizar el uso de LazyCache (predeterminado: 0.95). | FLOAT | No | 0.0 - 1.0 |
| `detallado` | Si se registra información detallada (predeterminado: False). | BOOLEAN | No | - |

Nota: `reuse_threshold`, `start_percent`, `end_percent` y `verbose` son opciones avanzadas opcionales.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo con la funcionalidad de LazyCache añadida. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/es.md)

---
**Source fingerprint (SHA-256):** `78f9c13473567e068fc2be35b2f8f5aa459d43d3f13300a6ea858af98d3e2a44`
