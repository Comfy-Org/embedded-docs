# UnwrapMesh

Genera un atlas UV para una malla 3D. La superficie se divide en gráficos, cada gráfico se aplana en dos dimensiones y los resultados se empaquetan en un atlas UV [0,1]. Los vértices en las costuras de los gráficos se duplican, por lo que la malla de salida puede contener más vértices que la de entrada.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `mesh` | La malla de entrada a desplegar. Acepta una sola malla o un lote de mallas. | MESH | Sí | — |
| `segmenter` | Algoritmo de gráficos a utilizar. pec: gráficos rápidos por colapso de aristas paralelas en GPU. adaptive: CPU, más lento. (por defecto: "pec") | COMBO | Sí | "pec"<br>"adaptive" |
| `resolution` | Resolución objetivo del atlas para la autoescala de densidad de texeles (0 = ajustar al contenido). (por defecto: 1024) | INT | Sí | 0 a 8192 (paso 256) |
| `padding` | Relleno de texeles entre gráficos. (por defecto: 1) | INT | Sí | 0 a 16 |
| `weld_distance` | Radio de fusión de vértices coincidentes como fracción de la extensión de la malla (0 = automático). Auméntelo a ~0.001 si obtiene gráficos por triángulo (entrada sin soldar). (por defecto: 0.0) | FLOAT | Sí | 0.0 a 1.0 (paso 0.0001) |

Nota: si la malla de entrada contiene vértices sin soldar (sopa de triángulos), el nodo puede advertir que la adyacencia de caras es baja y producir gráficos UV por cara; aumentar `weld_distance` fusiona los vértices coincidentes antes de desplegar.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `mesh` | La malla de entrada con un atlas UV generado en [0,1]. Los vértices de las costuras se duplican, por lo que el conteo de vértices de salida puede superar al de entrada. Los colores de vértice y la textura de la malla de entrada se conservan. | MESH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnwrapMesh/es.md)

---
**Source fingerprint (SHA-256):** `cf0dbbe43df507921e6e9795b42d5cb5691ccc2ae98a8bb17e02e3928ea0b815`
