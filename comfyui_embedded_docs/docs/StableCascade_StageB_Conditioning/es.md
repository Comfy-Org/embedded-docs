> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/es.md)

El nodo StableCascade_StageB_Conditioning prepara los datos de condicionamiento para la generación de la Etapa B de Stable Cascade combinando la información de condicionamiento existente con las representaciones latentes previas de la Etapa C. Modifica los datos de condicionamiento para incluir las muestras latentes de la Etapa C, permitiendo que el proceso de generación aproveche la información previa para obtener resultados más coherentes.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | Sí | - | Los datos de condicionamiento que serán modificados con la información previa de la Etapa C |
| `stage_c` | LATENT | Sí | - | La representación latente de la Etapa C que contiene las muestras previas para el condicionamiento |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Los datos de condicionamiento modificados con la información previa de la Etapa C integrada |