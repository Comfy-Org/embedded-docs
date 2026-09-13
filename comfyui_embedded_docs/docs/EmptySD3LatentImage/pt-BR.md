# EmptySD3LatentImage

EmptySD3LatentImage cria uma imagem latente em branco (todos os valores zero) no layout esperado pelos modelos Stable Diffusion 3. Como o latente está vazio, ele normalmente é usado como ponto de partida que um fluxo de trabalho de geração preenche com uma imagem. A largura e a altura escolhidas determinam o tamanho da imagem final.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `width` | A largura da imagem latente em pixels (padrão: 1024). Os valores são incrementados em passos de 16. | INT | Sim | 16 a MAX_RESOLUTION (passo: 16) |
| `height` | A altura da imagem latente em pixels (padrão: 1024). Os valores são incrementados em passos de 16. | INT | Sim | 16 a MAX_RESOLUTION (passo: 16) |
| `batch_size` | O número de imagens latentes a serem geradas no lote (padrão: 1). | INT | Sim | 1 a 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `LATENT` | Um tensor latente contendo amostras em branco (todos os valores zero) no formato compatível com SD3. O tensor tem 16 canais, é reduzido por um fator de 8 em relação a `width` e `height`, e carrega uma taxa de redução espacial de 8. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `694ede56f43e3f3889b4d23e636fa6b33b490bcbd214584557f0dc883fa0a32d`
