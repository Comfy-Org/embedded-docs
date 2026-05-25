> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHiDreamO1LatentImage/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHiDreamO1LatentImage/en.md)

## Visão Geral

Este nó cria uma imagem latente vazia no espaço de pixels, projetada especificamente para o modelo HiDream-O1-Image. Ele gera um tensor vazio de zeros que serve como ponto de partida para a geração de imagens, com dimensões definidas pelas entradas de largura, altura e tamanho do lote.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `largura` | INT | Sim | 64 a 4096 (passo: 32) | A largura da imagem latente em pixels (padrão: 2048). O modelo foi treinado em ~4 megapixels; resoluções mais baixas saem da distribuição e a qualidade regride visivelmente. |
| `altura` | INT | Sim | 64 a 4096 (passo: 32) | A altura da imagem latente em pixels (padrão: 2048). O modelo foi treinado em ~4 megapixels; resoluções mais baixas saem da distribuição e a qualidade regride visivelmente. |
| `tamanho_do_lote` | INT | Não | 1 a 64 | O número de imagens latentes a serem geradas em um único lote (padrão: 1). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `samples` | LATENT | Um tensor preenchido com zeros representando a imagem latente vazia, com formato (batch_size, 3, height, width). |

## Notas

- O modelo HiDream-O1-Image foi treinado em aproximadamente 4 megapixels. O uso de resoluções significativamente mais baixas pode resultar em qualidade de imagem reduzida.
- As resoluções treinadas incluem: 2048x2048, 2304x1728, 1728x2304, 2560x1440, 1440x2560, 2496x1664, 1664x2496, 3104x1312, 1312x3104, 2304x1792, 1792x2304.

---
**Source fingerprint (SHA-256):** `fca32bbeddf120b4a7f9a9b88814f5345db133b35252c4d86079397be350c15e`
