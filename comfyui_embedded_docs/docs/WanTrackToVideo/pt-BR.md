> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/pt-BR.md)

O nó WanTrackToVideo converte dados de rastreamento de movimento em sequências de vídeo, processando pontos de rastreamento e gerando quadros de vídeo correspondentes. Ele recebe coordenadas de rastreamento como entrada e produz condicionamentos de vídeo e representações latentes que podem ser usadas para geração de vídeo. Quando nenhum rastreamento é fornecido, ele recorre à conversão padrão de imagem para vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `positivo` | CONDITIONING | Sim | - | Condicionamento positivo para geração de vídeo |
| `negativo` | CONDITIONING | Sim | - | Condicionamento negativo para geração de vídeo |
| `vae` | VAE | Sim | - | Modelo VAE para codificação e decodificação |
| `faixas` | STRING | Sim | - | Dados de rastreamento em formato JSON como uma string multilinha (padrão: "[]") |
| `largura` | INT | Sim | 16 a MAX_RESOLUTION | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) |
| `altura` | INT | Sim | 16 a MAX_RESOLUTION | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) |
| `duração` | INT | Sim | 1 a MAX_RESOLUTION | Número de quadros no vídeo de saída (padrão: 81, passo: 4) |
| `tamanho_do_lote` | INT | Sim | 1 a 4096 | Número de vídeos a serem gerados simultaneamente (padrão: 1) |
| `temperatura` | FLOAT | Sim | 1.0 a 1000.0 | Parâmetro de temperatura para correção de movimento (padrão: 220.0, passo: 0.1) |
| `topk` | INT | Sim | 1 a 10 | Valor top-k para correção de movimento (padrão: 2) |
| `imagem_inicial` | IMAGE | Não | - | Imagem inicial para geração de vídeo |
| `clip_vision_output` | CLIPVISIONOUTPUT | Não | - | Saída de visão CLIP para condicionamento adicional |

**Nota:** Quando `tracks` contém dados de rastreamento válidos, o nó processa os rastros de movimento para gerar vídeo. Quando `tracks` está vazio, ele alterna para o modo padrão de imagem para vídeo. Se `start_image` for fornecido, ele inicializa o primeiro quadro da sequência de vídeo.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `positivo` | CONDITIONING | Condicionamento positivo com informações de rastreamento de movimento aplicadas |
| `negativo` | CONDITIONING | Condicionamento negativo com informações de rastreamento de movimento aplicadas |
| `latent` | LATENT | Representação latente do vídeo gerado |

---
**Source fingerprint (SHA-256):** `b3e12492d3dafa100266f6be8fe05e4d62b827f1a2bdb4029f804b107dc691ed`
