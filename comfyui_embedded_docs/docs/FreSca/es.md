> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreSca/es.md)

El nodo FreSca aplica escalado dependiente de la frecuencia a la guía durante el proceso de muestreo. Separa la señal de guía en componentes de baja frecuencia y alta frecuencia utilizando filtrado de Fourier, luego aplica diferentes factores de escala a cada rango de frecuencia antes de recombinarlos. Esto permite un control más matizado sobre cómo la guía afecta diferentes aspectos de la salida generada.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo al que aplicar el escalado de frecuencia |
| `scale_low` | FLOAT | No | 0-10 | Factor de escala para componentes de baja frecuencia (por defecto: 1.0) |
| `scale_high` | FLOAT | No | 0-10 | Factor de escala para componentes de alta frecuencia (por defecto: 1.25) |
| `freq_cutoff` | INT | No | 1-10000 | Número de índices de frecuencia alrededor del centro a considerar como baja frecuencia (por defecto: 20) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo modificado con escalado dependiente de la frecuencia aplicado a su función de guía |