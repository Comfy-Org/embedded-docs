> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/pt-BR.md)

O nó WanSoundImageToVideoExtend estende um latente de vídeo existente gerando quadros adicionais, opcionalmente guiado por áudio, uma imagem de referência e um vídeo de controle. Ele recebe um latente de vídeo inicial e produz uma sequência de vídeo mais longa, usando as sugestões de condicionamento e pistas de áudio fornecidas para influenciar o novo conteúdo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `positivo` | CONDITIONING | Sim | - | Sugestões de condicionamento positivo que orientam o que o vídeo deve incluir |
| `negativo` | CONDITIONING | Sim | - | Sugestões de condicionamento negativo que especificam o que o vídeo deve evitar |
| `vae` | VAE | Sim | - | Autoencoder Variacional usado para codificar e decodificar quadros de vídeo |
| `comprimento` | INT | Sim | 1 a MAX_RESOLUTION | Número total de quadros a serem gerados para a sequência de vídeo (padrão: 77, passo: 4) |
| `latente de vídeo` | LATENT | Sim | - | Representação latente de vídeo inicial que serve como ponto de partida para a extensão |
| `saída do codificador de áudio` | AUDIOENCODEROUTPUT | Não | - | Embeddings de áudio opcionais que podem influenciar a geração de vídeo com base nas características do som |
| `imagem de referência` | IMAGE | Não | - | Imagem de referência opcional que fornece orientação visual para a geração do vídeo |
| `vídeo de controle` | IMAGE | Não | - | Vídeo de controle opcional que pode guiar o movimento e o estilo do vídeo gerado |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `positivo` | CONDITIONING | Condicionamento positivo processado com contexto de vídeo aplicado |
| `negativo` | CONDITIONING | Condicionamento negativo processado com contexto de vídeo aplicado |
| `latent` | LATENT | Representação latente de vídeo gerada contendo a sequência de vídeo estendida |

---
**Source fingerprint (SHA-256):** `fc9aee5d51e96b864da7d75f592f07691be8b970346998b209b3ad8a72308ecb`
