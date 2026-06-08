# Criar Informações da Câmera

O nó Criar Informações da Câmera constrói uma estrutura de informações de câmera para renderização 3D. Ele suporta três modos para definir a câmera: órbita (rotação horizontal/vertical/distância ao redor de um alvo), look_at (posição explícita no mundo) e quaternion (posição mais rotação). O sistema de coordenadas é destro com Y como eixo vertical.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `modo` | Como definir a câmera: ângulos de órbita, uma posição explícita ou uma posição + quaternion. | COMBO | Sim | `"orbit"`<br>`"look_at"`<br>`"quaternion"` |
| `alvo_x` | Ponto de observação (pivô da órbita/alvo). No modo órbita, mova-o para panorâmica/transladar toda a câmera. Ignorado no modo quaternion. Padrão é a origem. (padrão: 0.0) | FLOAT | Não | -1000.0 a 1000.0 |
| `alvo_y` | Componente Y do ponto alvo. (padrão: 0.0) | FLOAT | Não | -1000.0 a 1000.0 |
| `alvo_z` | Componente Z do ponto alvo. (padrão: 0.0) | FLOAT | Não | -1000.0 a 1000.0 |
| `rolagem` | Rotação lateral da câmera em torno do eixo de visão, em graus. (padrão: 0.0) | FLOAT | Não | -180.0 a 180.0 |
| `fov` | Campo de visão vertical em graus. (padrão: 35.0) | FLOAT | Não | 1.0 a 120.0 |
| `zoom` | Zoom digital (multiplicador de distância focal). Valores maiores que 1 ampliam sem mover a câmera. (padrão: 1.0) | FLOAT | Não | 0.01 a 100.0 |
| `tipo_de_câmera` | Projeção usada pelo Render Splat: perspectiva (encurtamento) ou ortográfica (paralela). (padrão: "perspective") | COMBO | Não | `"perspective"`<br>`"orthographic"` |

### Parâmetros Específicos do Modo

Quando `mode` está definido como `"orbit"`, os seguintes parâmetros ficam disponíveis:

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `yaw` | Ângulo de rotação horizontal em torno do alvo. (padrão: 35.0) | FLOAT | Sim | -360.0 a 360.0 |
| `pitch` | Ângulo de rotação vertical em torno do alvo. (padrão: 30.0) | FLOAT | Sim | -89.0 a 89.0 |
| `distance` | Distância da câmera ao alvo. (padrão: 4.0) | FLOAT | Sim | 0.01 a 1000.0 |

Quando `mode` está definido como `"look_at"`, os seguintes parâmetros ficam disponíveis:

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `position_x` | Posição da câmera no espaço mundial (destro, Y para cima). (padrão: 4.0) | FLOAT | Sim | -1000.0 a 1000.0 |
| `position_y` | Componente Y da posição da câmera. (padrão: 4.0) | FLOAT | Sim | -1000.0 a 1000.0 |
| `position_z` | Componente Z da posição da câmera. (padrão: 4.0) | FLOAT | Sim | -1000.0 a 1000.0 |

Quando `mode` está definido como `"quaternion"`, os seguintes parâmetros ficam disponíveis:

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `position_x` | Posição da câmera no espaço mundial (destro, Y para cima). (padrão: 4.0) | FLOAT | Sim | -1000.0 a 1000.0 |
| `position_y` | Componente Y da posição da câmera. (padrão: 4.0) | FLOAT | Sim | -1000.0 a 1000.0 |
| `position_z` | Componente Z da posição da câmera. (padrão: 4.0) | FLOAT | Sim | -1000.0 a 1000.0 |
| `quat_x` | Componente X do quaternion de rotação mundial da câmera. (padrão: 0.0) | FLOAT | Sim | -1.0 a 1.0 |
| `quat_y` | Componente Y do quaternion de rotação mundial da câmera. (padrão: 0.0) | FLOAT | Sim | -1.0 a 1.0 |
| `quat_z` | Componente Z do quaternion de rotação mundial da câmera. (padrão: 0.0) | FLOAT | Sim | -1.0 a 1.0 |
| `quat_w` | Quaternion de rotação mundial da câmera (three.js: olha para o -Z local). Normalizado automaticamente. (padrão: 1.0) | FLOAT | Sim | -1.0 a 1.0 |

**Nota:** Os parâmetros `target_x`, `target_y` e `target_z` são ignorados quando `mode` está definido como `"quaternion"`. No modo `"orbit"`, esses parâmetros alvo definem o ponto pivô em torno do qual a câmera orbita.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `camera_info` | Estrutura de informações da câmera contendo posição, rotação, campo de visão, zoom e tipo de projeção para renderização 3D. | LOAD3DCAMERA |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateCameraInfo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `577c114130f72b753d5f15775fe05b3e1e734f5865cca32c576d042583f8e873`
