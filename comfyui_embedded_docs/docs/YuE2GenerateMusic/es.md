# YuE2 Generar música

Genera tokens musicales y condicionamiento acústico a partir de un estilo, una letra y una notación ABC. Devuelve el condicionamiento y la duración generada en segundos, los cuales deben proporcionarse al nodo Empty YuE2 Latent Audio. Si la entrada ABC se deja vacía, se ignora el modo seleccionado y se usa automáticamente el modo off.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `clip` | El modelo CLIP utilizado para tokenizar y codificar las entradas musicales. | CLIP | Sí | - |
| `style` | Texto que describe el estilo musical. Admite entrada multilínea y prompts dinámicos. | STRING | Sí | Texto multilínea |
| `lyrics` | Letra para la música generada. Admite entrada multilínea y prompts dinámicos. | STRING | Sí | Texto multilínea |
| `abc` | Conecte el generador ABC o proporcione una partitura editada. Déjelo vacío para usar el modo off automáticamente. predeterminado: "" | STRING | Sí | Texto multilínea |
| `seed` | Semilla aleatoria para la generación. predeterminado: 0 | INT | Sí | 0 a 18446744073709551615 |
| `mode` | full: genera melodía y acordes; melody: genera solo melodía, recomendado para versiones. predeterminado: "full" | COMBO | Sí | "full"<br>"melody" |
| `max_duration` | Duración máxima en segundos. Se reduce automáticamente para prompts largos; la generación puede detenerse antes. predeterminado: 360.0 | FLOAT | Sí | 0.04 a 900.0 |
| `temperature` | Temperatura de muestreo para la generación. predeterminado: 1.0 (avanzado) | FLOAT | Sí | 0.0 a 5.0 |
| `top_p` | Umbral de probabilidad del muestreo de núcleo (nucleus sampling). predeterminado: 0.95 (avanzado) | FLOAT | Sí | 0.01 a 1.0 |
| `top_k` | Límite de muestreo top-k. predeterminado: 100 (avanzado) | INT | Sí | 1 a 32768 |
| `repetition_penalty` | Penalización aplicada a los tokens repetidos. predeterminado: 1.2 (avanzado) | FLOAT | Sí | 0.01 a 10.0 |

Nota: Si `abc` está vacío o contiene solo espacios en blanco, la selección de `mode` se ignora y se usa automáticamente el modo off.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `CONDITIONING` | Condicionamiento acústico generado a partir de los tokens musicales. | CONDITIONING |
| `seconds` | La duración de audio generada en segundos. Proporcione este valor al nodo Empty YuE2 Latent Audio. | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateMusic/es.md)

---
**Source fingerprint (SHA-256):** `54f5d46cf083726bdf97c86e5683b2727840f75bb553bddf9525cfbf5affa44c`
