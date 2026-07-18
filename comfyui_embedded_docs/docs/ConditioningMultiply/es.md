# Condicionamiento (Multiplicar)

Este nodo multiplica los vectores de condicionamiento por un factor escalar, permitiéndote escalar la influencia de una entrada de condicionamiento. Aplica el multiplicador tanto al tensor de condicionamiento principal como a la salida agrupada, si está presente.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `conditioning` | Los datos de condicionamiento que se escalarán | CONDITIONING | Sí | - |
| `multiplier` | El factor de escala que se aplicará al condicionamiento (predeterminado: 1.0) | FLOAT | Sí | -100.0 a 100.0 (paso: 0.01) |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|-------------|-------------|-----------|
| `CONDITIONING` | Los datos de condicionamiento escalados con el multiplicador aplicado tanto al tensor principal como a la salida agrupada | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningMultiply/es.md)

---
**Source fingerprint (SHA-256):** `8d241e3d5d91e513c24ade5b4bece4bf879fe093a4be6d53dab11a5a0bf55616`
