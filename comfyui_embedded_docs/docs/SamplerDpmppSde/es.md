# SamplerDpmppSde

Este nodo está diseñado para generar un muestreador para el modelo DPM++ SDE (Ecuación Diferencial Estocástica). Se adapta tanto a entornos de ejecución en CPU como en GPU, optimizando la implementación del muestreador según el hardware disponible.

## Entradas

| Parámetro | Descripción | Tipo de Dato |
| --- | --- | --- |
| `eta` | Especifica el tamaño de paso para el solucionador SDE, influyendo en la granularidad del proceso de muestreo. | FLOAT |
| `s_noise` | Determina el nivel de ruido que se aplicará durante el proceso de muestreo, afectando la diversidad de las muestras generadas. | FLOAT |
| `r` | Controla la proporción de reducción de ruido en el proceso de muestreo, impactando la claridad y calidad de las muestras generadas. | FLOAT |
| `noise_device` | Selecciona el entorno de ejecución (CPU o GPU) para el muestreador, optimizando el rendimiento según el hardware disponible. | COMBO[STRING] |

## Salidas

| Parámetro | Descripción | Tipo de Dato |
| --- | --- | --- |
| `sampler` | El muestreador generado configurado con los parámetros especificados, listo para usar en operaciones de muestreo. | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDpmppSde/es.md)
