> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/pt-BR.md)

O nó WanSoundImageToVideo gera conteúdo de vídeo a partir de imagens com condicionamento de áudio opcional. Ele recebe *prompts* de condicionamento positivo e negativo, juntamente com um modelo VAE, para criar latentes de vídeo, e pode incorporar imagens de referência, codificação de áudio, vídeos de controle e referências de movimento para orientar o processo de geração de vídeo.

## Visão Geral

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | *Prompts* de condicionamento positivo que orientam qual conteúdo deve aparecer no vídeo gerado |
| `negative` | CONDITIONING | Sim | - | *Prompts* de condicionamento negativo que especificam qual conteúdo deve ser evitado no vídeo gerado |
| `vae` | VAE | Sim | - | Modelo VAE usado para codificar e decodificar as representações latentes do vídeo |
| `width` | INT | Sim | 16 a MAX_RESOLUTION | Largura do vídeo de saída em pixels (padrão: 832, deve ser divisível por 16) |
| `height` | INT | Sim | 16 a MAX_RESOLUTION | Altura do vídeo de saída em pixels (padrão: 480, deve ser divisível por 16) |
| `length` | INT | Sim | 1 a MAX_RESOLUTION | Número de quadros no vídeo gerado (padrão: 77, deve ser divisível por 4) |
| `batch_size` | INT | Sim | 1 a 4096 | Número de vídeos a serem gerados simultaneamente (padrão: 1) |
| `audio_encoder_output` | AUDIOENCODEROUTPUT | Não | - | Codificação de áudio opcional que pode influenciar a geração do vídeo com base nas características do som |
| `ref_image` | IMAGE | Não | - | Imagem de referência opcional que fornece orientação visual para o conteúdo do vídeo |
| `control_video` | IMAGE | Não | - | Vídeo de controle opcional que orienta o movimento e a estrutura do vídeo gerado |
| `ref_motion` | IMAGE | Não | - | Referência de movimento opcional que fornece orientação para os padrões de movimento no vídeo |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamento positivo processado que foi modificado para geração de vídeo |
| `negative` | CONDITIONING | Condicionamento negativo processado que foi modificado para geração de vídeo |
| `latent` | LATENT | Representação do vídeo gerado no espaço latente, que pode ser decodificada em quadros de vídeo finais |
