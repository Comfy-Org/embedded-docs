# LTXVProgramador

El nodo `LTXVScheduler` genera valores sigma para procesos de muestreo personalizados. Calcula los parámetros del programa de ruido basándose en la cantidad de tokens en el latente de entrada y aplica una transformación sigmoide para crear el programa de muestreo. El nodo puede opcionalmente estirar los sigmas resultantes para que coincidan con un valor terminal especificado.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `pasos` | Número de pasos de muestreo (predeterminado: 20) | INT | Sí | 1-10000 |
| `max_desplazamiento` | Valor de desplazamiento máximo para el cálculo de sigma (predeterminado: 2.05) | FLOAT | Sí | 0.0-100.0 |
| `base_desplazamiento` | Valor de desplazamiento base para el cálculo de sigma (predeterminado: 0.95) | FLOAT | Sí | 0.0-100.0 |
| `estiramiento` | Estirar los sigmas para que estén en el rango [terminal, 1] (predeterminado: Verdadero) | BOOLEAN | Sí | Verdadero/Falso |
| `terminal` | El valor terminal de los sigmas después del estiramiento (predeterminado: 0.1) | FLOAT | Sí | 0.0-0.99 |
| `latente` | Entrada latente opcional utilizada para calcular el recuento de tokens para el ajuste de sigma | LATENT | No | - |

**Nota:** El parámetro `latent` es opcional. Cuando no se proporciona, el nodo utiliza un recuento de tokens predeterminado de 4096 para los cálculos.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `sigmas` | Valores sigma generados para el proceso de muestreo | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/es.md)

---
**Source fingerprint (SHA-256):** `3c7e8721fd75bfb0a253c38cd29e2ee1905bfe08193aa97dbaa959550aba34bc`
