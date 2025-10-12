> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/es.md)

El nodo AlignYourStepsScheduler genera valores sigma para el proceso de eliminación de ruido basándose en diferentes tipos de modelos. Calcula niveles de ruido apropiados para cada paso del proceso de muestreo y ajusta el número total de pasos según el parámetro de eliminación de ruido. Esto ayuda a alinear los pasos de muestreo con los requisitos específicos de los diferentes modelos de difusión.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `tipo_modelo` | STRING | COMBO | - | SD1, SDXL, SVD | Especifica el tipo de modelo a utilizar para el cálculo de sigma |
| `pasos` | INT | INT | 10 | 1-10000 | El número total de pasos de muestreo a generar |
| `desruido` | FLOAT | FLOAT | 1.0 | 0.0-1.0 | Controla cuánto eliminar el ruido de la imagen, donde 1.0 utiliza todos los pasos y valores más bajos utilizan menos pasos |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Devuelve los valores sigma calculados para el proceso de eliminación de ruido |
