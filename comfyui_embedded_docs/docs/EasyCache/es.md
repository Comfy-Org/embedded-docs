El nodo EasyCache implementa un sistema de caché nativo para modelos con el fin de mejorar el rendimiento reutilizando pasos previamente calculados durante el proceso de muestreo. Añade la funcionalidad EasyCache a un modelo con umbrales configurables para determinar cuándo iniciar y detener el uso de la caché durante la línea de tiempo del muestreo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo al que se le añadirá EasyCache. | MODEL | Sí | - |
| `umbral_de_reutilización` | El umbral para reutilizar pasos almacenados en caché (predeterminado: 0.2). | FLOAT | No | 0.0 - 3.0 |
| `porcentaje_inicial` | El paso de muestreo relativo para comenzar a usar EasyCache (predeterminado: 0.15). | FLOAT | No | 0.0 - 1.0 |
| `porcentaje_final` | El paso de muestreo relativo para finalizar el uso de EasyCache (predeterminado: 0.95). | FLOAT | No | 0.0 - 1.0 |
| `detallado` | Si se debe registrar información detallada (predeterminado: False). | BOOLEAN | No | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `modelo` | El modelo con la funcionalidad EasyCache añadida. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/es.md)

---
**Source fingerprint (SHA-256):** `e9d9bf5ecae8034b562f1a27acf528d1f3241d7d28621beba149d3e9bd66a247`
