> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_TrackToMask/es.md)

# Resumen

Selecciona objetos rastreados específicos de una sesión de seguimiento SAM3 mediante sus números de índice y los combina en una única máscara de salida. Esto permite elegir qué objetos conservar y cuáles ignorar de los resultados del seguimiento.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `track_data` | SAM3TRACKDATA | Sí | N/A | Los datos de seguimiento provenientes de un nodo rastreador SAM3, que contienen las máscaras empaquetadas y el tamaño de imagen original. |
| `object_indices` | STRING | No | Cualquier lista de enteros separados por comas | Índices de objetos separados por comas para incluir en la máscara de salida (ej. '0,2,3'). Si se deja vacío, se incluyen todos los objetos rastreados. |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|-------------|-----------|-------------|
| `masks` | MASK | Una única máscara binaria para cada fotograma, donde los objetos seleccionados se combinan en una sola máscara. Si no se selecciona ningún objeto o no existen datos de seguimiento, devuelve una máscara de ceros. |