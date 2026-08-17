# CFGNorm

CFGNorm aplica una técnica de normalización al proceso de guía sin clasificador (CFG) en modelos de difusión. Ajusta la escala de la predicción sin ruido comparando las normas de las salidas condicional e incondicional, y luego aplica un multiplicador de intensidad para controlar el efecto. Esto ayuda a estabilizar el proceso de generación al prevenir valores extremos en el escalado de la guía. Cuando `pre_cfg` está habilitado, el reescalado se aplica en su lugar al ruido combinado antes de la combinación CFG del muestreador.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de difusión al que se le aplica la normalización CFG | MODEL | Sí | - |
| `strength` | Controla la intensidad del efecto de normalización aplicado al escalado de CFG (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 100.0 (paso 0.01) |
| `pre_cfg` | Si es true, reescala el ruido combinado ANTES de la combinación CFG del muestreador, sin limitación (puede amplificar). Coincide con la CFG escalada por norma utilizada por modelos como Lens. El valor false (predeterminado) conserva el comportamiento original de solo atenuación en el espacio x0 posterior a CFG. (predeterminado: False) | BOOLEAN | No | True<br>False |

Nota: En el modo posterior a CFG predeterminado, el factor de reescalado está limitado entre 0.0 y 1.0, por lo que solo puede atenuar (reducir) la escala de la predicción. Cuando `pre_cfg` está habilitado, no se aplica limitación, por lo que el ruido combinado puede amplificarse. En ese modo, un valor de `strength` distinto de 1.0 mezcla el resultado de nuevo hacia la CFG lineal estándar.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `patched_model` | Devuelve el modelo modificado con la normalización CFG aplicada a su proceso de muestreo | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/es.md)

---
**Source fingerprint (SHA-256):** `427dda498ebda2642489aa2591f063355a77b1e064e0dc7fa8570ed8200c2734`
