> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksFour/es.md)

El nodo Combinar Hooks [4] fusiona hasta cuatro grupos de hooks separados en un único grupo de hooks combinado. Toma cualquier combinación de las cuatro entradas de hooks disponibles y las combina utilizando el sistema de combinación de hooks de ComfyUI. Esto permite consolidar múltiples configuraciones de hooks para un procesamiento optimizado en flujos de trabajo avanzados.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `hooks_A` | HOOKS | opcional | None | - | Primer grupo de hooks a combinar |
| `hooks_B` | HOOKS | opcional | None | - | Segundo grupo de hooks a combinar |
| `hooks_C` | HOOKS | opcional | None | - | Tercer grupo de hooks a combinar |
| `hooks_D` | HOOKS | opcional | None | - | Cuarto grupo de hooks a combinar |

**Nota:** Las cuatro entradas de hooks son opcionales. El nodo combinará solo los grupos de hooks que se proporcionen, y devolverá un grupo de hooks vacío si no se conecta ninguna entrada.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `HOOKS` | HOOKS | Grupo de hooks combinado que contiene todas las configuraciones de hooks proporcionadas |
