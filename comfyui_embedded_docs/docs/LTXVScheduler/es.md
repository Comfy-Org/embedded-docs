> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/es.md)

El nodo LTXVScheduler genera valores sigma para procesos de muestreo personalizados. Calcula parámetros de programación de ruido basados en el número de tokens en el latente de entrada y aplica una transformación sigmoide para crear la programación de muestreo. El nodo puede opcionalmente estirar los sigmas resultantes para coincidir con un valor terminal especificado.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `pasos` | INT | Sí | 1-10000 | Número de pasos de muestreo (valor por defecto: 20) |
| `max_desplazamiento` | FLOAT | Sí | 0.0-100.0 | Valor de desplazamiento máximo para el cálculo de sigma (valor por defecto: 2.05) |
| `base_desplazamiento` | FLOAT | Sí | 0.0-100.0 | Valor de desplazamiento base para el cálculo de sigma (valor por defecto: 0.95) |
| `estiramiento` | BOOLEAN | Sí | True/False | Estirar los sigmas para que estén en el rango [terminal, 1] (valor por defecto: True) |
| `terminal` | FLOAT | Sí | 0.0-0.99 | El valor terminal de los sigmas después del estiramiento (valor por defecto: 0.1) |
| `latente` | LATENT | No | - | Entrada latente opcional utilizada para calcular el recuento de tokens para el ajuste de sigma |

**Nota:** El parámetro `latent` es opcional. Cuando no se proporciona, el nodo utiliza un recuento de tokens predeterminado de 4096 para los cálculos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Valores sigma generados para el proceso de muestreo |
