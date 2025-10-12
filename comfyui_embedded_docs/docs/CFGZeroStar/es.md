> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGZeroStar/es.md)

El nodo CFGZeroStar aplica una técnica especializada de escalado de guía a modelos de difusión. Modifica el proceso de guía libre de clasificador calculando un factor de escala optimizado basado en la diferencia entre las predicciones condicionales e incondicionales. Este enfoque ajusta la salida final para proporcionar un control mejorado sobre el proceso de generación mientras mantiene la estabilidad del modelo.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `modelo` | MODEL | requerido | - | - | El modelo de difusión que será modificado con la técnica de escalado de guía CFGZeroStar |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `patched_model` | MODEL | El modelo modificado con el escalado de guía CFGZeroStar aplicado |
