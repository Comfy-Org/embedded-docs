> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingDiscrete/es.md)

Este nodo está diseñado para modificar el comportamiento de muestreo de un modelo aplicando una estrategia de muestreo discreto. Permite seleccionar diferentes métodos de muestreo, como epsilon, v_prediction, lcm o x0, y opcionalmente ajusta la estrategia de reducción de ruido del modelo según la configuración de la relación de ruido cero-shot (zsnr).

## Entradas

| Parámetro | Tipo de dato | Python dtype     | Descripción |
|-----------|--------------|-------------------|-------------|
| `modelo`   | MODEL     | `torch.nn.Module` | El modelo al que se aplicará la estrategia de muestreo discreto. Este parámetro es crucial ya que define el modelo base que será modificado. |
| `muestreo`| COMBO[STRING] | `str`           | Especifica el método de muestreo discreto que se aplicará al modelo. La elección del método afecta la forma en que el modelo genera muestras, ofreciendo diferentes estrategias de muestreo. |
| `zsnr`    | `BOOLEAN`   | `bool`           | Una bandera booleana que, cuando está habilitada, ajusta la estrategia de reducción de ruido del modelo según la relación de ruido cero-shot. Esto puede influir en la calidad y las características de las muestras generadas. |

## Salidas

| Parámetro | Tipo de dato | Python dtype     | Descripción |
|-----------|-------------|-------------------|-------------|
| `modelo`   | MODEL     | `torch.nn.Module` | El modelo modificado con la estrategia de muestreo discreto aplicada. Este modelo ahora está preparado para generar muestras utilizando el método y los ajustes especificados. |