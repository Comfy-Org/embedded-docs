# WanMoveTracksFromCoords

El nodo WanMoveTracksFromCoords crea trayectorias de movimiento a partir de una cadena de coordenadas en formato JSON. Convierte los datos de coordenadas en un formato de tensor que puede ser utilizado por otros nodos de procesamiento de video y, opcionalmente, puede aplicar una máscara para controlar la visibilidad de las trayectorias a lo largo del tiempo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `track_coords` | Cadena con formato JSON que contiene los datos de coordenadas de las trayectorias. El valor predeterminado es una lista vacía (`"[]"`). | STRING | No | N/A |
| `track_mask` | Máscara opcional. Cuando se proporciona, el nodo la utiliza para determinar la visibilidad de cada trayectoria por fotograma. Cuando no se proporciona, todas las trayectorias se consideran visibles en todos los fotogramas. | MASK | No | N/A |

**Nota:** La entrada `track_coords` espera una estructura JSON específica. Debe ser una lista de trayectorias, donde cada trayectoria es una lista de fotogramas, y cada fotograma es un objeto con coordenadas `x` e `y`. El número de fotogramas debe ser consistente en todas las trayectorias.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `tracks` | Los datos de trayectoria generados, que contienen las coordenadas de la ruta y la información de visibilidad de cada trayectoria. | TRACKS |
| `track_length` | El número total de fotogramas en las trayectorias generadas. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/es.md)

---
**Source fingerprint (SHA-256):** `125187c96332fa81f0a30bcc4c927f405b56b578638ea565642a2b88dff808b7`
