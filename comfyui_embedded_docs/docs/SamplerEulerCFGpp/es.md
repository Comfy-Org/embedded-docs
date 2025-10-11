> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerCFGpp/es.md)

El nodo SamplerEulerCFGpp proporciona un método de muestreo Euler CFG++ para generar salidas. Este nodo ofrece dos versiones de implementación diferentes del muestreador Euler CFG++ que pueden seleccionarse según la preferencia del usuario.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `version` | STRING | Sí | `"regular"`<br>`"alternative"` | La versión de implementación del muestreador Euler CFG++ a utilizar |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Devuelve una instancia configurada del muestreador Euler CFG++ |