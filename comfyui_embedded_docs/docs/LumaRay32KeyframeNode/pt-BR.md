# Luma Ray 3.2 Quadro-chave

Este nó ancora uma imagem guia a uma posição específica na linha do tempo do vídeo de saída do Luma Ray 3.2. Conecte este nó à entrada "keyframes" do nó Luma Ray 3.2 Keyframes to Video e encadeie vários keyframes conectando a entrada opcional "keyframes".

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | Imagem guia a ser colocada no momento escolhido do vídeo de saída. | IMAGE | Sim | - |
| `position` | Como posicionar esta imagem na linha do tempo do vídeo de saída. | DYNAMIC_COMBO | Sim | "Fraction of duration (0.0-1.0)"<br>"Absolute time (seconds)" |
| `keyframes` | Keyframes anteriores opcionais para encadear com este. | LUMA_RAY32_KEYFRAME | Não | - |

### Entradas de Fração da duração (0.0-1.0)

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `fraction` | Onde no vídeo de saída esta imagem se aplica (0.0 = início, 1.0 = fim). Padrão: 0.0. | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |

### Entradas de Tempo absoluto (segundos)

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `seconds` | Tempo em segundos desde o início do vídeo de saída em que esta imagem se aplica. Padrão: 0.0. | FLOAT | Sim | 0.0 a 10.0 (passo: 0.1) |

O parâmetro `position` determina qual valor é usado para posicionar a imagem na linha do tempo. Apenas o subparâmetro pertencente à opção selecionada é exibido e usado: `fraction` para "Fraction of duration (0.0-1.0)" e `seconds` para "Absolute time (seconds)".

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `keyframes` | Uma cadeia de keyframes que inclui o novo keyframe combinado com quaisquer keyframes anteriores opcionais. | LUMA_RAY32_KEYFRAME |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframeNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b49d879888e6e83d6937068e799ea583ed5c90284e829ac496821eea330fe9c7`
