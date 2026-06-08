Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/en.md)

O nó WanImageToVideo prepara representações de condicionamento e latentes para tarefas de geração de vídeo. Ele cria um espaço latente vazio para geração de vídeo e pode opcionalmente incorporar imagens iniciais e saídas de visão do CLIP para orientar o processo de geração de vídeo. O nó modifica as entradas de condicionamento positivo e negativo com base na imagem e nos dados de visão fornecidos.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamento positivo para orientar a geração | CONDITIONING | Sim | - |
| `negativo` | Entrada de condicionamento negativo para orientar a geração | CONDITIONING | Sim | - |
| `vae` | Modelo VAE para codificar imagens para o espaço latente | VAE | Sim | - |
| `largura` | Largura do vídeo de saída (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo de saída (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `duração` | Número de quadros no vídeo (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de vídeos a serem gerados em um lote (padrão: 1) | INT | Sim | 1 a 4096 |
| `clip_vision_output` | Saída opcional de visão do CLIP para condicionamento adicional | CLIP_VISION_OUTPUT | Não | - |
| `imagem_inicial` | Imagem inicial opcional para inicializar a geração do vídeo | IMAGE | Não | - |

**Nota:** Quando `start_image` é fornecido, o nó codifica a sequência de imagens e aplica mascaramento às entradas de condicionamento. O parâmetro `clip_vision_output`, quando fornecido, adiciona condicionamento baseado em visão às entradas positivas e negativas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | Condicionamento positivo modificado com dados de imagem e visão incorporados | CONDITIONING |
| `negativo` | Condicionamento negativo modificado com dados de imagem e visão incorporados | CONDITIONING |
| `latent` | Tensor de espaço latente vazio pronto para geração de vídeo | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e9f4350c43e48351523c04d82675c24f868df7b2109530c32b8e752a3ab61e8b`
