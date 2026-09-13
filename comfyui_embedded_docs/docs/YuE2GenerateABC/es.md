# YuE2 Generar ABC

Este nodo genera notación ABC para una canción basada en una descripción de estilo y una letra, usando un modelo de texto y letras YuE2. La salida `abc` resultante se puede conectar al nodo YuE2 Generate Music para producir audio.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `clip` | El modelo YuE2 utilizado para tokenizar el estilo y la letra y generar la notación ABC. | CLIP | Sí | - |
| `style` | Texto que describe el estilo musical de la canción. | STRING | Sí | - |
| `lyrics` | Texto que contiene la letra de la canción. | STRING | Sí | - |
| `seed` | Semilla aleatoria utilizada para la generación. Cambiarla produce resultados diferentes. Predeterminado: 0. | INT | Sí | 0 a 18446744073709551615 |
| `mode` | full: genera melodía y acordes; melody: genera solo melodía, recomendado para covers. | COMBO | Sí | "full"<br>"melody" |
| `max_abc_tokens` | Número máximo de tokens generados para la notación ABC. Predeterminado: 8192. | INT | Sí | 1 a 20000 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `abc` | La notación ABC generada de la canción, que se puede conectar al nodo YuE2 Generate Music. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateABC/es.md)

---
**Source fingerprint (SHA-256):** `3e06f980a53e90b750f4190a95199e0e5ed1bd8c54d4dbf8485602ff1af00102`
