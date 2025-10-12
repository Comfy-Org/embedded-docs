> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooks/es.md)

El nodo Combine Hooks [2] combina dos grupos de hooks en un único grupo de hooks combinado. Toma dos entradas de hooks opcionales y las combina utilizando la funcionalidad de combinación de hooks de ComfyUI. Esto permite consolidar múltiples configuraciones de hooks para un procesamiento optimizado.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `hooks_A` | HOOKS | Opcional | None | - | Primer grupo de hooks a combinar |
| `hooks_B` | HOOKS | Opcional | None | - | Segundo grupo de hooks a combinar |

**Nota:** Ambas entradas son opcionales, pero se debe proporcionar al menos un grupo de hooks para que el nodo funcione. Si solo se proporciona un grupo de hooks, este será devuelto sin cambios.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `hooks` | HOOKS | Grupo de hooks combinado que contiene todos los hooks de ambos grupos de entrada |
