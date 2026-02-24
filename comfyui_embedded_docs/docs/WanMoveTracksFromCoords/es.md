> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/es.md)

El nodo WanMoveTracksFromCoords crea un conjunto de pistas de movimiento a partir de una lista de puntos de coordenadas. Convierte una cadena con formato JSON de coordenadas en un formato de tensor que puede ser utilizado por otros nodos de procesamiento de video, y puede aplicar opcionalmente una máscara para controlar la visibilidad de las pistas a lo largo del tiempo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `track_coords` | STRING | Sí | N/A | Una cadena con formato JSON que contiene los datos de coordenadas para las pistas. El valor por defecto es una lista vacía (`"[]"`). |
| `track_mask` | MASK | No | N/A | Una máscara opcional. Cuando se proporciona, el nodo la utiliza para determinar la visibilidad de cada pista por fotograma. |

**Nota:** La entrada `track_coords` espera una estructura JSON específica. Debe ser una lista de pistas, donde cada pista es una lista de fotogramas, y cada fotograma es un objeto con coordenadas `x` e `y`. El número de fotogramas debe ser consistente en todas las pistas.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `tracks` | TRACKS | Los datos de pista generados, que contienen las coordenadas de la ruta y la información de visibilidad para cada pista. |
| `track_length` | INT | El número total de fotogramas en las pistas generadas. |
