# Girar Malha

Rotaciona uma malha 3D em torno dos eixos do mundo usando ângulos Euler XYZ (em graus) ou um quaternion. No modo Euler XYZ, as rotações são aplicadas como X, depois Y e depois Z; no modo quaternion, o quaternion (w, x, y, z) é normalizado automaticamente. A rotação é aplicada aos vértices da malha, e as normais e tangentes também são rotacionadas para que a iluminação e o sombreamento permaneçam corretos.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mode` | O modo de rotação a usar. `"euler_xyz"` aplica a rotação como ângulos X, depois Y e depois Z em torno dos eixos do mundo (em graus). `"quaternion"` usa um quaternion (w, x, y, z) que é normalizado automaticamente. | DYNAMIC_COMBO | Sim | `"euler_xyz"`<br>`"quaternion"` |
| `mesh` | A malha 3D a rotacionar. | MESH | Sim | — |

### Entradas do euler_xyz

Estas entradas aparecem quando `mode` está definido como `"euler_xyz"`.

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `angle_x` | Rotação em torno do eixo X em graus. (padrão: 0.0) | FLOAT | Não | -360.0 a 360.0 (passo: 0.1) |
| `angle_y` | Rotação em torno do eixo Y em graus. (padrão: 0.0) | FLOAT | Não | -360.0 a 360.0 (passo: 0.1) |
| `angle_z` | Rotação em torno do eixo Z em graus. (padrão: 0.0) | FLOAT | Não | -360.0 a 360.0 (passo: 0.1) |

### Entradas do quaternion

Estas entradas aparecem quando `mode` está definido como `"quaternion"`.

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `qw` | Componente W do quaternion (w, x, y, z). (padrão: 1.0) | FLOAT | Não | -1.0 a 1.0 (passo: 0.001) |
| `qx` | Componente X do quaternion (w, x, y, z). (padrão: 0.0) | FLOAT | Não | -1.0 a 1.0 (passo: 0.001) |
| `qy` | Componente Y do quaternion (w, x, y, z). (padrão: 0.0) | FLOAT | Não | -1.0 a 1.0 (passo: 0.001) |
| `qz` | Componente Z do quaternion (w, x, y, z). (padrão: 0.0) | FLOAT | Não | -1.0 a 1.0 (passo: 0.001) |

**Nota:** Quando `mode` é `"euler_xyz"` e todos os três ângulos são 0.0, ou quando `mode` é `"quaternion"` e o quaternion é a identidade (1, 0, 0, 0), a malha é retornada inalterada. O quaternion é normalizado automaticamente antes do uso; se sua magnitude estiver abaixo de 1e-8, o nó gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `mesh` | A malha rotacionada. Os vértices são rotacionados, e as normais são rotacionadas como direções. As tangentes têm seus componentes X, Y, Z rotacionados, enquanto o componente W (orientação) é mantido inalterado. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RotateMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `38b120a3f719264d1269275ecfefa145b507c688735e4a461bb89517c697674f`
