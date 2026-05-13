> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/en.md)

O nó WanImageToVideo prepara representações de condicionamento e latentes para tarefas de geração de vídeo. Ele cria um espaço latente vazio para geração de vídeo e pode opcionalmente incorporar imagens iniciais e saídas de visão do CLIP para orientar o processo de geração de vídeo. O nó modifica as entradas de condicionamento positivo e negativo com base na imagem e nos dados de visão fornecidos.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `positive` | CONDITIONING | Sim | - | Entrada de condicionamento positivo para orientar a geração |
| `negative` | CONDITIONING | Sim | - | Entrada de condicionamento negativo para orientar a geração |
| `vae` | VAE | Sim | - | Modelo VAE para codificar imagens para o espaço latente |
| `width` | INT | Sim | 16 a MAX_RESOLUTION | Largura do vídeo de saída (padrão: 832, passo: 16) |
| `height` | INT | Sim | 16 a MAX_RESOLUTION | Altura do vídeo de saída (padrão: 480, passo: 16) |
| `length` | INT | Sim | 1 a MAX_RESOLUTION | Número de quadros no vídeo (padrão: 81, passo: 4) |
| `batch_size` | INT | Sim | 1 a 4096 | Número de vídeos a serem gerados em um lote (padrão: 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Não | - | Saída opcional de visão do CLIP para condicionamento adicional |
| `start_image` | IMAGE | Não | - | Imagem inicial opcional para inicializar a geração do vídeo |

**Nota:** Quando `start_image` é fornecido, o nó codifica a sequência de imagens e aplica mascaramento às entradas de condicionamento. O parâmetro `clip_vision_output`, quando fornecido, adiciona condicionamento baseado em visão às entradas positivas e negativas.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `positive` | CONDITIONING | Condicionamento positivo modificado com dados de imagem e visão incorporados |
| `negative` | CONDITIONING | Condicionamento negativo modificado com dados de imagem e visão incorporados |
| `latent` | LATENT | Tensor de espaço latente vazio pronto para geração de vídeo |

---
**Source fingerprint (SHA-256):** `e9f4350c43e48351523c04d82675c24f868df7b2109530c32b8e752a3ab61e8b`
