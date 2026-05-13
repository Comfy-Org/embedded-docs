> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreSca/es.md)

El nodo FreSca aplica un escalado dependiente de la frecuencia a la guía durante el proceso de muestreo. Separa la señal de guía en componentes de baja y alta frecuencia mediante filtrado de Fourier, luego aplica diferentes factores de escalado a cada rango de frecuencia antes de recombinarlos. Esto permite un control más matizado sobre cómo la guía afecta diferentes aspectos de la salida generada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo al que se aplicará el escalado de frecuencia |
| `escala_baja` | FLOAT | No | 0 - 10 | Factor de escalado para componentes de baja frecuencia (predeterminado: 1.0) |
| `escala_alta` | FLOAT | No | 0 - 10 | Factor de escalado para componentes de alta frecuencia (predeterminado: 1.25) |
| `corte_frecuencia` | INT | No | 1 - 10000 | Número de índices de frecuencia alrededor del centro para considerar como baja frecuencia (predeterminado: 20) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `modelo` | MODEL | El modelo modificado con escalado dependiente de la frecuencia aplicado a su función de guía |

---
**Source fingerprint (SHA-256):** `254a28847e082739f80c9637d9657ef618d40db1862b6856c1cda22436438ded`
