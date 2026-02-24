> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/pt-BR.md)

O nó WanTrackToVideo converte dados de rastreamento de movimento em sequências de vídeo, processando pontos de rastreamento e gerando os quadros de vídeo correspondentes. Ele recebe coordenadas de rastreamento como entrada e produz condicionamentos de vídeo e representações latentes que podem ser usadas para geração de vídeo. Quando nenhum rastreamento é fornecido, ele recorre à conversão padrão de imagem para vídeo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | Condicionamento positivo para geração de vídeo |
| `negative` | CONDITIONING | Sim | - | Condicionamento negativo para geração de vídeo |
| `vae` | VAE | Sim | - | Modelo VAE para codificação e decodificação |
| `tracks` | STRING | Sim | - | Dados de rastreamento em formato JSON como uma string de múltiplas linhas (padrão: "[]") |
| `width` | INT | Sim | 16 a MAX_RESOLUTION | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) |
| `height` | INT | Sim | 16 a MAX_RESOLUTION | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) |
| `length` | INT | Sim | 1 a MAX_RESOLUTION | Número de quadros no vídeo de saída (padrão: 81, passo: 4) |
| `batch_size` | INT | Sim | 1 a 4096 | Número de vídeos a serem gerados simultaneamente (padrão: 1) |
| `temperature` | FLOAT | Sim | 1.0 a 1000.0 | Parâmetro de temperatura para aplicação de movimento (padrão: 220.0, passo: 0.1) |
| `topk` | INT | Sim | 1 a 10 | Valor top-k para aplicação de movimento (padrão: 2) |
| `start_image` | IMAGE | Não | - | Imagem inicial para geração de vídeo |
| `clip_vision_output` | CLIPVISIONOUTPUT | Não | - | Saída de visão CLIP para condicionamento adicional |

**Observação:** Quando `tracks` contém dados de rastreamento válidos, o nó processa os rastreamentos de movimento para gerar o vídeo. Quando `tracks` está vazio, ele alterna para o modo padrão de imagem para vídeo. Se `start_image` for fornecida, ela inicializa o primeiro quadro da sequência de vídeo.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamento positivo com informações de rastreamento de movimento aplicadas |
| `negative` | CONDITIONING | Condicionamento negativo com informações de rastreamento de movimento aplicadas |
| `latent` | LATENT | Representação latente do vídeo gerado |
