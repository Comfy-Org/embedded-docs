Este nodo está diseñado para modificar el condicionamiento de un modelo generativo aplicando una máscara con una fuerza especificada a ciertas áreas. Permite ajustes dirigidos dentro del condicionamiento, habilitando un control más preciso sobre el proceso de generación.

## Entradas

### Requerido

| Parámetro     | Data Type | Descripción |
|---------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Los datos de condicionamiento a modificar. Sirve como base para aplicar la máscara y los ajustes de fuerza. |
| `máscara`        | `MASK`       | Un tensor de máscara que especifica las áreas dentro del condicionamiento a modificar. |
| `fuerza`    | `FLOAT`      | La fuerza del efecto de la máscara sobre el condicionamiento, permitiendo un ajuste fino de las modificaciones aplicadas. |
| `establecer_area_cond` | COMBO[STRING] | Determina si el efecto de la máscara se aplica al área predeterminada o está limitado por la propia máscara, ofreciendo flexibilidad para dirigir regiones específicas. |

## Salidas

| Parámetro     | Data Type | Descripción |
|---------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Los datos de condicionamiento modificados, con los ajustes de máscara y fuerza aplicados. |
