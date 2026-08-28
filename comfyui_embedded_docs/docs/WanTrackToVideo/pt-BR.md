# WanTrackToVideo

O nó WanTrackToVideo converte dados de rastreamento de movimento em sequências de vídeo processando pontos de rastreamento e gerando os quadros de vídeo correspondentes. Ele recebe coordenadas de rastreamento como entrada e produz condicionamento de vídeo e representações latentes que podem ser usados para geração de vídeo. Quando nenhuma trilha é fornecida, ele recorre à conversão padrão de imagem para vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | Condicionamento positivo para geração de vídeo | CONDITIONING | Sim | - |
| `negativo` | Condicionamento negativo para geração de vídeo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE para codificação e decodificação | VAE | Sim | - |
| `faixas` | Dados de rastreamento formatados em JSON como uma string multilinha (padrão: "[]"). Cada trilha é preenchida ou truncada para um comprimento fixo de 121 pontos. | STRING | Sim | - |
| `largura` | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 to MAX_RESOLUTION |
| `altura` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 to MAX_RESOLUTION |
| `duração` | Número de quadros no vídeo de saída (padrão: 81, passo: 4) | INT | Sim | 1 to MAX_RESOLUTION |
| `tamanho_do_lote` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `temperatura` | Parâmetro de temperatura para a montagem de movimento (padrão: 220.0, passo: 0.1) | FLOAT | Sim | 1.0 a 1000.0 |
| `topk` | Valor top-k para a montagem de movimento (padrão: 2) | INT | Sim | 1 a 10 |
| `imagem_inicial` | Imagem inicial para geração de vídeo | IMAGE | Não | - |
| `clip_vision_output` | Saída do CLIP vision para condicionamento adicional | CLIP_VISION_OUTPUT | Não | - |

**Nota:** Quando `tracks` contém dados de rastreamento válidos, o nó processa as trilhas de movimento para gerar vídeo. Quando `tracks` está vazio, ele alterna para o modo padrão de imagem para vídeo. Se `start_image` for fornecido, ele inicializa o primeiro quadro da sequência de vídeo, e o resultado da montagem de movimento é adicionado ao condicionamento positivo e negativo. Se `clip_vision_output` for fornecido, ele também é adicionado a ambos os condicionamentos positivo e negativo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positivo` | Condicionamento positivo com informações de trilhas de movimento aplicadas | CONDITIONING |
| `negativo` | Condicionamento negativo com informações de trilhas de movimento aplicadas | CONDITIONING |
| `latente` | Representação latente do vídeo gerado | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e67fe326dd7e5ae63ddc35946d8144138d04d9523ec1ad2e08ea6bc1dc9325da`
