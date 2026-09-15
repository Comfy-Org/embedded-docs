# WanImagemParaVídeo

O nó WanImageToVideo prepara condicionamento e representações latentes para geração de vídeo. Ele cria um espaço latente vazio para o vídeo e pode, opcionalmente, incorporar uma imagem inicial e uma saída de visão CLIP para orientar a geração. Tanto as entradas de condicionamento positivo quanto as de condicionamento negativo são atualizadas com a imagem e os dados de visão fornecidos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamento positivo usada para orientar a geração | CONDITIONING | Sim | - |
| `negativo` | Entrada de condicionamento negativo usada para orientar a geração | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar imagens no espaço latente | VAE | Sim | - |
| `largura` | Largura do vídeo gerado (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo gerado (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `duração` | Número de quadros no vídeo (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de vídeos a gerar em um lote (padrão: 1) | INT | Sim | 1 a 4096 |
| `clip_vision_output` | Saída de visão CLIP opcional adicionada como condicionamento extra tanto às entradas positiva quanto negativa | CLIP_VISION_OUTPUT | Não | - |
| `imagem_inicial` | Imagem inicial opcional usada para inicializar o vídeo. Quando fornecida, ela é redimensionada para a `width` e a `height` especificadas e colocada no início da sequência de quadros; quaisquer quadros além de `length` são ignorados. Os quadros restantes são preenchidos com valores de cinza neutro (0.5). | IMAGE | Não | - |

**Nota:** Quando `start_image` é fornecida, a sequência de quadros é codificada com o VAE e uma máscara é aplicada ao condicionamento. A máscara é definida como 0 para os quadros cobertos pela imagem inicial e como 1 para os quadros restantes, para que a geração continue a partir da imagem fornecida. Apenas os três primeiros canais de cor (RGB) da imagem são usados durante a codificação. Tanto o condicionamento positivo quanto o negativo recebem a mesma imagem latente concatenada, a máscara e, se fornecida, a saída de visão CLIP.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo, atualizado com a imagem e os dados de visão | CONDITIONING |
| `negative` | Condicionamento negativo, atualizado com a imagem e os dados de visão | CONDITIONING |
| `latent` | Tensor latente vazio pronto para geração de vídeo, com shape [batch_size, 16, ((length-1)//4)+1, height//8, width//8] | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `46779f9f2f3da16826b7b547761a96597a3b6b43ce51a9c13367987642f3d5b7`
