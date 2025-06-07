
Este nodo está diseñado para generar un muestrador para el modelo DPM++ SDE (Ecuación Diferencial Estocástica). Se adapta a entornos de ejecución tanto en CPU como en GPU, optimizando la implementación del muestrador según el hardware disponible.

## Entradas

| Parámetro      | Data Type | Descripción |
|----------------|-------------|-------------|
| `eta`          | FLOAT       | Especifica el tamaño del paso para el solucionador SDE, influyendo en la granularidad del proceso de muestreo.|
| `s_noise`      | FLOAT       | Determina el nivel de ruido que se aplicará durante el proceso de muestreo, afectando la diversidad de las muestras generadas.|
| `r`            | FLOAT       | Controla la proporción de reducción de ruido en el proceso de muestreo, impactando la claridad y calidad de las muestras generadas.|
| `noise_device` | COMBO[STRING]| Selecciona el entorno de ejecución (CPU o GPU) para el muestrador, optimizando el rendimiento según el hardware disponible.|

## Salidas

| Parámetro    | Data Type | Descripción |
|----------------|-------------|-------------|
| `sampler`    | SAMPLER     | El muestrador generado configurado con los parámetros especificados, listo para su uso en operaciones de muestreo. |
