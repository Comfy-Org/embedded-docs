El nodo LatentComposite está diseñado para mezclar o fusionar dos representaciones latentes en una sola salida. Este proceso es esencial para crear imágenes o características compuestas combinando las características de las latentes de entrada de manera controlada.

## Entradas

| Parámetro    | Data Type | Descripción |
|--------------|-------------|-------------|
| `samples_to` | `LATENT`    | La representación latente 'samples_to' donde se compondrá 'samples_from'. Sirve como base para la operación de composición. |
| `samples_from` | `LATENT` | La representación latente 'samples_from' que se compondrá sobre 'samples_to'. Contribuye con sus características al resultado final compuesto. |
| `x`          | `INT`      | La coordenada x (posición horizontal) donde se colocará la latente 'samples_from' sobre 'samples_to'. Determina la alineación horizontal del compuesto. |
| `y`          | `INT`      | La coordenada y (posición vertical) donde se colocará la latente 'samples_from' sobre 'samples_to'. Determina la alineación vertical del compuesto. |
| `feather`    | `INT`      | Un booleano que indica si la latente 'samples_from' debe ser redimensionada para coincidir con 'samples_to' antes de componer. Esto puede afectar la escala y proporción del resultado compuesto. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La salida es una representación latente compuesta, mezclando las características de las latentes 'samples_to' y 'samples_from' según las coordenadas especificadas y la opción de redimensionamiento. |
