> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentConcat/es.md)

El nodo LatentConcat combina dos muestras latentes a lo largo de una dimensión especificada. Toma dos entradas latentes y las concatena a lo largo del eje elegido (dimensión x, y o t). El nodo ajusta automáticamente el tamaño del lote de la segunda entrada para que coincida con la primera entrada antes de realizar la operación de concatenación.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `samples1` | LATENT | Sí | - | La primera muestra latente a concatenar |
| `samples2` | LATENT | Sí | - | La segunda muestra latente a concatenar |
| `dim` | COMBO | Sí | `"x"`<br>`"-x"`<br>`"y"`<br>`"-y"`<br>`"t"`<br>`"-t"` | La dimensión a lo largo de la cual concatenar las muestras latentes. Los valores positivos concatenan samples1 antes de samples2, los valores negativos concatenan samples2 antes de samples1 |

**Nota:** La segunda muestra latente (`samples2`) se ajusta automáticamente para que coincida con el tamaño del lote de la primera muestra latente (`samples1`) antes de la concatenación.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | LATENT | Las muestras latentes concatenadas resultantes de combinar las dos muestras de entrada a lo largo de la dimensión especificada |
