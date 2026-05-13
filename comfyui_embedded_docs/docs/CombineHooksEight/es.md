> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksEight/es.md)

El nodo Combinar Hooks [8] fusiona hasta ocho grupos de hooks diferentes en un único grupo combinado. Toma múltiples entradas de hooks y las combina utilizando la funcionalidad de combinación de hooks de ComfyUI. Esto permite consolidar múltiples configuraciones de hooks para un procesamiento optimizado en flujos de trabajo avanzados.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Valor por Defecto | Rango | Descripción |
|-----------|--------------|-----------------|-------------------|-------|-------------|
| `hooks_A` | HOOKS | opcional | None | - | Primer grupo de hooks a combinar |
| `hooks_B` | HOOKS | opcional | None | - | Segundo grupo de hooks a combinar |
| `hooks_C` | HOOKS | opcional | None | - | Tercer grupo de hooks a combinar |
| `hooks_D` | HOOKS | opcional | None | - | Cuarto grupo de hooks a combinar |
| `hooks_E` | HOOKS | opcional | None | - | Quinto grupo de hooks a combinar |
| `hooks_F` | HOOKS | opcional | None | - | Sexto grupo de hooks a combinar |
| `hooks_G` | HOOKS | opcional | None | - | Séptimo grupo de hooks a combinar |
| `hooks_H` | HOOKS | opcional | None | - | Octavo grupo de hooks a combinar |

**Nota:** Todos los parámetros de entrada son opcionales. El nodo combinará únicamente los grupos de hooks que se proporcionen, ignorando aquellos que se dejen vacíos. Puedes proporcionar desde uno hasta ocho grupos de hooks para su combinación.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `HOOKS` | HOOKS | Un único grupo de hooks combinado que contiene todas las configuraciones de hooks proporcionadas |

---
**Source fingerprint (SHA-256):** `8cd13ec6710a9b2905c14301cfd15be616c00f1b4140451cdf0915f091c77197`
