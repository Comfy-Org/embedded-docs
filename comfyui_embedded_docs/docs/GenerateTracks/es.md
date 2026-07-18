El nodo `GenerateTracks` crea múltiples rutas de movimiento paralelas para la generación de videos. Define una trayectoria principal desde un punto de inicio hasta un punto final, luego genera un conjunto de pistas que corren paralelas a esta trayectoria, espaciadas uniformemente. Puedes controlar la forma de la trayectoria (línea recta o curva Bezier), la velocidad de movimiento a lo largo de ella y en qué fotogramas las pistas son visibles.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `ancho` | El ancho del fotograma de video en píxeles. El valor predeterminado es 832. | INT | Sí | 16 - 4096 |
| `alto` | La altura del fotograma de video en píxeles. El valor predeterminado es 480. | INT | Sí | 16 - 4096 |
| `inicio_x` | Coordenada X normalizada (0-1) para la posición de inicio. El valor predeterminado es 0.0. | FLOAT | Sí | 0.0 - 1.0 |
| `inicio_y` | Coordenada Y normalizada (0-1) para la posición de inicio. El valor predeterminado es 0.0. | FLOAT | Sí | 0.0 - 1.0 |
| `fin_x` | Coordenada X normalizada (0-1) para la posición final. El valor predeterminado es 1.0. | FLOAT | Sí | 0.0 - 1.0 |
| `fin_y` | Coordenada Y normalizada (0-1) para la posición final. El valor predeterminado es 1.0. | FLOAT | Sí | 0.0 - 1.0 |
| `número_de_frames` | El número total de fotogramas para los cuales generar posiciones de pista. El valor predeterminado es 81. | INT | Sí | 1 - 1024 |
| `número_de_rutas` | El número de pistas paralelas a generar. El valor predeterminado es 5. | INT | Sí | 1 - 100 |
| `separación_de_rutas` | Distancia normalizada entre pistas. Las pistas se distribuyen perpendicularmente a la dirección del movimiento. El valor predeterminado es 0.025. | FLOAT | Sí | 0.0 - 1.0 |
| `bezier` | Habilita la trayectoria de curva Bezier usando el punto medio como punto de control. El valor predeterminado es Falso. | BOOLEAN | Sí | Verdadero / Falso |
| `medio_x` | Punto de control X normalizado para la curva Bezier. Solo se usa cuando 'bezier' está habilitado. El valor predeterminado es 0.5. | FLOAT | Sí | 0.0 - 1.0 |
| `medio_y` | Punto de control Y normalizado para la curva Bezier. Solo se usa cuando 'bezier' está habilitado. El valor predeterminado es 0.5. | FLOAT | Sí | 0.0 - 1.0 |
| `interpolación` | Controla la temporización/velocidad del movimiento a lo largo de la trayectoria. El valor predeterminado es "linear". | COMBO | Sí | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` |
| `máscara_de_ruta` | Máscara opcional para indicar fotogramas visibles. | MASK | No | - |

**Nota:** Los parámetros `mid_x` y `mid_y` solo se utilizan cuando el parámetro `bezier` está configurado en `True`. Cuando `bezier` es `False`, la trayectoria es una línea recta desde el punto de inicio hasta el punto final.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `longitud_de_ruta` | Un objeto de pistas que contiene las coordenadas de trayectoria generadas e información de visibilidad para todas las pistas en todos los fotogramas. | TRACKS |
| `longitud_de_ruta` | El número de fotogramas para los cuales se generaron pistas, coincidiendo con el `número_de_frames` de entrada. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/es.md)

---
**Source fingerprint (SHA-256):** `3dca1cabaee8738e2a68acafed47ad347019d03c9b7f0d1392b3fdf97d0e8add`
