> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/es.md)

El nodo `GenerateTracks` crea múltiples rutas de movimiento paralelas para la generación de videos. Define una trayectoria principal desde un punto de inicio hasta un punto final, luego genera un conjunto de pistas que corren paralelas a esta trayectoria, espaciadas uniformemente. Puedes controlar la forma de la trayectoria (línea recta o curva Bezier), la velocidad de movimiento a lo largo de ella y en qué fotogramas las pistas son visibles.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `ancho` | INT | Sí | 16 - 4096 | El ancho del fotograma de video en píxeles. El valor predeterminado es 832. |
| `alto` | INT | Sí | 16 - 4096 | La altura del fotograma de video en píxeles. El valor predeterminado es 480. |
| `inicio_x` | FLOAT | Sí | 0.0 - 1.0 | Coordenada X normalizada (0-1) para la posición de inicio. El valor predeterminado es 0.0. |
| `inicio_y` | FLOAT | Sí | 0.0 - 1.0 | Coordenada Y normalizada (0-1) para la posición de inicio. El valor predeterminado es 0.0. |
| `fin_x` | FLOAT | Sí | 0.0 - 1.0 | Coordenada X normalizada (0-1) para la posición final. El valor predeterminado es 1.0. |
| `fin_y` | FLOAT | Sí | 0.0 - 1.0 | Coordenada Y normalizada (0-1) para la posición final. El valor predeterminado es 1.0. |
| `número_de_frames` | INT | Sí | 1 - 1024 | El número total de fotogramas para los cuales generar posiciones de pista. El valor predeterminado es 81. |
| `número_de_rutas` | INT | Sí | 1 - 100 | El número de pistas paralelas a generar. El valor predeterminado es 5. |
| `separación_de_rutas` | FLOAT | Sí | 0.0 - 1.0 | Distancia normalizada entre pistas. Las pistas se distribuyen perpendicularmente a la dirección del movimiento. El valor predeterminado es 0.025. |
| `bezier` | BOOLEAN | Sí | Verdadero / Falso | Habilita la trayectoria de curva Bezier usando el punto medio como punto de control. El valor predeterminado es Falso. |
| `medio_x` | FLOAT | Sí | 0.0 - 1.0 | Punto de control X normalizado para la curva Bezier. Solo se usa cuando 'bezier' está habilitado. El valor predeterminado es 0.5. |
| `medio_y` | FLOAT | Sí | 0.0 - 1.0 | Punto de control Y normalizado para la curva Bezier. Solo se usa cuando 'bezier' está habilitado. El valor predeterminado es 0.5. |
| `interpolación` | COMBO | Sí | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` | Controla la temporización/velocidad del movimiento a lo largo de la trayectoria. El valor predeterminado es "linear". |
| `máscara_de_ruta` | MASK | No | - | Máscara opcional para indicar fotogramas visibles. |

**Nota:** Los parámetros `mid_x` y `mid_y` solo se utilizan cuando el parámetro `bezier` está configurado en `True`. Cuando `bezier` es `False`, la trayectoria es una línea recta desde el punto de inicio hasta el punto final.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `longitud_de_ruta` | TRACKS | Un objeto de pistas que contiene las coordenadas de trayectoria generadas e información de visibilidad para todas las pistas en todos los fotogramas. |
| `track_length` | INT | El número de fotogramas para los cuales se generaron pistas, coincidiendo con el `número_de_frames` de entrada. |

---
**Source fingerprint (SHA-256):** `3dca1cabaee8738e2a68acafed47ad347019d03c9b7f0d1392b3fdf97d0e8add`
