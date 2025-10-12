> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/es.md)

El nodo DualCFGGuider crea un sistema de guía para muestreo con guía libre de clasificadores dual. Combina dos entradas de condicionamiento positivo con una entrada de condicionamiento negativo, aplicando diferentes escalas de guía a cada par de condicionamiento para controlar la influencia de cada prompt en la salida generada.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo a utilizar para la guía |
| `cond1` | CONDITIONING | Sí | - | La primera entrada de condicionamiento positivo |
| `cond2` | CONDITIONING | Sí | - | La segunda entrada de condicionamiento positivo |
| `negativo` | CONDITIONING | Sí | - | La entrada de condicionamiento negativo |
| `cfg_conds` | FLOAT | Sí | 0.0 - 100.0 | Escala de guía para el primer condicionamiento positivo (por defecto: 8.0) |
| `cfg_cond2_negativo` | FLOAT | Sí | 0.0 - 100.0 | Escala de guía para el segundo condicionamiento positivo y el negativo (por defecto: 8.0) |
| `style` | COMBO | Sí | "regular"<br>"nested" | El estilo de guía a aplicar (por defecto: "regular") |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `GUIDER` | GUIDER | Un sistema de guía configurado listo para usar con muestreo |
