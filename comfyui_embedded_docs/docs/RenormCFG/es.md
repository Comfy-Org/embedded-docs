> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/es.md)

El nodo RenormCFG modifica el proceso de guía libre de clasificador (CFG) en modelos de difusión aplicando escalado y normalización condicional. Ajusta el proceso de eliminación de ruido basándose en umbrales de paso de tiempo especificados y factores de renormalización para controlar la influencia de las predicciones condicionales versus las incondicionales durante la generación de imágenes.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo de difusión al que aplicar CFG renormalizado |
| `cfg_trunc` | FLOAT | No | 0.0 - 100.0 | Umbral de paso de tiempo para aplicar el escalado CFG (por defecto: 100.0) |
| `renorm_cfg` | FLOAT | No | 0.0 - 100.0 | Factor de renormalización para controlar la fuerza de la guía condicional (por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `modelo` | MODEL | El modelo modificado con la función CFG renormalizada aplicada |
