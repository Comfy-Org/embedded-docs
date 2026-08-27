# WeldVertices

Weld Vertices fusiona vértices coincidentes en una malla 3D, de modo que las caras que anteriormente tenían puntos de esquina separados terminan compartiendo los mismos vértices. Agrupa vértices cercanos mediante cuantificación de cuadrícula con una tolerancia basada en la caja delimitadora de la malla, y promedia los colores de vértice para cada grupo fusionado. Esto es útil cuando una malla llega sin soldar, es decir, cada cara tiene sus propios vértices y no hay aristas compartidas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `mesh` | La malla 3D de entrada cuyos vértices coincidentes se fusionarán. | MESH | Sí | - |
| `epsilon_rel` | Tolerancia de soldadura (fracción de la diagonal de la caja delimitadora). 1e-5 para deduplicación de flotantes; 1e-3 para vértices visiblemente cercanos pero distintos. Valor predeterminado: 1e-5. | FLOAT | Sí | 0.0 a ilimitado |
| `epsilon_abs` | Tolerancia de soldadura absoluta (anula epsilon_rel cuando > 0). Valor predeterminado: 0.0. | FLOAT | Sí | 0.0 a ilimitado |

Nota: Cuando `epsilon_abs` es mayor que 0, tiene prioridad sobre `epsilon_rel` y la tolerancia relativa se ignora. Cuando `epsilon_abs` es 0, se usa la tolerancia relativa `epsilon_rel`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `mesh` | La malla soldada con vértices fusionados, índices de cara actualizados y colores de vértice promediados (si la malla de entrada tenía colores). | MESH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WeldVertices/es.md)

---
**Source fingerprint (SHA-256):** `f8779e764b344de651b8459f6e4c28773509d9596a98fd164dc7044278856435`
