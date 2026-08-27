# Guía Dual CFG

El nodo DualCFGGuider crea un sistema de guía para el muestreo de guía dual sin clasificador. Combina dos entradas de condicionamiento con una entrada de condicionamiento negativa y aplica dos escalas de guía separadas para controlar cuán fuertemente influye cada condicionamiento en la salida generada. Admite dos estilos de combinar estas escalas de guía: "regular" y "nested".

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo a utilizar para la guía | MODEL | Sí | - |
| `cond1` | La primera entrada de condicionamiento positiva | CONDITIONING | Sí | - |
| `cond2` | La segunda entrada de condicionamiento, utilizada como referencia entre el primer condicionamiento positivo y el condicionamiento negativo | CONDITIONING | Sí | - |
| `negativo` | La entrada de condicionamiento negativa | CONDITIONING | Sí | - |
| `cfg_conds` | Escala de guía aplicada al primer condicionamiento positivo (valor predeterminado: 8.0) | FLOAT | Sí | 0.0 - 100.0 |
| `cfg_cond2_negativo` | Escala de guía aplicada entre el segundo condicionamiento y el condicionamiento negativo (valor predeterminado: 8.0) | FLOAT | Sí | 0.0 - 100.0 |
| `estilo` | El estilo de guía a aplicar (valor predeterminado: "regular"). Cuando se establece en "nested", la guía se aplica de forma anidada | COMBO | Sí | "regular"<br>"nested" |

Nota: En el estilo `regular`, `cfg_cond2_negative` se aplica entre `cond2` y `negative`, y `cfg_conds` se aplica entre `cond1` y `cond2`. En el estilo `nested`, `cfg_conds` se aplica primero entre `cond1` y `cond2`, y la predicción resultante se guía para alejarse de `negative` utilizando `cfg_cond2_negative`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `GUIDER` | Un sistema de guía configurado listo para usar con muestreo | GUIDER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/es.md)

---
**Source fingerprint (SHA-256):** `ef28d109149cb545bcd76215fd99535905c1d395222149a029c1c210e2912e97`
