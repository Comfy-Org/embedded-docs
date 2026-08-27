# FillHoles

Este nodo rellena agujeros en una malla 3D detectando bordes de contorno abiertos y creando nuevas caras para cerrarlos. Se ejecuta en la GPU, conserva la geometría y las UV existentes, y puede procesar mallas individuales, listas de mallas o lotes de mallas.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `mesh` | La malla 3D a procesar. Acepta una malla individual, una lista de mallas o una malla por lotes. | MESH | Sí | - |
| `max_perimeter` | Perímetro máximo de agujero a rellenar. 0 lo desactiva. (predeterminado: 0.03) | FLOAT | Sí | 0.0 to no upper limit |
| `weld_epsilon_rel` | Tolerancia de pre-soldadura (fracción de la diagonal de la caja delimitadora); la detección de contornos requiere vértices soldados. 0 la omite. (predeterminado: 1e-5) | FLOAT | Sí | 0.0 to no upper limit |
| `max_vertices` | Tope de vértices de contorno por ciclo; el abanico de centroide solo funciona para agujeros pequeños casi planos. Mantener ≤16. (predeterminado: 16) | INT | Sí | 3 to 1024 |
| `fill_chains` | También rellena cadenas abiertas (no solo ciclos). Genera ruido; OFF coincide con cumesh. (predeterminado: False) | BOOLEAN | Sí | True or False |

Nota: Cuando `weld_epsilon_rel` es mayor que 0, el nodo pre-suelda los vértices duplicados antes de detectar agujeros. La tolerancia de soldadura comienza en la fracción indicada de la diagonal de la caja delimitadora y aumenta automáticamente duplicándose hasta que la malla se considere soldada o la tolerancia alcance un límite de 1e-2. Los agujeros con más de 8 vértices de contorno utilizan un relleno de abanico de centroide (insertando un nuevo vértice central), mientras que los agujeros más pequeños utilizan un relleno de abanico de vértice que reutiliza un vértice de contorno existente.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `mesh` | La malla con los agujeros rellenados, que coincide con el formato de lote de entrada. | MESH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FillHoles/es.md)

---
**Source fingerprint (SHA-256):** `c0fd7f0c2d6eea098efb1dcfd80eaa52997e185b9c442b483f75318eea082196`
