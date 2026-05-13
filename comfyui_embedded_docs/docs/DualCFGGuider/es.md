> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/es.md)

El nodo DualCFGGuider crea un sistema de guía para muestreo de guía libre de clasificador dual. Combina dos entradas de condicionamiento positivo con una entrada de condicionamiento negativo, aplicando diferentes escalas de guía a cada par de condicionamiento para controlar la influencia de cada indicación en la salida generada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo a utilizar para la guía |
| `cond1` | CONDITIONING | Sí | - | La primera entrada de condicionamiento positivo |
| `cond2` | CONDITIONING | Sí | - | La segunda entrada de condicionamiento positivo |
| `negativo` | CONDITIONING | Sí | - | La entrada de condicionamiento negativo |
| `cfg_conds` | FLOAT | Sí | 0.0 - 100.0 | Escala de guía para el primer condicionamiento positivo (predeterminado: 8.0) |
| `cfg_cond2_negativo` | FLOAT | Sí | 0.0 - 100.0 | Escala de guía para el segundo condicionamiento positivo y el negativo (predeterminado: 8.0) |
| `estilo` | COMBO | Sí | "regular"<br>"nested" | El estilo de guía a aplicar (predeterminado: "regular"). Cuando se establece en "nested", la guía se aplica de forma anidada |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `GUIDER` | GUIDER | Un sistema de guía configurado listo para usar con muestreo |

---
**Source fingerprint (SHA-256):** `802e07f2e64dc2d55e86290db7e94dffd46079a9180480a560035d0bb6350325`
