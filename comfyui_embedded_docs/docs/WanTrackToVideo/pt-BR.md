O nó WanTrackToVideo converte dados de rastreamento de movimento em sequências de vídeo, processando pontos de rastreamento e gerando quadros de vídeo correspondentes. Ele recebe coordenadas de rastreamento como entrada e produz condicionamentos de vídeo e representações latentes que podem ser usadas para geração de vídeo. Quando nenhum rastreamento é fornecido, ele recorre à conversão padrão de imagem para vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | Condicionamento positivo para geração de vídeo | CONDITIONING | Sim | - |
| `negativo` | Condicionamento negativo para geração de vídeo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE para codificação e decodificação | VAE | Sim | - |
| `faixas` | Dados de rastreamento em formato JSON como uma string multilinha (padrão: "[]") | STRING | Sim | - |
| `largura` | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `duração` | Número de quadros no vídeo de saída (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `temperatura` | Parâmetro de temperatura para correção de movimento (padrão: 220.0, passo: 0.1) | FLOAT | Sim | 1.0 a 1000.0 |
| `topk` | Valor top-k para correção de movimento (padrão: 2) | INT | Sim | 1 a 10 |
| `imagem_inicial` | Imagem inicial para geração de vídeo | IMAGE | Não | - |
| `clip_vision_output` | Saída de visão CLIP para condicionamento adicional | CLIPVISIONOUTPUT | Não | - |

**Nota:** Quando `tracks` contém dados de rastreamento válidos, o nó processa os rastros de movimento para gerar vídeo. Quando `tracks` está vazio, ele alterna para o modo padrão de imagem para vídeo. Se `start_image` for fornecido, ele inicializa o primeiro quadro da sequência de vídeo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | Condicionamento positivo com informações de rastreamento de movimento aplicadas | CONDITIONING |
| `negativo` | Condicionamento negativo com informações de rastreamento de movimento aplicadas | CONDITIONING |
| `latent` | Representação latente do vídeo gerado | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b3e12492d3dafa100266f6be8fe05e4d62b827f1a2bdb4029f804b107dc691ed`
