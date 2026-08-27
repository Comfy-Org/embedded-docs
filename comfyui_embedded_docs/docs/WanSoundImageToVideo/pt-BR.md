# WanSoundImageToVideo

O nó WanSoundImageToVideo gera conteúdo de vídeo a partir de imagens com condicionamento de áudio opcional. Ele recebe prompts de condicionamento positivos e negativos juntamente com um modelo VAE para criar latentes de vídeo, e pode incorporar imagens de referência, codificação de áudio, vídeos de controle e referências de movimento para orientar o processo de geração de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | Prompts de condicionamento positivos que orientam qual conteúdo deve aparecer no vídeo gerado | CONDITIONING | Sim | - |
| `negativo` | Prompts de condicionamento negativos que especificam qual conteúdo deve ser evitado no vídeo gerado | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar e decodificar as representações latentes do vídeo | VAE | Sim | - |
| `largura` | Largura do vídeo de saída em pixels (padrão: 832, deve ser divisível por 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo de saída em pixels (padrão: 480, deve ser divisível por 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `comprimento` | Número de quadros no vídeo gerado (padrão: 77, deve ser divisível por 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho do lote` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `saída do codificador de áudio` | Codificação de áudio opcional que pode influenciar a geração de vídeo com base nas características do som. Quando fornecida, as características de áudio são interpoladas e usadas para condicionar a geração do vídeo. | AUDIO_ENCODER_OUTPUT | Não | - |
| `imagem de referência` | Imagem de referência opcional que fornece orientação visual para o conteúdo do vídeo. A imagem é redimensionada para corresponder à largura e altura especificadas e, em seguida, codificada em uma representação latente. Apenas a primeira imagem da entrada é usada como referência. | IMAGE | Não | - |
| `vídeo de controle` | Vídeo de controle opcional que orienta o movimento e a estrutura do vídeo gerado. O vídeo é redimensionado e codificado e, em seguida, usado para condicionar a saída. Apenas os primeiros `length` quadros são usados. | IMAGE | Não | - |
| `referência de movimento` | Referência de movimento opcional que fornece orientação para os padrões de movimento no vídeo. Se a entrada tiver mais de 73 quadros, apenas os últimos 73 serão usados. Se menos de 73 quadros forem fornecidos, a sequência será preenchida com quadros neutros. | IMAGE | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positivo` | Condicionamento positivo processado, modificado para geração de vídeo, incluindo embeddings de áudio, latentes de referência, referências de movimento e condicionamento de vídeo de controle | CONDITIONING |
| `negativo` | Condicionamento negativo processado, modificado para geração de vídeo, incluindo embeddings de áudio (definidos como zero), latentes de referência, referências de movimento e condicionamento de vídeo de controle | CONDITIONING |
| `latente` | Representação de vídeo gerada no espaço latente que pode ser decodificada em quadros finais de vídeo. O tensor latente tem forma [batch_size, 16, latent_t, height/8, width/8], em que latent_t é derivado do parâmetro `length` | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b1148cd00d8999dd6842e3c2fb13655fda8f20d5befed975a6d1652688b2807c`
