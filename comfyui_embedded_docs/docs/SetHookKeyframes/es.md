> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetHookKeyframes/es.md)

El nodo Set Hook Keyframes permite aplicar programación de fotogramas clave a grupos de hooks existentes. Toma un grupo de hooks y opcionalmente aplica información de temporización de fotogramas clave para controlar cuándo se ejecutan los diferentes hooks durante el proceso de generación. Cuando se proporcionan fotogramas clave, el nodo clona el grupo de hooks y establece la temporización de fotogramas clave en todos los hooks dentro del grupo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `hooks` | HOOKS | Sí | - | El grupo de hooks al que se aplicará la programación de fotogramas clave |
| `hook_kf` | HOOK_KEYFRAMES | No | - | Grupo opcional de fotogramas clave que contiene información de temporización para la ejecución de hooks |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `hooks` | HOOKS | El grupo de hooks modificado con programación de fotogramas clave aplicada (clonado si se proporcionaron fotogramas clave) |