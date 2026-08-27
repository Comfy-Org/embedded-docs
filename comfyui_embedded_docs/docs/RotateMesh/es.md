# RotateMesh

Rota una malla 3D alrededor de los ejes globales mediante ángulos de Euler XYZ (en grados) o un cuaternión. La rotación se aplica a los vértices de la malla, y las normales y las tangentes también se rotan para que la iluminación y el sombreado sigan siendo correctos.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `mode` | El modo de rotación que se utilizará. `"euler_xyz"` aplica la rotación como ángulos X, luego Y y luego Z alrededor de los ejes globales (en grados). `"quaternion"` utiliza un cuaternión (w, x, y, z) que se normaliza automáticamente. | DYNAMIC_COMBO | Sí | `"euler_xyz"`<br>`"quaternion"` |
| `mesh` | La malla 3D que se va a rotar. | MESH | Sí | — |

### Entradas de euler_xyz

Estas entradas aparecen cuando `mode` se establece en `"euler_xyz"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `angle_x` | Rotación alrededor del eje X en grados. (por defecto: 0.0) | FLOAT | No | -360.0 a 360.0 (paso: 0.1) |
| `angle_y` | Rotación alrededor del eje Y en grados. (por defecto: 0.0) | FLOAT | No | -360.0 a 360.0 (paso: 0.1) |
| `angle_z` | Rotación alrededor del eje Z en grados. (por defecto: 0.0) | FLOAT | No | -360.0 a 360.0 (paso: 0.1) |

### Entradas de quaternion

Estas entradas aparecen cuando `mode` se establece en `"quaternion"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `qw` | Componente W del cuaternión (w, x, y, z). (por defecto: 1.0) | FLOAT | No | -1.0 a 1.0 (paso: 0.001) |
| `qx` | Componente X del cuaternión (w, x, y, z). (por defecto: 0.0) | FLOAT | No | -1.0 a 1.0 (paso: 0.001) |
| `qy` | Componente Y del cuaternión (w, x, y, z). (por defecto: 0.0) | FLOAT | No | -1.0 a 1.0 (paso: 0.001) |
| `qz` | Componente Z del cuaternión (w, x, y, z). (por defecto: 0.0) | FLOAT | No | -1.0 a 1.0 (paso: 0.001) |

**Nota:** Cuando `mode` es `"euler_xyz"` y los tres ángulos son 0.0, o cuando `mode` es `"quaternion"` y el cuaternión es la identidad (1, 0, 0, 0), la malla se devuelve sin cambios. El cuaternión se normaliza automáticamente antes de usarse; si su magnitud está demasiado cerca de cero, el nodo genera un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `mesh` | La malla rotada. Los vértices se rotan y las normales se rotan como direcciones. Los componentes X, Y y Z de las tangentes se rotan, mientras que el componente W (lateralidad) se mantiene sin cambios. | MESH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RotateMesh/es.md)

---
**Source fingerprint (SHA-256):** `38b120a3f719264d1269275ecfefa145b507c688735e4a461bb89517c697674f`
