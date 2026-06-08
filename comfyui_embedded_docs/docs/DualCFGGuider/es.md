El nodo DualCFGGuider crea un sistema de guía para muestreo de guía libre de clasificador dual. Combina dos entradas de condicionamiento positivo con una entrada de condicionamiento negativo, aplicando diferentes escalas de guía a cada par de condicionamiento para controlar la influencia de cada indicación en la salida generada.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo a utilizar para la guía | MODEL | Sí | - |
| `cond1` | La primera entrada de condicionamiento positivo | CONDITIONING | Sí | - |
| `cond2` | La segunda entrada de condicionamiento positivo | CONDITIONING | Sí | - |
| `negativo` | La entrada de condicionamiento negativo | CONDITIONING | Sí | - |
| `cfg_conds` | Escala de guía para el primer condicionamiento positivo (predeterminado: 8.0) | FLOAT | Sí | 0.0 - 100.0 |
| `cfg_cond2_negativo` | Escala de guía para el segundo condicionamiento positivo y el negativo (predeterminado: 8.0) | FLOAT | Sí | 0.0 - 100.0 |
| `estilo` | El estilo de guía a aplicar (predeterminado: "regular"). Cuando se establece en "nested", la guía se aplica de forma anidada | COMBO | Sí | "regular"<br>"nested" |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `GUIDER` | Un sistema de guía configurado listo para usar con muestreo | GUIDER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/es.md)

---
**Source fingerprint (SHA-256):** `802e07f2e64dc2d55e86290db7e94dffd46079a9180480a560035d0bb6350325`
