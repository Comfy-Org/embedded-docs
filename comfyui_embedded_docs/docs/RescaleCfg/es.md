
El nodo RescaleCFG está diseñado para ajustar las escalas de condicionamiento y descondicionamiento de la salida de un modelo en función de un multiplicador especificado, con el objetivo de lograr un proceso de generación más equilibrado y controlado. Funciona reescalando la salida del modelo para modificar la influencia de los componentes condicionados y descondicionados, lo que potencialmente mejora el rendimiento o la calidad de salida del modelo.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `model`   | MODEL     | El parámetro del modelo representa el modelo generativo que se va a ajustar. Es crucial ya que el nodo aplica una función de reescalado a la salida del modelo, influyendo directamente en el proceso de generación. |
| `multiplier` | `FLOAT` | El parámetro multiplicador controla la extensión del reescalado aplicado a la salida del modelo. Determina el equilibrio entre los componentes originales y reescalados, afectando las características de la salida final. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `model`   | MODEL     | El modelo modificado con escalas de condicionamiento y descondicionamiento ajustadas. Se espera que este modelo produzca salidas con características potencialmente mejoradas debido al reescalado aplicado.
