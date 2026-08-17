# WanImagemParaVídeo

O nó WanImageToVideo prepara representações de condicionamento e latentes para tarefas de geração de vídeo. Ele cria um espaço latente vazio para a geração de vídeo e pode, opcionalmente, incorporar imagens iniciais e saídas do CLIP vision para orientar o processo de geração. O nó modifica as entradas de condicionamento positivo e negativo com base na imagem e nos dados de visão fornecidos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | Entrada de condicionamento positivo para orientar a geração | CONDITIONING | Sim | - |
| `negative` | Entrada de condicionamento negativo para orientar a geração | CONDITIONING | Sim | - |
| `vae` | Modelo VAE para codificar imagens no espaço latente | VAE | Sim | - |
| `width` | Largura do vídeo de saída (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `height` | Altura do vídeo de saída (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `length` | Número de quadros no vídeo (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `batch_size` | Número de vídeos a serem gerados em um lote (padrão: 1) | INT | Sim | 1 a 4096 |
| `clip_vision_output` | Saída opcional do CLIP vision para condicionamento adicional | CLIP_VISION_OUTPUT | Não | - |
| `start_image` | Imagem inicial opcional para inicializar a geração de vídeo. Quando fornecida, a imagem é redimensionada para corresponder à largura e à altura especificadas, e os primeiros quadros do vídeo são inicializados a partir dessa imagem. Os quadros restantes são preenchidos com valores cinza neutro (0,5). Apenas os primeiros `length` quadros da imagem são usados. | IMAGE | Não | - |

**Nota:** Quando `start_image` é fornecido, o nó codifica a sequência de imagens usando o VAE e aplica uma máscara às entradas de condicionamento. A máscara cobre todos os quadros, exceto aqueles inicializados pela imagem inicial, permitindo que a geração seja construída a partir da imagem fornecida. O parâmetro `clip_vision_output`, quando fornecido, adiciona condicionamento baseado em visão tanto às entradas positivas quanto negativas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo modificado com a incorporação de imagem e dados de visão | CONDITIONING |
| `negative` | Condicionamento negativo modificado com a incorporação de imagem e dados de visão | CONDITIONING |
| `latent` | Tensor de espaço latente vazio pronto para geração de vídeo, com formato [batch_size, 16, ((length-1)//4)+1, height//8, width//8] | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `46779f9f2f3da16826b7b547761a96597a3b6b43ce51a9c13367987642f3d5b7`
