> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchMasksNode/es.md)

El nodo Combinar Máscaras combina múltiples entradas de máscaras individuales en un solo lote. Toma un número variable de entradas de máscaras y las genera como un único tensor de máscaras agrupadas, lo que permite el procesamiento por lotes de máscaras en nodos posteriores.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `mask_0` | MASK | Sí | - | La primera entrada de máscara. |
| `mask_1` | MASK | Sí | - | La segunda entrada de máscara. |
| `mask_2` a `mask_49` | MASK | No | - | Entradas de máscara adicionales opcionales. El nodo puede aceptar un mínimo de 2 y un máximo de 50 máscaras en total. |

**Nota:** Este nodo utiliza una plantilla de entrada de crecimiento automático. Debes conectar al menos dos máscaras (`mask_0` y `mask_1`). Puedes agregar hasta 48 entradas de máscara opcionales adicionales (`mask_2` a `mask_49`) para un total de 50 máscaras. Todas las máscaras conectadas se combinarán en un solo lote.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | MASK | Un único lote de máscaras que contiene todas las máscaras de entrada apiladas juntas. |

---
**Source fingerprint (SHA-256):** `8eb7a2a2d8108b619387b049d92348b8e9fc6d5e94e78c856c8520b88cdf77f2`
