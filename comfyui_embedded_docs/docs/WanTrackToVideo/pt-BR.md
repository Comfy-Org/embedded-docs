# WanTrackToVideo

O nó WanTrackToVideo usa dados de rastreamento de movimento (trajetórias de pontos) para orientar a geração de vídeo. Ele processa os rastreamentos, opcionalmente os combina com uma imagem inicial e produz saídas positivas e negativas condicionadas, além de um tensor latente para o modelo de vídeo Wan. Quando nenhum rastreamento válido é fornecido, ele usa a conversão padrão de imagem para vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positive` | Condicionamento positivo para geração de vídeo | CONDITIONING | Sim | - |
| `negative` | Condicionamento negativo para geração de vídeo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar quadros de vídeo | VAE | Sim | - |
| `tracks` | Dados de rastreamento formatados em JSON como uma string de várias linhas (padrão: "[]") | STRING | Sim | - |
| `width` | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `height` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `length` | Número de quadros no vídeo de saída (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `batch_size` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `temperature` | Parâmetro avançado de temperatura para correção de movimento (padrão: 220.0, passo: 0.1) | FLOAT | Sim | 1.0 a 1000.0 |
| `topk` | Valor avançado de top-k para correção de movimento (padrão: 2) | INT | Sim | 1 a 10 |
| `start_image` | Imagem inicial usada para o primeiro quadro da geração de vídeo | IMAGE | Sim | - |
| `clip_vision_output` | Saída de visão CLIP para condicionamento adicional | CLIP_VISION_OUTPUT | Não | - |

**Notas:**
- A entrada `tracks` espera uma string JSON ou uma lista de strings JSON contendo dados de rastreamento de pontos. Se `tracks` estiver vazia ou não puder ser analisada, o nó usa o comportamento padrão do WanImageToVideo.
- Quando `start_image` está presente, ela é redimensionada para corresponder a `width` e `height` e usada como o primeiro quadro da sequência de vídeo.
- Quando `clip_vision_output` é fornecido, ele é adicionado ao condicionamento positivo e negativo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo com informações de rastreamento de movimento e imagem opcional aplicadas | CONDITIONING |
| `negative` | Condicionamento negativo com informações de rastreamento de movimento e imagem opcional aplicadas | CONDITIONING |
| `latent` | Tensor latente preenchido com zeros, dimensionado para as dimensões, comprimento e tamanho do lote solicitados do vídeo | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e67fe326dd7e5ae63ddc35946d8144138d04d9523ec1ad2e08ea6bc1dc9325da`
