# WanMoveTracksFromCoords

El nodo WanMoveTracksFromCoords crea pistas de movimiento a partir de una cadena con formato JSON de coordenadas. Convierte los datos de coordenadas en un formato de tensor que puede ser utilizado por otros nodos de procesamiento de video y, opcionalmente, puede aplicar una máscara para controlar la visibilidad de las pistas a lo largo del tiempo.

## Entradas

| Parámetro | Descripción | Tipo de datos | ¿Requerido? | Rango |
| --- | --- | --- | --- | --- |
| `coordenadas_de_pista` | Una cadena con formato JSON que contiene los datos de coordenadas de las pistas. El valor predeterminado es una lista vacía (`"[]"`). Esta entrada es una entrada forzada, por lo que debe estar conectada en la interfaz. | STRING | No | N/D |
| `máscara_de_pista` | Una máscara opcional. Cuando se proporciona, el nodo la utiliza para determinar la visibilidad de las pistas por fotograma: las pistas son visibles en los fotogramas donde la máscara contiene cualquier píxel distinto de cero. Cuando no se proporciona, todas las pistas son visibles en todos los fotogramas. | MASK | No | N/D |

**Nota:** La entrada `track_coords` espera una estructura JSON específica. Debe ser una lista de pistas, donde cada pista es una lista de fotogramas, y cada fotograma es un objeto con coordenadas `x` y `y`. El número de fotogramas debe ser coherente en todas las pistas y se debe proporcionar al menos una pista.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `tracks` | Los datos de pista generados, que contienen las coordenadas de la trayectoria y la información de visibilidad de cada pista. | TRACKS |
| `longitud_de_pista` | El número total de fotogramas en las pistas generadas. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/es.md)

---
**Source fingerprint (SHA-256):** `125187c96332fa81f0a30bcc4c927f405b56b578638ea565642a2b88dff808b7`
