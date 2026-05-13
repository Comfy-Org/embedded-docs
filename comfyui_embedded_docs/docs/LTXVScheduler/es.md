> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/es.md)

El nodo `LTXVScheduler` genera valores sigma para procesos de muestreo personalizados. Calcula los parámetros del programa de ruido basándose en la cantidad de tokens en el latente de entrada y aplica una transformación sigmoide para crear el programa de muestreo. El nodo puede opcionalmente estirar los sigmas resultantes para que coincidan con un valor terminal especificado.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `pasos` | INT | Sí | 1-10000 | Número de pasos de muestreo (predeterminado: 20) |
| `max_desplazamiento` | FLOAT | Sí | 0.0-100.0 | Valor de desplazamiento máximo para el cálculo de sigma (predeterminado: 2.05) |
| `base_desplazamiento` | FLOAT | Sí | 0.0-100.0 | Valor de desplazamiento base para el cálculo de sigma (predeterminado: 0.95) |
| `estiramiento` | BOOLEAN | Sí | Verdadero/Falso | Estirar los sigmas para que estén en el rango [terminal, 1] (predeterminado: Verdadero) |
| `terminal` | FLOAT | Sí | 0.0-0.99 | El valor terminal de los sigmas después del estiramiento (predeterminado: 0.1) |
| `latente` | LATENT | No | - | Entrada latente opcional utilizada para calcular el recuento de tokens para el ajuste de sigma |

**Nota:** El parámetro `latent` es opcional. Cuando no se proporciona, el nodo utiliza un recuento de tokens predeterminado de 4096 para los cálculos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Valores sigma generados para el proceso de muestreo |

---
**Source fingerprint (SHA-256):** `3c7e8721fd75bfb0a253c38cd29e2ee1905bfe08193aa97dbaa959550aba34bc`
