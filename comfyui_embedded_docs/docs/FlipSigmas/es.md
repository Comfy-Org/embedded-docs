El nodo `FlipSigmas` está diseñado para manipular la secuencia de valores sigma utilizados en modelos de difusión invirtiendo su orden y asegurando que el primer valor no sea cero si originalmente lo era. Esta operación es crucial para adaptar los niveles de ruido en orden inverso, facilitando el proceso de generación en modelos que operan reduciendo gradualmente el ruido de los datos.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `sigmas`  | `SIGMAS`    | El parámetro 'sigmas' representa la secuencia de valores sigma que se va a invertir. Esta secuencia es crucial para controlar los niveles de ruido aplicados durante el proceso de difusión, y su inversión es esencial para el proceso de generación inversa. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `sigmas`  | `SIGMAS`    | La salida es la secuencia modificada de valores sigma, invertida y ajustada para asegurar que el primer valor no sea cero si originalmente lo era, lista para su uso en operaciones posteriores del modelo de difusión. |
