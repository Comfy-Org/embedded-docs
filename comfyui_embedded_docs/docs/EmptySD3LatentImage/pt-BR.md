# EmptySD3LatentImage

EmptySD3LatentImage cria um tensor de imagem latente em branco, formatado especificamente para modelos Stable Diffusion 3. Ele gera um tensor preenchido com zeros que possui as dimensões e a estrutura corretas esperadas pelos pipelines SD3. É comumente usado como ponto de partida para fluxos de trabalho de geração de imagens.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `largura` | A largura da imagem latente de saída em pixels (padrão: 1024) | INT | Sim | 16 to MAX_RESOLUTION (step: 16) |
| `altura` | A altura da imagem latente de saída em pixels (padrão: 1024) | INT | Sim | 16 to MAX_RESOLUTION (step: 16) |
| `tamanho_do_lote` | O número de imagens latentes a serem geradas em um lote (padrão: 1) | INT | Sim | 1 a 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `LATENT` | Um tensor latente contendo amostras em branco com dimensões compatíveis com SD3. O tensor possui 16 canais e é reduzido espacialmente por um fator de 8 em relação à largura e altura de entrada. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `694ede56f43e3f3889b4d23e636fa6b33b490bcbd214584557f0dc883fa0a32d`
