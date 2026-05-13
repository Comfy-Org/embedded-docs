> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEqualizer3Band/es.md)

# Ecualizador de Audio (3 Bandas)

El nodo Ecualizador de Audio (3 Bandas) permite ajustar las frecuencias graves, medias y agudas de una forma de onda de audio. Aplica tres filtros separados: un filtro shelving bajo para graves, un filtro peak para medios y un filtro shelving alto para agudos. Cada banda puede controlarse de forma independiente con ajustes de ganancia, frecuencia y ancho de banda.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `audio` | AUDIO | Sí | - | Los datos de audio de entrada que contienen la forma de onda y la frecuencia de muestreo. |
| `low_gain_dB` | FLOAT | No | -24.0 a 24.0 | Ganancia para frecuencias bajas (Graves). Los valores positivos amplifican, los negativos atenúan. (predeterminado: 0.0) |
| `low_freq` | INT | No | 20 a 500 | Frecuencia de corte para el filtro shelving bajo en Hertz (Hz). (predeterminado: 100) |
| `mid_gain_dB` | FLOAT | No | -24.0 a 24.0 | Ganancia para frecuencias medias. Los valores positivos amplifican, los negativos atenúan. (predeterminado: 0.0) |
| `mid_freq` | INT | No | 200 a 4000 | Frecuencia central para el filtro peak de medios en Hertz (Hz). (predeterminado: 1000) |
| `mid_q` | FLOAT | No | 0.1 a 10.0 | Factor Q (ancho de banda) para el filtro peak de medios. Los valores más bajos crean una banda más ancha, los valores más altos crean una banda más estrecha. (predeterminado: 0.707) |
| `high_gain_dB` | FLOAT | No | -24.0 a 24.0 | Ganancia para frecuencias altas (Agudos). Los valores positivos amplifican, los negativos atenúan. (predeterminado: 0.0) |
| `high_freq` | INT | No | 1000 a 15000 | Frecuencia de corte para el filtro shelving alto en Hertz (Hz). (predeterminado: 5000) |

**Nota:** Los parámetros `low_gain_dB`, `mid_gain_dB` y `high_gain_dB` solo se aplican cuando su valor no es cero. Si una ganancia se establece en 0.0, la etapa de filtro correspondiente se omite.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `audio` | AUDIO | Los datos de audio procesados con la ecualización aplicada, que contienen la forma de onda modificada y la frecuencia de muestreo original. |

---
**Source fingerprint (SHA-256):** `7aeaec2959f1af6144e46d8e6c558a16193669846923df1db23ae9d47e5cc173`
