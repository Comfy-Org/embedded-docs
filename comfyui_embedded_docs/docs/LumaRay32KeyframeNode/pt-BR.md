# Luma Ray 3.2 Quadro-chave

Este nó ancora uma imagem guia a uma posição específica na linha do tempo do vídeo de saída do Luma Ray 3.2. Conecte este nó à entrada `keyframes` do nó Luma Ray 3.2 Keyframes to Video e encadeie vários keyframes conectando a entrada opcional `keyframes`.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `image` | Imagem guia para colocar no momento escolhido do vídeo de saída. | IMAGE | Sim | - |
| `position` | Como colocar esta imagem na linha do tempo do vídeo de saída. | DYNAMIC_COMBO | Sim | "Fraction of duration (0.0-1.0)"<br>"Absolute time (seconds)" |
| `keyframes` | Keyframes anteriores opcionais para encadear com este. | LUMA_RAY32_KEYFRAME | Não | - |

Quando "Fraction of duration (0.0-1.0)" for selecionado para o parâmetro `position`, você pode especificar um valor `fraction` (padrão: 0.0, intervalo: 0.0 a 1.0, passo: 0.01) que determina onde no vídeo de saída esta imagem é aplicada (0.0 = início, 1.0 = fim).

Quando "Absolute time (seconds)" for selecionado para o parâmetro `position`, você pode especificar um valor `seconds` (padrão: 0.0, intervalo: 0.0 a 10.0, passo: 0.1) que determina o tempo em segundos a partir do início do vídeo de saída onde esta imagem é aplicada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `keyframes` | Um encadeamento de keyframes que inclui o novo keyframe combinado com quaisquer keyframes anteriores opcionais. | LUMA_RAY32_KEYFRAME |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframeNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b49d879888e6e83d6937068e799ea583ed5c90284e829ac496821eea330fe9c7`
