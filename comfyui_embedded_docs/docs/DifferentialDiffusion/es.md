> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DifferentialDiffusion/es.md)

El nodo Difusión Diferencial modifica el proceso de eliminación de ruido aplicando una máscara binaria basada en umbrales de paso de tiempo. Crea una máscara que combina entre la máscara de eliminación de ruido original y una máscara binaria basada en umbrales, permitiendo un ajuste controlado de la intensidad del proceso de difusión.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo de difusión a modificar |
| `intensidad` | FLOAT | No | 0.0 - 1.0 | Controla la intensidad de combinación entre la máscara de eliminación de ruido original y la máscara binaria de umbral (predeterminado: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `modelo` | MODEL | El modelo de difusión modificado con la función de máscara de eliminación de ruido actualizada |

---
**Source fingerprint (SHA-256):** `3b1727baa6c546516f5dfb53e6e39f27fc7429cde2ac7fd7dfbab99eebb39816`
