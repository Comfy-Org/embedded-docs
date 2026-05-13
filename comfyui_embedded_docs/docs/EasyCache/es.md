> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/es.md)

El nodo EasyCache implementa un sistema de caché nativo para modelos con el fin de mejorar el rendimiento reutilizando pasos previamente calculados durante el proceso de muestreo. Añade la funcionalidad EasyCache a un modelo con umbrales configurables para determinar cuándo iniciar y detener el uso de la caché durante la línea de tiempo del muestreo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo al que se le añadirá EasyCache. |
| `umbral_de_reutilización` | FLOAT | No | 0.0 - 3.0 | El umbral para reutilizar pasos almacenados en caché (predeterminado: 0.2). |
| `porcentaje_inicial` | FLOAT | No | 0.0 - 1.0 | El paso de muestreo relativo para comenzar a usar EasyCache (predeterminado: 0.15). |
| `porcentaje_final` | FLOAT | No | 0.0 - 1.0 | El paso de muestreo relativo para finalizar el uso de EasyCache (predeterminado: 0.95). |
| `detallado` | BOOLEAN | No | - | Si se debe registrar información detallada (predeterminado: False). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `modelo` | MODEL | El modelo con la funcionalidad EasyCache añadida. |

---
**Source fingerprint (SHA-256):** `e9d9bf5ecae8034b562f1a27acf528d1f3241d7d28621beba149d3e9bd66a247`
