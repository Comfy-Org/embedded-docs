# LoopIteration

Este nodo proporciona metadatos de iteración para flujos de trabajo de tipo bucle. Recibe entradas basadas en listas y transfiere el primer elemento de cada lista, de modo que un bucle puede rastrear el índice actual, si se trata del primer o del último paso, el elemento actual de la lista y cualquier valor de iteración en curso. El comportamiento de la caché se controla mediante el indicador `reuse_cache`.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `iteration_index` | El índice de la iteración actual, proporcionado como una lista. El primer elemento se transfiere a la salida. | INT | Sí | - |
| `is_first` | Indica si la iteración actual es la primera, proporcionado como una lista. El primer elemento se transfiere a la salida. | BOOLEAN | Sí | - |
| `is_last` | Indica si la iteración actual es la última, proporcionado como una lista. El primer elemento se transfiere a la salida. | BOOLEAN | Sí | - |
| `list_item` | El elemento tomado de la lista para esta iteración. Opcional; el primer elemento se transfiere a la salida cuando se proporciona; de lo contrario, se devuelve None. | ANY | No | - |
| `current_iteration_value` | El valor transportado por la iteración actual. Opcional; el primer elemento se transfiere a la salida cuando se proporciona; de lo contrario, se devuelve None. | ANY | No | - |
| `reuse_cache` | Controla si el resultado puede reutilizarse desde la caché. Cuando está habilitado, el nodo mantiene una huella estable para que los resultados en caché puedan reutilizarse. Cuando está deshabilitado, se genera una huella no coincidente para que el nodo se ejecute de nuevo en cada iteración. | BOOLEAN | Sí | - |

Nota: Este nodo admite entradas de lista, lo que significa que se espera que cada entrada llegue como una lista y el nodo solo emite el primer elemento de cada lista. También acepta entradas adicionales más allá de las enumeradas aquí.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-----------|-----------|
| `iteration_index` | El índice de la iteración actual. | INT |
| `is_first` | Indica si la iteración actual es la primera. | BOOLEAN |
| `is_last` | Indica si la iteración actual es la última. | BOOLEAN |
| `list_item` | El elemento tomado de la lista para esta iteración, o None cuando no se proporcionó ningún elemento. | ANY |
| `current_iteration_value` | El valor transportado por la iteración actual, o None cuando no se proporcionó ningún valor. | ANY |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopIteration/es.md)

---
**Source fingerprint (SHA-256):** `1d167860b89de0f7b435a3715f6d543cad7602648abb58575b572c0406631cda`
