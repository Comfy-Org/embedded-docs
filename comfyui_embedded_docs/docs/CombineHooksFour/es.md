> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksFour/es.md)

El nodo **Combinar Ganchos [4]** fusiona hasta cuatro grupos de ganchos separados en un único grupo combinado. Toma cualquier combinación de las cuatro entradas de ganchos disponibles y las combina utilizando el sistema de combinación de ganchos de ComfyUI. Esto permite consolidar múltiples configuraciones de ganchos para un procesamiento optimizado en flujos de trabajo avanzados.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Valor por Defecto | Rango | Descripción |
|-----------|--------------|-----------------|-------------------|-------|-------------|
| `hooks_A` | HOOKS | opcional | None | - | Primer grupo de ganchos a combinar |
| `hooks_B` | HOOKS | opcional | None | - | Segundo grupo de ganchos a combinar |
| `hooks_C` | HOOKS | opcional | None | - | Tercer grupo de ganchos a combinar |
| `hooks_D` | HOOKS | opcional | None | - | Cuarto grupo de ganchos a combinar |

**Nota:** Las cuatro entradas de ganchos son opcionales. El nodo combinará únicamente los grupos de ganchos que se proporcionen y devolverá un grupo de ganchos vacío si no hay entradas conectadas.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `HOOKS` | HOOKS | Grupo de ganchos combinado que contiene todas las configuraciones de ganchos proporcionadas |

---
**Source fingerprint (SHA-256):** `92a8038e7b5a7491afcbd48830a1e278fe4d697321fb874821ebf7edd09d5815`
