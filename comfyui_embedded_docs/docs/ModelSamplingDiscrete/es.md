
Este nodo está diseñado para modificar el comportamiento de muestreo de un modelo aplicando una estrategia de muestreo discreto. Permite la selección de diferentes métodos de muestreo, como epsilon, v_prediction, lcm o x0, y ajusta opcionalmente la estrategia de reducción de ruido del modelo según la configuración del ratio de ruido cero disparo (zsnr).

## Entradas

| Parámetro | Tipo de Dato | Tipo Python     | Descripción |
|-----------|--------------|-------------------|-------------|
| `model`   | MODEL     | `torch.nn.Module` | El modelo al que se aplicará la estrategia de muestreo discreto. Este parámetro es crucial ya que define el modelo base que será modificado. |
| `sampling`| COMBO[STRING] | `str`           | Especifica el método de muestreo discreto que se aplicará al modelo. La elección del método afecta cómo el modelo genera muestras, ofreciendo diferentes estrategias para el muestreo. |
| `zsnr`    | `BOOLEAN`   | `bool`           | Un indicador booleano que, cuando está habilitado, ajusta la estrategia de reducción de ruido del modelo según el ratio de ruido cero disparo. Esto puede influir en la calidad y características de las muestras generadas. |

## Salidas

| Parámetro | Tipo de Dato | Tipo Python     | Descripción |
|-----------|-------------|-------------------|-------------|
| `model`   | MODEL     | `torch.nn.Module` | El modelo modificado con la estrategia de muestreo discreto aplicada. Este modelo ahora está equipado para generar muestras utilizando el método y ajustes especificados. |
