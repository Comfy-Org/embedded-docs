# LTXVProgramador

El nodo LTXVScheduler genera valores sigma para procesos de muestreo personalizados. Calcula los parámetros del programa de ruido basándose en el recuento de tokens en el latente de entrada y aplica una transformación sigmoide para crear el programa de muestreo. El nodo puede opcionalmente estirar los sigmas resultantes para que coincidan con un valor terminal especificado.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `steps` | Número de pasos de muestreo (por defecto: 20) | INT | Sí | 1-10000 |
| `max_shift` | Valor máximo de desplazamiento para el cálculo de sigma (por defecto: 2.05) | FLOAT | Sí | 0.0-100.0 |
| `base_shift` | Valor base de desplazamiento para el cálculo de sigma (por defecto: 0.95) | FLOAT | Sí | 0.0-100.0 |
| `stretch` | Estirar los sigmas para que estén en el rango [terminal, 1] (por defecto: True) | BOOLEAN | Sí | True/False |
| `terminal` | El valor terminal de los sigmas después del estiramiento (por defecto: 0.1) | FLOAT | Sí | 0.0-0.99 |
| `latent` | Entrada latente opcional utilizada para calcular el recuento de tokens para el ajuste de sigma | LATENT | No | - |

**Nota:** El parámetro `latent` es opcional. Cuando no se proporciona, el nodo utiliza un recuento de tokens por defecto de 4096 para los cálculos.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `sigmas` | Valores sigma generados para el proceso de muestreo | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/es.md)

---
**Source fingerprint (SHA-256):** `5b4907e905e27a951c332c400e24023ef089df7a5f4a17b1fc8ba42a41302399`
