# GenerateTracks

El nodo `GenerateTracks` crea múltiples rutas de movimiento paralelas para la generación de video. Define una ruta principal desde un punto inicial hasta un punto final, y luego genera un conjunto de pistas que corren paralelas a esta ruta, espaciadas uniformemente. Puedes controlar la forma de la ruta (línea recta o curva de Bézier), la velocidad de movimiento a lo largo de ella y en qué fotogramas las pistas son visibles.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `width` | El ancho del fotograma de video en píxeles. El valor predeterminado es 832. | INT | Sí | 16 - 4096 |
| `height` | La altura del fotograma de video en píxeles. El valor predeterminado es 480. | INT | Sí | 16 - 4096 |
| `start_x` | Coordenada X normalizada (0-1) para la posición inicial. El valor predeterminado es 0.0. | FLOAT | Sí | 0.0 - 1.0 |
| `start_y` | Coordenada Y normalizada (0-1) para la posición inicial. El valor predeterminado es 0.0. | FLOAT | Sí | 0.0 - 1.0 |
| `end_x` | Coordenada X normalizada (0-1) para la posición final. El valor predeterminado es 1.0. | FLOAT | Sí | 0.0 - 1.0 |
| `end_y` | Coordenada Y normalizada (0-1) para la posición final. El valor predeterminado es 1.0. | FLOAT | Sí | 0.0 - 1.0 |
| `num_frames` | El número total de fotogramas para los cuales generar posiciones de pista. El valor predeterminado es 81. | INT | Sí | 1 - 1024 |
| `num_tracks` | El número de pistas paralelas a generar. El valor predeterminado es 5. | INT | Sí | 1 - 100 |
| `track_spread` | Distancia normalizada entre pistas. Las pistas se extienden perpendicularmente a la dirección del movimiento. El valor predeterminado es 0.025. | FLOAT | Sí | 0.0 - 1.0 |
| `bezier` | Habilita la ruta de curva de Bézier usando el punto medio como punto de control. El valor predeterminado es False. | BOOLEAN | Sí | True / False |
| `mid_x` | Punto de control X normalizado para la curva de Bézier. Solo se usa cuando `bezier` está habilitado. El valor predeterminado es 0.5. | FLOAT | Sí | 0.0 - 1.0 |
| `mid_y` | Punto de control Y normalizado para la curva de Bézier. Solo se usa cuando `bezier` está habilitado. El valor predeterminado es 0.5. | FLOAT | Sí | 0.0 - 1.0 |
| `interpolation` | Controla la sincronización/velocidad del movimiento a lo largo de la ruta. El valor predeterminado es "linear". Con "constant", todos los puntos permanecen en la posición inicial. | COMBO | Sí | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` |
| `track_mask` | Máscara opcional para indicar fotogramas visibles. | MASK | No | - |

**Nota:** Los parámetros `mid_x` y `mid_y` solo se utilizan cuando el parámetro `bezier` está establecido en `True`. Cuando `bezier` es `False`, la ruta es una línea recta desde el punto inicial hasta el punto final.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `TRACKS` | Un objeto de pistas que contiene las coordenadas de la ruta generada y la información de visibilidad para todas las pistas en todos los fotogramas. | TRACKS |
| `track_length` | El número de fotogramas para los cuales se generaron pistas, coincidiendo con la entrada `num_frames`. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/es.md)

---
**Source fingerprint (SHA-256):** `4bd4d03a84f4b7ea260555b43f217af0b90dd4ca5196aca94e8f3886875ab912`
