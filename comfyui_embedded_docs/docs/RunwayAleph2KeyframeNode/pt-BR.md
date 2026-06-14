# Nó de Keyframe Runway Aleph2

Este nó ancora uma imagem de guia a um momento específico do seu vídeo de entrada, para que o modelo Aleph2 direcione a edição naquele ponto do seu material. Conecte este nó à entrada "keyframes" do nó Runway Aleph2 Video to Video e encadeie vários deles (até 5) através da entrada opcional "keyframes".

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `image` | A imagem de guia a ser aplicada no momento escolhido do vídeo de entrada. | IMAGE | Sim | - |
| `timing` | Como posicionar esta imagem na linha do tempo do vídeo de entrada. | COMBO | Sim | Ver abaixo |
| `keyframes` | Keyframes anteriores opcionais para encadear com este. | KEYFRAME | Não | - |

### Opções do Parâmetro Timing

O parâmetro `timing` possui dois modos:

| Modo | Subparâmetro | Descrição | Faixa |
|------|--------------|-----------|-------|
| "Segundos absolutos" | `seconds` | Tempo em segundos a partir do início do vídeo de entrada onde esta imagem se aplica (padrão: 0,0) | 0,0 a 30,0, passo 0,1 |
| "Fração da duração" | `fraction` | Onde no vídeo de entrada esta imagem se aplica, como uma fração de sua duração (0,0 = início, 1,0 = fim) (padrão: 0,0) | 0,0 a 1,0, passo 0,01 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `keyframes` | Uma cadeia de keyframes incluindo este e quaisquer keyframes previamente conectados. | KEYFRAME |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2KeyframeNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b5ac6553166b7366fd35f97740861be163f91bc2353f5f83bdc2f04bf40f8478`
