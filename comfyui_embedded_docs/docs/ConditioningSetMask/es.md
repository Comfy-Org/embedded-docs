> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetMask/es.md)

Este nodo está diseñado para modificar el condicionamiento de un modelo generativo aplicando una máscara con una intensidad específica a ciertas áreas. Permite realizar ajustes dirigidos dentro del condicionamiento, brindando un control más preciso sobre el proceso de generación.

## Entradas

### Obligatorias

| Parámetro      | Tipo de Dato | Descripción |
|----------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Los datos de condicionamiento que se modificarán. Sirven como base para aplicar la máscara y los ajustes de intensidad. |
| `mask`         | `MASK`       | Un tensor de máscara que especifica las áreas dentro del condicionamiento que se modificarán. |
| `strength`     | `FLOAT`      | La intensidad del efecto de la máscara sobre el condicionamiento, lo que permite un ajuste fino de las modificaciones aplicadas. |
| `set_cond_area` | COMBO[STRING] | Determina si el efecto de la máscara se aplica al área predeterminada o está limitado por la propia máscara, ofreciendo flexibilidad para apuntar a regiones específicas. |

## Salidas

| Parámetro      | Tipo de Dato | Descripción |
|----------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Los datos de condicionamiento modificados, con los ajustes de máscara e intensidad aplicados. |