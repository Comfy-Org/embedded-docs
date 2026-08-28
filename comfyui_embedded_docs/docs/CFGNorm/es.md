# CFGNorm

CFGNorm aplica una técnica de normalización al proceso de guía sin clasificador (CFG) en los modelos de difusión. Ajusta la escala de la predicción de eliminación de ruido comparando las normas de las salidas condicionales e incondicionales, y luego aplica un multiplicador de intensidad para controlar el efecto. De forma predeterminada, la normalización solo atenúa la salida de guía, pero habilitar `pre_cfg` reescala el ruido combinado antes de la combinación CFG del muestreador, sin limitarlo, lo que puede amplificarlo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de difusión al que se le aplica la normalización de CFG | MODEL | Sí | - |
| `intensidad` | Controla la intensidad del efecto de normalización aplicado a la escala de CFG (por defecto: 1.0) | FLOAT | Sí | 0.0 a 100.0 |
| `pre_cfg` | Si es true, reescala el ruido combinado ANTES de la combinación CFG del muestreador, sin limitarlo (puede amplificarlo). Coincide con la CFG de escala por norma utilizada por modelos como Lens. El valor false predeterminado mantiene el comportamiento original posterior a CFG de solo atenuación en el espacio x0. (por defecto: false) | BOOLEAN | No | true / false |

Nota: Este nodo está marcado como experimental.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `modelo_parcheado` | Devuelve el modelo modificado con la normalización de CFG aplicada a su proceso de muestreo | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/es.md)

---
**Source fingerprint (SHA-256):** `427dda498ebda2642489aa2591f063355a77b1e064e0dc7fa8570ed8200c2734`
