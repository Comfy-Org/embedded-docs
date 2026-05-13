> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/es.md)

El nodo ModelSamplingSD3 aplica parámetros de muestreo de Stable Diffusion 3 a un modelo. Modifica el comportamiento de muestreo del modelo ajustando el parámetro de desplazamiento, que controla las características de la distribución de muestreo. El nodo crea una copia modificada del modelo de entrada con la configuración de muestreo especificada aplicada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo de entrada al que se aplicarán los parámetros de muestreo SD3 |
| `shift` | FLOAT | Sí | 0.0 - 100.0 | Controla el parámetro de desplazamiento del muestreo (valor predeterminado: 3.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `model` | MODEL | El modelo modificado con los parámetros de muestreo SD3 aplicados |

---
**Source fingerprint (SHA-256):** `aa2172d578badffb0a728308b0d3aae4d048db074336963965264d5e512a0d93`
