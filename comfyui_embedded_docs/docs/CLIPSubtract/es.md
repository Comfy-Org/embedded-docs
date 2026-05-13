> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSubtract/es.md)

El nodo CLIPSubtract realiza una operación de resta entre dos modelos CLIP. Toma el primer modelo CLIP como base y resta los parches clave del segundo modelo CLIP, con un multiplicador opcional para controlar la intensidad de la resta. Esto permite una combinación de modelos ajustada mediante la eliminación de características específicas de un modelo utilizando otro.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Valor por Defecto | Rango | Descripción |
|-----------|--------------|-----------------|-------------------|-------|-------------|
| `clip1` | CLIP | Requerido | - | - | El modelo CLIP base que será modificado |
| `clip2` | CLIP | Requerido | - | - | El modelo CLIP cuyos parches clave se restarán del modelo base |
| `multiplier` | FLOAT | Requerido | 1.0 | -10.0 a 10.0, paso 0.01 | Controla la intensidad de la operación de resta. Los valores positivos restan características de clip2, mientras que los valores negativos agregan características en su lugar. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `CLIP` | CLIP | El modelo CLIP resultante después de la operación de resta |

---
**Source fingerprint (SHA-256):** `ea7b6f838d6eb083d2d9bc07891b6ef2f3e625861ab1de9279df351e58f2a2a8`
