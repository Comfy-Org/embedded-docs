> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEqualizer3Band/es.md)

El nodo Ecualizador de Audio (3 Bandas) permite ajustar las frecuencias graves, medias y agudas de una forma de onda de audio. Aplica tres filtros separados: un filtro de estante bajo para los graves, un filtro de pico para los medios y un filtro de estante alto para los agudos. Cada banda puede controlarse de forma independiente con ajustes de ganancia, frecuencia y ancho de banda.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Sí | - | Los datos de audio de entrada que contienen la forma de onda y la frecuencia de muestreo. |
| `low_gain_dB` | FLOAT | No | -24.0 a 24.0 | Ganancia para las frecuencias bajas (Graves). Los valores positivos realzan, los valores negativos atenúan. (por defecto: 0.0) |
| `low_freq` | INT | No | 20 a 500 | Frecuencia de corte para el filtro de estante bajo en Hertz (Hz). (por defecto: 100) |
| `mid_gain_dB` | FLOAT | No | -24.0 a 24.0 | Ganancia para las frecuencias medias. Los valores positivos realzan, los valores negativos atenúan. (por defecto: 0.0) |
| `mid_freq` | INT | No | 200 a 4000 | Frecuencia central para el filtro de pico de medios en Hertz (Hz). (por defecto: 1000) |
| `mid_q` | FLOAT | No | 0.1 a 10.0 | Factor Q (ancho de banda) para el filtro de pico de medios. Valores más bajos crean una banda más ancha, valores más altos crean una banda más estrecha. (por defecto: 0.707) |
| `high_gain_dB` | FLOAT | No | -24.0 a 24.0 | Ganancia para las frecuencias altas (Agudos). Los valores positivos realzan, los valores negativos atenúan. (por defecto: 0.0) |
| `high_freq` | INT | No | 1000 a 15000 | Frecuencia de corte para el filtro de estante alto en Hertz (Hz). (por defecto: 5000) |

**Nota:** Los parámetros `low_gain_dB`, `mid_gain_dB` y `high_gain_dB` solo se aplican cuando su valor no es cero. Si una ganancia se establece en 0.0, se omite la etapa de filtro correspondiente.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `audio` | AUDIO | Los datos de audio procesados con la ecualización aplicada, que contienen la forma de onda modificada y la frecuencia de muestreo original. |