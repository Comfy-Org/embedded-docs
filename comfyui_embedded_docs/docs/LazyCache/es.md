> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/es.md)

LazyCache es una versión desarrollada internamente de EasyCache que proporciona una implementación aún más sencilla. Funciona con cualquier modelo en ComfyUI y añade funcionalidad de caché para reducir el cómputo durante el muestreo. Aunque generalmente tiene un rendimiento inferior a EasyCache, puede ser más efectivo en algunos casos raros y ofrece compatibilidad universal.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo al que añadir LazyCache. |
| `reuse_threshold` | FLOAT | No | 0.0 - 3.0 | El umbral para reutilizar pasos en caché (valor por defecto: 0.2). |
| `start_percent` | FLOAT | No | 0.0 - 1.0 | El paso de muestreo relativo para comenzar el uso de LazyCache (valor por defecto: 0.15). |
| `end_percent` | FLOAT | No | 0.0 - 1.0 | El paso de muestreo relativo para finalizar el uso de LazyCache (valor por defecto: 0.95). |
| `verbose` | BOOLEAN | No | - | Si se debe registrar información detallada (valor por defecto: False). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo con funcionalidad LazyCache añadida. |