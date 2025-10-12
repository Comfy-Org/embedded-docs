> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/es.md)

El nodo LatentApplyOperation aplica una operación específica a muestras latentes. Toma datos latentes y una operación como entradas, procesa las muestras latentes utilizando la operación proporcionada y devuelve los datos latentes modificados. Este nodo le permite transformar o manipular representaciones latentes en su flujo de trabajo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `muestras` | LATENT | Sí | - | Las muestras latentes que serán procesadas por la operación |
| `operación` | LATENT_OPERATION | Sí | - | La operación a aplicar a las muestras latentes |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | LATENT | Las muestras latentes modificadas después de aplicar la operación |
