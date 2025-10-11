> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DifferentialDiffusion/es.md)

El nodo Differential Diffusion modifica el proceso de eliminación de ruido aplicando una máscara binaria basada en umbrales de paso de tiempo. Crea una máscara que combina entre la máscara de eliminación de ruido original y una máscara binaria basada en umbrales, permitiendo un ajuste controlado de la fuerza del proceso de difusión.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo de difusión a modificar |
| `strength` | FLOAT | No | 0.0 - 1.0 | Controla la fuerza de mezcla entre la máscara de eliminación de ruido original y la máscara binaria de umbral (valor por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo de difusión modificado con la función de máscara de eliminación de ruido actualizada |