# MergeMeshes

MergeMeshes combina múltiples entradas de malla en una sola malla apilando sus vértices, caras, coordenadas UV y colores de vértice, y ajustando los índices de las caras para que el resultado sea una única malla continua.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `meshes` | Ranura ampliable: conecta de 2 a 50 objetos de malla (denominados `mesh_1`, `mesh_2`, ..., `mesh_50`). Todas las mallas conectadas se fusionan en una única malla de salida. | MESH | Sí | 2 a 50 mallas |

**Nota:** Solo se utiliza el primer elemento de malla de cada lote de mallas de entrada. Si alguna malla de entrada tiene datos UV, la salida incluye UV y las mallas sin UV reciben valores UV rellenos con ceros. Si alguna malla de entrada tiene colores de vértice, la salida incluye colores de vértice; las mallas sin colores reciben colores blancos (valor 1), y los canales de color se rellenan hasta el mayor número de canales encontrado entre las entradas. Solo se conserva la textura de la primera entrada que la proporcione; las texturas adicionales se descartan.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `mesh` | La malla fusionada que contiene todos los vértices, caras, UV y colores de entrada combinados en una sola malla. | MESH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeMeshes/es.md)

---
**Source fingerprint (SHA-256):** `0ce49b522f6348d524df20d6c27eb8bd9575c4a781790f6f8e3ac4f3ee255d38`
