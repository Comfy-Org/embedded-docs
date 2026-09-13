# Imagem Latente Vazia HiDream-O1

Este nó cria uma imagem latente vazia no espaço de pixels para o modelo HiDream-O1-Image. Ele gera um tensor em branco de zeros que atua como ponto de partida para a geração de imagem, com dimensões definidas pelas entradas width, height e batch_size.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `width` | A largura da imagem latente em pixels. Padrão: 2048. O valor deve ser múltiplo de 32. O modelo foi treinado com cerca de 4 megapixels; resoluções menores podem reduzir a qualidade de forma perceptível. | INT | Sim | 64 a 4096 (step: 32) |
| `height` | A altura da imagem latente em pixels. Padrão: 2048. O valor deve ser múltiplo de 32. O modelo foi treinado com cerca de 4 megapixels; resoluções menores podem reduzir a qualidade de forma perceptível. | INT | Sim | 64 a 4096 (step: 32) |
| `batch_size` | O número de imagens latentes a serem geradas em um único lote. Padrão: 1. | INT | Sim | 1 a 64 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `samples` | Um tensor preenchido com zeros representando a imagem latente vazia, com formato (batch_size, 3, height, width). | LATENT |

## Notas

- O modelo HiDream-O1-Image foi treinado com aproximadamente 4 megapixels. Usar resoluções significativamente menores pode resultar em qualidade de imagem visivelmente reduzida.
- Resoluções de treinamento incluem: 2048x2048, 2304x1728, 1728x2304, 2560x1440, 1440x2560, 2496x1664, 1664x2496, 3104x1312, 1312x3104, 2304x1792, 1792x2304.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHiDreamO1LatentImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7412639e261512d9174e60009143c8c06c354e2a20ada7271837d72053426be5`
