> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetLatentNoiseMask/es.md)

Este nodo está diseñado para aplicar una máscara de ruido a un conjunto de muestras latentes. Modifica las muestras de entrada integrando una máscara específica, alterando así sus características de ruido.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `muestras` | `LATENT`    | Las muestras latentes a las que se aplicará la máscara de ruido. Este parámetro es crucial para determinar el contenido base que será modificado. |
| `máscara`    | `MASK`      | La máscara que se aplicará a las muestras latentes. Define las áreas y la intensidad de la alteración del ruido dentro de las muestras. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Las muestras latentes modificadas con la máscara de ruido aplicada. |