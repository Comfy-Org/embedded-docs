> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/pt-BR.md)

O nó WanSoundImageToVideo gera conteúdo de vídeo a partir de imagens com condicionamento de áudio opcional. Ele utiliza prompts de condicionamento positivo e negativo juntamente com um modelo VAE para criar latentes de vídeo, podendo incorporar imagens de referência, codificação de áudio, vídeos de controle e referências de movimento para orientar o processo de geração de vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `positivo` | CONDITIONING | Sim | - | Prompts de condicionamento positivo que orientam qual conteúdo deve aparecer no vídeo gerado |
| `negativo` | CONDITIONING | Sim | - | Prompts de condicionamento negativo que especificam qual conteúdo deve ser evitado no vídeo gerado |
| `vae` | VAE | Sim | - | Modelo VAE usado para codificar e decodificar as representações latentes do vídeo |
| `largura` | INT | Sim | 16 a MAX_RESOLUTION | Largura do vídeo de saída em pixels (padrão: 832, deve ser divisível por 16) |
| `altura` | INT | Sim | 16 a MAX_RESOLUTION | Altura do vídeo de saída em pixels (padrão: 480, deve ser divisível por 16) |
| `comprimento` | INT | Sim | 1 a MAX_RESOLUTION | Número de quadros no vídeo gerado (padrão: 77, deve ser divisível por 4) |
| `tamanho do lote` | INT | Sim | 1 a 4096 | Número de vídeos a serem gerados simultaneamente (padrão: 1) |
| `saída do codificador de áudio` | AUDIOENCODEROUTPUT | Não | - | Codificação de áudio opcional que pode influenciar a geração de vídeo com base nas características sonoras |
| `imagem de referência` | IMAGE | Não | - | Imagem de referência opcional que fornece orientação visual para o conteúdo do vídeo |
| `vídeo de controle` | IMAGE | Não | - | Vídeo de controle opcional que orienta o movimento e a estrutura do vídeo gerado |
| `referência de movimento` | IMAGE | Não | - | Referência de movimento opcional que fornece orientação para padrões de movimento no vídeo |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `positivo` | CONDITIONING | Condicionamento positivo processado que foi modificado para geração de vídeo |
| `negativo` | CONDITIONING | Condicionamento negativo processado que foi modificado para geração de vídeo |
| `latent` | LATENT | Representação do vídeo gerado no espaço latente que pode ser decodificada em quadros finais de vídeo |

---
**Source fingerprint (SHA-256):** `f80f82b8671294a14ecfecf91bc13febae0c91c5efa438467a4413d52dc82d3f`
