# CLIPSubtract

El nodo CLIPSubtract realiza una operación de resta entre dos modelos CLIP. Toma el primer modelo CLIP como base y resta los parches clave del segundo modelo CLIP, con un multiplicador opcional para controlar la intensidad de la resta. Esto permite una combinación de modelos ajustada mediante la eliminación de características específicas de un modelo utilizando otro.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Tipo de Entrada | Valor por Defecto | Rango |
| --- | --- | --- | --- | --- | --- |
| `clip1` | El modelo CLIP base que será modificado | CLIP | Requerido | - | - |
| `clip2` | El modelo CLIP cuyos parches clave se restarán del modelo base | CLIP | Requerido | - | - |
| `multiplier` | Controla la intensidad de la operación de resta. Los valores positivos restan características de clip2, mientras que los valores negativos agregan características en su lugar. | FLOAT | Requerido | 1.0 | -10.0 a 10.0, paso 0.01 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `CLIP` | El modelo CLIP resultante después de la operación de resta | CLIP |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSubtract/es.md)

---
**Source fingerprint (SHA-256):** `ea7b6f838d6eb083d2d9bc07891b6ef2f3e625861ab1de9279df351e58f2a2a8`
