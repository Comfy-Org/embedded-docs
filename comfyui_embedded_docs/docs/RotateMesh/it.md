# RotateMesh

Ruota una mesh 3D attorno agli assi globali usando angoli Euler XYZ (in gradi) oppure un quaternione. Nella modalità Euler XYZ, le rotazioni vengono applicate come X, poi Y, poi Z; nella modalità quaternion, il quaternione (w, x, y, z) viene normalizzato automaticamente. La rotazione viene applicata ai vertici della mesh; anche le normali e le tangenti vengono ruotate, così che illuminazione e ombreggiatura rimangano corrette.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `mode` | La modalità di rotazione da usare. `"euler_xyz"` applica la rotazione come angoli X, poi Y, poi Z attorno agli assi globali (in gradi). `"quaternion"` usa un quaternione (w, x, y, z) che viene normalizzato automaticamente. | DYNAMIC_COMBO | Sì | `"euler_xyz"`<br>`"quaternion"` |
| `mesh` | La mesh 3D da ruotare. | MESH | Sì | — |

### Input di euler_xyz

Questi input compaiono quando `mode` è impostato su `"euler_xyz"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `angle_x` | Rotazione attorno all'asse X in gradi. (predefinito: 0.0) | FLOAT | No | -360.0 a 360.0 (passo: 0.1) |
| `angle_y` | Rotazione attorno all'asse Y in gradi. (predefinito: 0.0) | FLOAT | No | -360.0 a 360.0 (passo: 0.1) |
| `angle_z` | Rotazione attorno all'asse Z in gradi. (predefinito: 0.0) | FLOAT | No | -360.0 a 360.0 (passo: 0.1) |

### Input di quaternion

Questi input compaiono quando `mode` è impostato su `"quaternion"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `qw` | Componente W del quaternione (w, x, y, z). (predefinito: 1.0) | FLOAT | No | -1.0 a 1.0 (passo: 0.001) |
| `qx` | Componente X del quaternione (w, x, y, z). (predefinito: 0.0) | FLOAT | No | -1.0 a 1.0 (passo: 0.001) |
| `qy` | Componente Y del quaternione (w, x, y, z). (predefinito: 0.0) | FLOAT | No | -1.0 a 1.0 (passo: 0.001) |
| `qz` | Componente Z del quaternione (w, x, y, z). (predefinito: 0.0) | FLOAT | No | -1.0 a 1.0 (passo: 0.001) |

**Nota:** Quando `mode` è `"euler_xyz"` e tutti e tre gli angoli sono 0.0, oppure quando `mode` è `"quaternion"` e il quaternione è l'identità (1, 0, 0, 0), la mesh viene restituita invariata. Il quaternione viene normalizzato automaticamente prima dell'uso; se il suo modulo è inferiore a 1e-8, il nodo genera un errore.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `mesh` | La mesh ruotata. I vertici vengono ruotati e le normali vengono ruotate come direzioni. Per le tangenti, le componenti X, Y e Z vengono ruotate, mentre la componente W (destrorsità) viene mantenuta invariata. | MESH |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RotateMesh/it.md)

---
**Source fingerprint (SHA-256):** `38b120a3f719264d1269275ecfefa145b507c688735e4a461bb89517c697674f`
