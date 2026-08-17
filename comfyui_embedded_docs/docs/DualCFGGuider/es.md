# Guía Dual CFG

El nodo DualCFGGuider crea un sistema de guiado para el muestreo de guiado sin clasificador dual. Combina dos entradas de condicionamiento positivo con una entrada de condicionamiento negativo, aplicando diferentes escalas de guiado a cada par de condicionamiento para controlar cuán fuertemente influye cada prompt en la salida generada.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo a utilizar para el guiado. | MODEL | Sí | - |
| `cond1` | La primera entrada de condicionamiento positivo. | CONDITIONING | Sí | - |
| `cond2` | La segunda entrada de condicionamiento positivo, tratada como el condicionamiento intermedio. | CONDITIONING | Sí | - |
| `negative` | La entrada de condicionamiento negativo. | CONDITIONING | Sí | - |
| `cfg_conds` | Escala de guiado aplicada entre `cond1` y `cond2` (por defecto: 8.0). | FLOAT | Sí | 0.0 - 100.0 |
| `cfg_cond2_negative` | Escala de guiado aplicada entre `cond2` y el condicionamiento negativo (por defecto: 8.0). | FLOAT | Sí | 0.0 - 100.0 |
| `style` | El estilo de guiado a aplicar (por defecto: "regular"). "regular" combina ambas escalas de guiado en un solo paso; "nested" aplica primero `cfg_conds` y luego escala el resultado con `cfg_cond2_negative` en relación con el condicionamiento negativo. | COMBO | Sí | "regular"<br>"nested" |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `GUIDER` | Un sistema de guiado configurado listo para usar con el muestreo. | GUIDER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/es.md)

---
**Source fingerprint (SHA-256):** `ef28d109149cb545bcd76215fd99535905c1d395222149a029c1c210e2912e97`
