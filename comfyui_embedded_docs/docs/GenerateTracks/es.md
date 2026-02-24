> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/es.md)

El nodo `GenerateTracks` crea múltiples trayectorias de movimiento paralelas para la generación de video. Define una ruta principal desde un punto de inicio hasta un punto final, luego genera un conjunto de pistas que corren paralelas a esta ruta, espaciadas uniformemente. Puedes controlar la forma de la ruta (línea recta o curva de Bézier), la velocidad del movimiento a lo largo de ella y en qué fotogramas son visibles las pistas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Sí | 16 - 4096 | El ancho del fotograma de video en píxeles. El valor por defecto es 832. |
| `height` | INT | Sí | 16 - 4096 | La altura del fotograma de video en píxeles. El valor por defecto es 480. |
| `start_x` | FLOAT | Sí | 0.0 - 1.0 | Coordenada X normalizada (0-1) para la posición de inicio. El valor por defecto es 0.0. |
| `start_y` | FLOAT | Sí | 0.0 - 1.0 | Coordenada Y normalizada (0-1) para la posición de inicio. El valor por defecto es 0.0. |
| `end_x` | FLOAT | Sí | 0.0 - 1.0 | Coordenada X normalizada (0-1) para la posición final. El valor por defecto es 1.0. |
| `end_y` | FLOAT | Sí | 0.0 - 1.0 | Coordenada Y normalizada (0-1) para la posición final. El valor por defecto es 1.0. |
| `num_frames` | INT | Sí | 1 - 1024 | El número total de fotogramas para los cuales generar posiciones de pista. El valor por defecto es 81. |
| `num_tracks` | INT | Sí | 1 - 100 | El número de pistas paralelas a generar. El valor por defecto es 5. |
| `track_spread` | FLOAT | Sí | 0.0 - 1.0 | Distancia normalizada entre pistas. Las pistas se distribuyen perpendicularmente a la dirección del movimiento. El valor por defecto es 0.025. |
| `bezier` | BOOLEAN | Sí | True / False | Habilita la ruta de curva de Bézier usando el punto medio como punto de control. El valor por defecto es False. |
| `mid_x` | FLOAT | Sí | 0.0 - 1.0 | Punto de control X normalizado para la curva de Bézier. Solo se usa cuando 'bezier' está habilitado. El valor por defecto es 0.5. |
| `mid_y` | FLOAT | Sí | 0.0 - 1.0 | Punto de control Y normalizado para la curva de Bézier. Solo se usa cuando 'bezier' está habilitado. El valor por defecto es 0.5. |
| `interpolation` | COMBO | Sí | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` | Controla la temporización/velocidad del movimiento a lo largo de la ruta. El valor por defecto es "linear". |
| `track_mask` | MASK | No | - | Máscara opcional para indicar los fotogramas visibles. |

**Nota:** Los parámetros `mid_x` y `mid_y` solo se utilizan cuando el parámetro `bezier` está establecido en `True`. Cuando `bezier` es `False`, la ruta es una línea recta desde el punto de inicio hasta el punto final.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `TRACKS` | TRACKS | Un objeto de pistas que contiene las coordenadas de ruta generadas y la información de visibilidad para todas las pistas en todos los fotogramas. |
| `track_length` | INT | El número de fotogramas para los cuales se generaron pistas, coincidiendo con la entrada `num_frames`. |
