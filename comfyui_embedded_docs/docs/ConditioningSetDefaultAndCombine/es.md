> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetDefaultAndCombine/es.md)

Este nodo combina datos de acondicionamiento con datos de acondicionamiento predeterminados utilizando un sistema basado en hooks. Toma una entrada de acondicionamiento principal y una entrada de acondicionamiento predeterminado, luego las fusiona de acuerdo con la configuración de hook especificada. El resultado es una única salida de acondicionamiento que incorpora ambas fuentes.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `cond` | CONDITIONING | Requerido | - | - | La entrada de acondicionamiento principal a procesar |
| `cond_DEFAULT` | CONDITIONING | Requerido | - | - | Los datos de acondicionamiento predeterminado que se combinarán con el acondicionamiento principal |
| `hooks` | HOOKS | Opcional | - | - | Configuración opcional de hooks que controla cómo se procesan y combinan los datos de acondicionamiento |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Los datos de acondicionamiento combinados resultantes de fusionar las entradas de acondicionamiento principal y predeterminado |
