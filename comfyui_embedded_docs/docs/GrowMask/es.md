El nodo `GrowMask` está diseñado para modificar el tamaño de una máscara dada, ya sea expandiéndola o contrayéndola, mientras opcionalmente aplica un efecto de afinado a las esquinas. Esta funcionalidad es crucial para ajustar dinámicamente los límites de la máscara en tareas de procesamiento de imágenes, permitiendo un control más flexible y preciso sobre el área de interés.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `mask`    | MASK        | La máscara de entrada a modificar. Este parámetro es central para la operación del nodo, sirviendo como base sobre la cual la máscara se expande o contrae. |
| `expand`  | INT         | Determina la magnitud y dirección de la modificación de la máscara. Los valores positivos hacen que la máscara se expanda, mientras que los valores negativos conducen a la contracción. Este parámetro influye directamente en el tamaño final de la máscara. |
| `tapered_corners` | BOOLEAN    | Una bandera booleana que, cuando se establece en True, aplica un efecto de afinado a las esquinas de la máscara durante la modificación. Esta opción permite transiciones más suaves y resultados visualmente atractivos. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `mask`    | MASK        | La máscara modificada después de aplicar la expansión/contracción especificada y el efecto opcional de esquinas afinadas. |
