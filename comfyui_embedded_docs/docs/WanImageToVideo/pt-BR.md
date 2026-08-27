# WanImagemParaVídeo

O nó WanImageToVideo prepara representações de condicionamento e latentes para tarefas de geração de vídeo. Ele cria um espaço latente vazio para a geração de vídeo e pode, opcionalmente, incorporar imagens iniciais e saídas de visão do CLIP para orientar o processo de geração. O nó modifica tanto as entradas de condicionamento positivo quanto negativo com base na imagem e nos dados de visão fornecidos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamento positivo para orientar a geração | CONDITIONING | Sim | - |
| `negativo` | Entrada de condicionamento negativo para orientar a geração | CONDITIONING | Sim | - |
| `vae` | Modelo VAE para codificar imagens no espaço latente | VAE | Sim | - |
| `largura` | Largura do vídeo de saída (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo de saída (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `duração` | Número de quadros no vídeo (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de vídeos a serem gerados em um lote (padrão: 1) | INT | Sim | 1 a 4096 |
| `clip_vision_output` | Saída de visão do CLIP opcional para condicionamento adicional | CLIP_VISION_OUTPUT | Não | - |
| `imagem_inicial` | Imagem inicial opcional para inicializar a geração de vídeo. Quando fornecida, a imagem é redimensionada para corresponder à largura e à altura especificadas, e os primeiros quadros do vídeo são inicializados a partir dela. Os quadros restantes são preenchidos com valores neutros de cinza (0,5). Quaisquer quadros além de `length` são ignorados. | IMAGE | Não | - |

**Observação:** Quando `start_image` é fornecida, o nó codifica a sequência de imagens usando o VAE e aplica uma máscara às entradas de condicionamento. A máscara cobre todos os quadros, exceto aqueles inicializados pela imagem inicial, permitindo que a geração se baseie na imagem fornecida. Apenas os três primeiros canais de cor (RGB) da imagem são usados durante a codificação. O parâmetro `clip_vision_output`, quando fornecido, adiciona condicionamento baseado em visão tanto às entradas positivas quanto negativas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positivo` | Condicionamento positivo modificado com dados de imagem e visão incorporados | CONDITIONING |
| `negativo` | Condicionamento negativo modificado com dados de imagem e visão incorporados | CONDITIONING |
| `latente` | Tensor de espaço latente vazio pronto para geração de vídeo, com formato [batch_size, 16, ((length-1)//4)+1, height//8, width//8] | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `46779f9f2f3da16826b7b547761a96597a3b6b43ce51a9c13367987642f3d5b7`
