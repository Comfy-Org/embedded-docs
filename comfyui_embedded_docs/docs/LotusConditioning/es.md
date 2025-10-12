> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/es.md)

El nodo LotusConditioning proporciona incrustaciones de condicionamiento precalculadas para el modelo Lotus. Utiliza un codificador congelado con condicionamiento nulo y devuelve incrustaciones de prompt predefinidas para lograr paridad con la implementación de referencia sin requerir inferencia o carga de archivos de tensor grandes. Este nodo genera un tensor de condicionamiento fijo que puede utilizarse directamente en el pipeline de generación.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| *Sin entradas* | - | - | - | Este nodo no acepta ningún parámetro de entrada. |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | Las incrustaciones de condicionamiento precalculadas para el modelo Lotus, que contienen incrustaciones de prompt fijas y un diccionario vacío. |
