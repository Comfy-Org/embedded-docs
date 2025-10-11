> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/es.md)

El nodo EasyCache implementa un sistema de caché nativo para modelos con el fin de mejorar el rendimiento mediante la reutilización de pasos previamente calculados durante el proceso de muestreo. Añade funcionalidad EasyCache a un modelo con umbrales configurables para determinar cuándo comenzar y detener el uso de la caché durante la línea de tiempo de muestreo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo al que se añadirá EasyCache. |
| `reuse_threshold` | FLOAT | No | 0.0 - 3.0 | El umbral para reutilizar pasos en caché (valor por defecto: 0.2). |
| `start_percent` | FLOAT | No | 0.0 - 1.0 | El paso de muestreo relativo para comenzar el uso de EasyCache (valor por defecto: 0.15). |
| `end_percent` | FLOAT | No | 0.0 - 1.0 | El paso de muestreo relativo para finalizar el uso de EasyCache (valor por defecto: 0.95). |
| `verbose` | BOOLEAN | No | - | Si se debe registrar información detallada (valor por defecto: False). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo con la funcionalidad EasyCache añadida. |